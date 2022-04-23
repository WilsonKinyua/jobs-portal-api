from django.urls import include,path
from rest_framework.authtoken import views as token_views
from .views import *

urlpatterns = [
    path('user/create/', createUser.as_view(), name='create_user'), # create user
    path('category/list/', CategoryList.as_view(), name='category_list'), # list categories
    path('job/list/', JobList.as_view(), name='job_list'), # list categories
]