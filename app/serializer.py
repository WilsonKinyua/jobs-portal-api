from .models import *
from rest_framework import serializers


# user serializer
class UserSerializer(serializers.ModelSerializer):
    """
    user serializer
    """
    class Meta:
        model = User
        exclude = ('password','user_permissions','id','groups','is_superuser','is_staff','is_active','date_joined','last_login')


# create user serializer
class UserCreationSerializer(serializers.ModelSerializer):
    """
        This method is used to serialize the user object
        Args:
            user: user object
    """

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

# jobs category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'icon', 'description')


# jobs serializer
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('company_name', 'company_email', 'company_phone', 'company_website', 'company_linkedin', 'company_logo', 'company_location', 'title', 'slug', 'category',
                  'description', 'salary_range', 'job_type', 'job_description', 'location', 'application_deadline', 'experience', 'qualification', 'link_to_job', 'user', 'created_at')
        extra_kwargs = {'user': {'read_only': True}}


# create job serializer
class CreateJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('company_name', 'company_email', 'company_phone', 'company_website', 'company_linkedin', 'company_logo', 'company_location', 'title', 'category',
                  'description', 'salary_range', 'job_type', 'job_description', 'location', 'application_deadline', 'experience', 'qualification', 'link_to_job', 'user')
        extra_kwargs = {'user': {'read_only': True}}

    # create job
    def create(self, validated_data):
        job = Job.objects.create(**validated_data)
        return job

    # # update job
    # def update(self, instance, validated_data):
    #     instance.company_name = validated_data.get('company_name', instance.company_name)
    #     instance.company_email = validated_data.get('company_email', instance.company_email)
    #     instance.company_phone = validated_data.get('company_phone', instance.company_phone)
    #     instance.company_website = validated_data.get('company_website', instance.company_website)
    #     instance.company_linkedin = validated_data.get('company_linkedin', instance.company_linkedin)
    #     instance.company_logo = validated_data.get('company_logo', instance.company_logo)
    #     instance.company_location = validated_data.get('company_location', instance.company_location)
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.category = validated_data.get('category', instance.category)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.salary_range = validated_data.get('salary_range', instance.salary_range)
    #     instance.job_type = validated_data.get('job_type', instance.job_type)
    #     instance.job_description = validated_data.get('job_description', instance.job_description)
    #     instance.location = validated_data.get('location', instance.location)
    #     instance.application_deadline = validated_data.get('application_deadline', instance.application_deadline)
    #     instance.experience = validated_data.get('experience', instance.experience)
    #     instance.qualification = validated_data.get('qualification', instance.qualification)
    #     instance.link_to_job = validated_data.get('link_to_job', instance.link_to_job)
    #     instance.user = validated_data.get('user', instance.user)
    #     instance.save()
    #     return instance
