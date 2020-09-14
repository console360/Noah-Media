from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
from django.utils import timezone
from drf_yasg.inspectors import CoreAPICompatInspector
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from noah import custom_status_codes
from noah import responses
from noah.permissions import IsAuthenticated
from .models import User
from .serializers import UserSignUpSerializer, UserSerializer, UserLoginSerializer, UserProfileSerializer, \
    UserForgetPassword
from .utils import send_forgot_password_email


class UserSignup(APIView):

    @swagger_auto_schema(request_body=UserSignUpSerializer, tags=['User'])
    def post(self, requests):
        requests.data['email'] = requests.data['email'].lower()

        serializer = UserSignUpSerializer(data=requests.data)

        if not serializer.is_valid():
            return Response(responses.generate_failure_response(custom_status_codes.USERS_SIGN_UP_FAILURE,
                                                                payload=serializer.errors),
                            status=status.HTTP_400_BAD_REQUEST)

        # Check if email address already exists
        if User.objects.filter(email=requests.data['email']).exists():
            return Response(
                responses.generate_failure_response(
                    custom_status_codes.USER_ACCOUNT_ALREADY_EXISTS,
                    payload=serializer.errors),
                status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(name=requests.data['name'], email=requests.data['email'],
                                        password=requests.data['password'], last_login=timezone.now())

        # retrieved token
        token = Token.objects.get(user_id=user.id)

        user_serializer = UserSerializer(user)

        return Response(responses.generate_success_response(custom_status_codes.USERS_SIGN_UP_SUCCESS,
                                                            payload={'user': user_serializer.data, 'token': token.key}),
                        status=status.HTTP_200_OK)


class UserSignIn(APIView):

    @swagger_auto_schema(request_body=UserLoginSerializer, tags=['User'])
    def post(self, requests):
        requests.data['email'] = requests.data['email'].lower()

        serializer = UserLoginSerializer(data=requests.data)
        if not serializer.is_valid():
            return Response(
                responses.generate_failure_response(
                    custom_status_codes.USERS_SIGN_IN_FAILURE,
                    payload=serializer.errors),
                status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=requests.data['email'])

            if user.is_deleted:
                return Response(
                    responses.generate_failure_response(custom_status_codes.USER_DOES_NOT_EXISTS,
                                                        payload={}), status=status.HTTP_400_BAD_REQUEST)
            user = authenticate(email=requests.data['email'], password=requests.data['password'])

            if user is not None:
                login(requests, user)
                token = Token.objects.get_or_create(user_id=user.id)
                user_serializer = UserSerializer(user)
                return Response(responses.generate_success_response(custom_status_codes.USERS_SIGN_IN_SUCCESS,
                                                                    payload={'user': user_serializer.data,
                                                                             'token': token[0].key}),
                                status=status.HTTP_200_OK)
            else:
                return Response(
                    responses.generate_failure_response(custom_status_codes.USERS_SIGN_IN_FAILURE, payload={}),
                    status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response(
                responses.generate_failure_response(custom_status_codes.USERS_SIGN_IN_FAILURE,
                                                    payload={}), status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPI(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(request_body=UserProfileSerializer, filter_inspectors=[CoreAPICompatInspector], tags=['User'])
    def put(self, requests, user_id):
        # TODO(OM): If user update a password then logout them automatically
        try:

            user = User.objects.get(id=user_id)

            # As we are having the same api to update password if user asked
            if 'password' in requests.data and 'current_password' in requests.data and not user.check_password(
                    requests.data['current_password']):
                # New password and current password provided. But current password is wrong.
                return Response(
                    responses.generate_failure_response(custom_status_codes.USERS_INVALID_OLD_PASSWORD_ERR,
                                                        payload={}), status=status.HTTP_400_BAD_REQUEST)
            elif 'password' in requests.data and 'current_password' not in requests.data:
                # New password provided. But current password isn't provided.
                return Response(
                    responses.generate_failure_response(custom_status_codes.USERS_MISSING_OLD_PASSWORD_ERR,
                                                        payload={}), status=status.HTTP_400_BAD_REQUEST)
            else:
                requests.data['is_system_generated_password'] = False

            serializer = UserProfileSerializer(user, data=requests.data, partial=True)
            if not serializer.is_valid():
                return Response(
                    responses.generate_failure_response(
                        custom_status_codes.USER_UPDATE_INVALID_DETAIL,
                        payload={}), status=status.HTTP_400_BAD_REQUEST)

            serializer.save()

            user_serializer = UserSerializer(user)

            return Response(
                responses.generate_success_response(
                    custom_status_codes.USER_DETAIL_GET_UPDATED,
                    payload=user_serializer.data),
                status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response(
                responses.generate_failure_response(custom_status_codes.USER_DOES_NOT_EXISTS,
                                                    payload={}), status=status.HTTP_400_BAD_REQUEST)

    # Disable hard delete API
    # @swagger_auto_schema(tags=['User'])
    # def delete(self, requests, user_id):
    #
    #     try:
    #         user = User.objects.get(id=user_id)
    #
    #         user.delete()
    #
    #         # TODO(Akshay): Delete user related all the data
    #
    #         return Response(
    #             responses.generate_success_response(
    #                 custom_status_codes.USER_DELETED_SUCCESS,
    #                 payload={}),
    #             status=status.HTTP_200_OK)
    #
    #     except User.DoesNotExist:
    #         return Response(
    #             responses.generate_failure_response(custom_status_codes.USER_DOES_NOT_EXISTS,
    #                                                 payload={}), status=status.HTTP_400_BAD_REQUEST)


class UserLogout(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(tags=['User'])
    def put(self, requests):

        try:
            requests.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            return Response(
                responses.generate_failure_response(custom_status_codes.USERS_SIGN_OUT_FAIL,
                                                    payload={}), status=status.HTTP_400_BAD_REQUEST)

        logout(requests)

        return Response(responses.generate_success_response(custom_status_codes.USERS_SIGN_OUT_SUCCESS, payload={}),
                        status=status.HTTP_200_OK)


class UserForgotPasswordAPI(APIView):

    @swagger_auto_schema(request_body=UserForgetPassword, tags=['User'])
    def put(self, request):
        request.data['email'] = request.data['email'].lower()

        if 'email' not in request.data:
            return Response(responses.generate_failure_response(
                custom_status_codes.EMAIL_IS_REQUIRED_FOR_PASSWORD_RESET_REQUEST,
                payload={}),
                status=status.HTTP_400_BAD_REQUEST)

        email = request.data['email']

        try:

            user = User.objects.get(email=email)

            new_password = User.objects.make_random_password()

            ok, message_id = send_forgot_password_email(user, new_password)

            if not ok:
                return Response(responses.generate_failure_response(
                    custom_status_codes.USERS_NEW_PASSWORD_ERR, payload={}),
                    status=status.HTTP_503_SERVICE_UNAVAILABLE)

            # Update password
            user.set_password(new_password)
            user.is_system_generated_password = True
            user.save()

            return Response(responses.generate_success_response(custom_status_codes.USERS_NEW_PASSWORD_SET,
                                                                payload={'isSent:': ok, 'message': message_id}),
                            status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response(responses.generate_failure_response(
                custom_status_codes.USER_DOES_NOT_EXISTS, payload={}),
                status=status.HTTP_400_BAD_REQUEST)
