from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user_app.api.serializers import RegistrationSerializer


@api_view(['POST',])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        data = {'logout': 'Logged Out Succesfully!'}
        return Response(data, status=status.HTTP_200_OK)


@api_view(['POST',])
def register_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['registration'] = 'Registration Successfull!'
            data['email'] = account.email
            data['username'] = account.username

            token, create = Token.objects.get_or_create(user=account)
            data['token'] = token.key

        else:
            data = serializer.errors

        return Response(data, status=status.HTTP_201_CREATED)
