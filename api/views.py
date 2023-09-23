
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render
from djoser.conf import settings
from djoser.permissions import CurrentUserOrAdmin
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from api.models import Student, Professor
from api.serializers import StudentSerializer, StudentCreateSerializer, ProfessorSerializer, ProfessorCreateSerializer


class ProfessorViewSet(ModelViewSet):
    serializer_class = ProfessorSerializer
    queryset = Professor.objects.all()
    token_generator = default_token_generator
    lookup_field = settings.USER_ID_FIELD
    permission_classes = [IsAdminUser, ]

    def permission_denied(self, request, **kwargs):
        if all((
                settings.HIDE_USERS,
                request.user.is_authenticated,
                self.action in ["update", "partial_update", "list", "retrieve"]
        )):
            raise NotFound()
        super().permission_denied(request, **kwargs)

    def get_serializer_class(self):
        if self.action == "create":
            return ProfessorCreateSerializer
        return self.serializer_class

    def update(self, request, *args, **kwargs):
        return super().update(request, partial=True)

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        if settings.HIDE_USERS and self.action == "list" and not user.is_staff and user.get_role() == "curator":
            queryset = queryset.filter(pk=user.curator.pk)
        return queryset

    def get_permissions(self):
        if self.action in ("retrieve", "update", "partial_update", "list"):
            self.permission_classes = [CurrentUserOrAdmin, ]
        return super().get_permissions()


class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    token_generator = default_token_generator
    lookup_field = settings.USER_ID_FIELD
    permission_classes = [IsAdminUser, ]

    def permission_denied(self, request, **kwargs):
        if all((
            settings.HIDE_USERS,
            request.user.is_authenticated,
            self.action in ["update", "partial_update", "list", "retrieve"]
        )):
            raise NotFound()
        super().permission_denied(request, **kwargs)

    def get_serializer_class(self):
        if self.action == "create":
            return StudentCreateSerializer
        return self.serializer_class

    def update(self, request, *args, **kwargs):
        if request.user.get_role() == "student":
            prev_data = {'user': request.data.pop("user", {})}
            request.data.clear()
            request.data.update(prev_data)
        return super().update(request, partial=True)

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        if settings.HIDE_USERS and self.action == "list" and not user.is_staff and user.get_role() == "student":
            queryset = queryset.filter(pk=user.student.pk)
        return queryset

    def get_permissions(self):
        if self.action in ("retrieve", "update", "partial_update", "list"):
            self.permission_classes = [CurrentUserOrAdmin, ]
        return super().get_permissions()