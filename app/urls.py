from django.urls import include,path
from rest_framework.authtoken import views as token_views
from .views import *

urlpatterns = [
    path('user/create/', createUser.as_view(), name='create_user'), # create user
    path('user/details/', getUser.as_view(), name='get_user'), # get user
    path('category/list/', CategoryList.as_view(), name='category_list'), # list categories
    path('jobs/', JobList.as_view(), name='job_list'),
]