import django
django.setup()

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework_simplejwt.views import TokenObtainPairView

from datetime import datetime
from multiprocessing import Process, Queue
import imageio

from .serializers import AdditionalUserInfoSerializer, PlanetLogSerializer, PlanetSerializer, UserInfoSerializer
from .serializers import BasicUserInfoSerializer
from .serializers import PlanetLog
from user.serializers import UserSerializer
from user.jwt_claim_serializer import CustomTokenObtainPairSerializer

from .models import Planet, PlanetLog

from makemigrations.permissions import HasNoUserInfoUser
from deeplearning.deeplearning_make_portrait import make_portrait


q = Queue()
p = None

DEFAULT_COIN = 1000


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
            return Response({"message": "회원가입 완료"}, status=status.HTTP_200_OK)
                
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserInfoView(APIView):
    permission_classes = [HasNoUserInfoUser]
    
    def post(self, request):
        global q, p

        request.data['user'] = request.user.id
        pic = imageio.imread(request.data.pop('portrait')[0])

        basic_user_info_serializer = BasicUserInfoSerializer(data=request.data)
        if basic_user_info_serializer.is_valid():
            q.put(request.data)
            
            p = Process(target=make_portrait, args=(q, pic, request.user.id))
            p.start()

            return Response(status=status.HTTP_200_OK)

        return Response({"error": "failed"}, status=status.HTTP_400_BAD_REQUEST)


def save_user_info(data, q):
    while q.qsize() < 2:
        pass

    basic_info = q.get()

    data['portrait'] = q.get()

    data['user'] = basic_info['user']
    data['name'] = basic_info['name']
    data['name_eng'] = basic_info['name_eng']
    data['birthday'] = basic_info['birthday']

    user_info_serializer = UserInfoSerializer(data=data)
    if user_info_serializer.is_valid():
        user_info_serializer.save()
        
    return


class PlanetView(APIView):
    permission_classes = [HasNoUserInfoUser]

    def get(self, request):
        planets = Planet.objects.all()
        planet_serializer = PlanetSerializer(planets, many=True).data
        
        return Response(planet_serializer, status=status.HTTP_200_OK)

    def post(self, request):
        global p, q

        data = request.data

        planet_name = data.pop('planet')
        planet_id = Planet.objects.get(name=planet_name).id

        data['planet'] = planet_id

        planet_log_serializer = PlanetLogSerializer(data=data)
        if planet_log_serializer.is_valid():
            planet_log_serializer.save()
        else:
            return Response(planet_log_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        now = datetime.now()
        date = now.strftime('%m%d')
        data['identification_number'] = f'{planet_id}{date}{request.user.id}'
        data['last_date'] = now.strftime('%Y-%m-%d')
        data['coin'] = DEFAULT_COIN

        additional_user_info_serializer = AdditionalUserInfoSerializer(data=data)
        if additional_user_info_serializer.is_valid():
            planet_process = Process(target=save_user_info, args=(data, q))
            planet_process.start()

            return Response(status=status.HTTP_200_OK)

        PlanetLog.objects.filter(planet=data['planet'], floor=data['floor'], room_number=data['room_number']).delete()
        return Response({"error": "failed"}, status=status.HTTP_400_BAD_REQUEST)