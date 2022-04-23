from .serializer import *
from .models import *
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.schemas import get_schema_view
from drf_yasg.utils import swagger_auto_schema


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
        jobs list view
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


# single job
class JobDetail(APIView):
    """
        job detail view
    """
    schema = get_schema_view()

    def get_object(self, pk):
        try:
            return Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        job = self.get_object(pk)
        serializer = JobSerializer(job)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Update a Job Application",
        request_body=CreateJobSerializer,
    )
    # update job
    def put(self, request, pk, format=None):
        job = self.get_object(pk)
        serializer = CreateJobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Job Application",
    )
    # delete job
    def delete(self, request, pk, format=None):
        job = self.get_object(pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# get all jobs by category_id
class JobByCategory(APIView):
    """
        job by category view
    """
    schema = get_schema_view()

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        jobs = Job.objects.filter(category=category)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)


# get all jobs by user_id
class JobByUser(APIView):
    """
        job by user view
    """
    schema = get_schema_view()

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        jobs = Job.objects.filter(user=user)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
