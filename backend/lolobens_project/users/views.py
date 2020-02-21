from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from lolobens_project.users.models import User
from lolobens_project.users.permissions import IsSuperUser, IsLoggedInUser
from lolobens_project.users.serializers import UserSerializer


class GetAllUser(ListAPIView):
    """
    GET: List of all users.
    Only Admin can GET Request.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUser, IsAuthenticated]


class RetrieveUpdateUserAccount(RetrieveUpdateAPIView):
    """
    GET: Retrieve account of current user.
    PATCH: Update account of current user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsLoggedInUser]

    def get_object(self):
        return self.request.user


class RetrieveSpecificUser(RetrieveAPIView):
    """
    GET: Retrieve account of user with ID.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUser, IsAuthenticated]
    lookup_url_kwarg = 'user_id'
