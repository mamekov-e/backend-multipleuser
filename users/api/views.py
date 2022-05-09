# from django.http import request
# from rest_framework.response import Response
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from .serializers import EmployeeSignupSerializer, \
    DirectorSignupSerializer, UserSerializer, UserTokenObtainPairSerializer

from .permissions import IsEmployeeUser, IsDirectorUser

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class EmployeeSignupView(generics.GenericAPIView):
    serializer_class = EmployeeSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "account created successfully"
        })


class DirectorSignupView(generics.GenericAPIView):
    serializer_class = DirectorSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "account created successfully"
        })


class EmployeeOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated & IsEmployeeUser]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class DirectorOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated & IsDirectorUser]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/token/',
            'method': 'POST, OPTIONS',
            'body': {'username': '', 'password': ''},
            'description': 'Creates and returns the access and refresh tokens',
        },
        {
            'Endpoint': '/token/refresh/',
            'method': 'POST, OPTIONS',
            'body': {'refresh': ''},
            'description': 'Refreshes and returns the access and refresh tokens',
        },
    ]

    return Response(routes)


# class LogoutView(APIView):
#
#     permission_classes = (permissions.IsAuthenticated,)
#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)


# class CustomAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'is_employee': user.is_employee,
#             'is_director': user.is_director
#         })


# class LogoutView(APIView):
#     def post(self, request, format=None):
#         request.auth.delete()
#         return Response({
#             "message": "user successfully logout"
#         })


