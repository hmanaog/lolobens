from django.urls import path

from lolobens_project.users.views import GetAllUser, RetrieveUpdateUserAccount, RetrieveSpecificUser

urlpatterns = [
    path('admin/', GetAllUser.as_view(), name='get all user'),
    path('customer/', RetrieveUpdateUserAccount.as_view(), name='retrieve update user account'),
    path('customer/id/<int:user_id>/', RetrieveSpecificUser.as_view(), name='retrieve specific user'),
]
