from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema, extend_schema_view

from .models import Profile
from .serializers import ProfileSerializer, UserSerializer


@extend_schema_view(
    list=extend_schema(summary='List all profiles', tags=['Profiles']),
    retrieve=extend_schema(summary='Retrieve a profile', tags=['Profiles']),
    create=extend_schema(summary='Create a profile', tags=['Profiles']),
    update=extend_schema(summary='Update a profile', tags=['Profiles']),
    partial_update=extend_schema(summary='Partial update a profile', tags=['Profiles']),
    destroy=extend_schema(summary='Delete a profile', tags=['Profiles']),
)
class ProfileViewSet(viewsets.ModelViewSet):
    """ViewSet for user profiles.

    Provides full CRUD operations on Profile objects.
    All endpoints require authentication (session or token).
    """

    queryset = Profile.objects.select_related('user').all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


@extend_schema_view(
    list=extend_schema(summary='List all users', tags=['Users']),
    retrieve=extend_schema(summary='Retrieve a user', tags=['Users']),
)
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for users (read-only).

    Provides list and detail views for registered users.
    Each user includes nested profile data.
    All endpoints require authentication.
    """

    queryset = User.objects.select_related('profile').all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
