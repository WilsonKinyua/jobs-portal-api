from .serializer import *
from .models import *
from django.http import JsonResponse
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.schemas import get_schema_view
from drf_yasg.utils import swagger_auto_schema
# from rest_framework.permissions import IsAuthenticated

# create user
class createUser(APIView):
    """This handles user creation functionality
    Args:
        generics ([type]): [description]
    """

    schema = get_schema_view()

    @swagger_auto_schema(
        operation_description="Create a new user",
        request_body=UserCreationSerializer,
    )
    def post(self, request, format=None):
        data = {}
        serializer = UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'User created successfully'
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# using token get user
class getUser(APIView):
    """This handles user functionality
    Args:
        generics ([type]): [description]
    """
    
    def get_object(self, token):
        try:
            return User.objects.get(auth_token=token)
        except User.DoesNotExist:
            raise Http404
        
    def get(self, request, format=None):
        data = {}
        if request.META.get('HTTP_AUTHORIZATION') is None:
            data['error'] = 'Invalid token'
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        user = self.get_object(request.META.get('HTTP_AUTHORIZATION'))
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        

# list categories
class CategoryList(APIView):
    """
        category list view
    """

    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


# jobs
class JobList(APIView):
    """
        job list view
    """
    schema = get_schema_view()

    def get(self, request, format=None):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Job Application",
        request_body=CreateJobSerializer,
    )
    # create job
    def post(self, request, format=None):
        serializer = CreateJobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
