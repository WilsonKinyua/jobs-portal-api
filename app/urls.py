from django.urls import path
from .views import *

urlpatterns = [
    path('user/create/', createUser.as_view(), name='create_user'), # create user
    path('user/details/', getUser.as_view(), name='get_user'), # get user
    path('category/list/', CategoryList.as_view(), name='category_list'), # list categories
    path('jobs/', JobList.as_view(), name='job_list'), # list jobs
    path('job/<int:pk>/details', JobDetail.as_view(), name='job_details'), # get job details
    path('category/<int:pk>/job/list', JobByCategory.as_view(), name='job_details'), # get job details
    path('user/<int:pk>/job/list', JobByUser.as_view(), name='job_details'), # get job details
]