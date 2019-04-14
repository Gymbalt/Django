from .serializers import QuestionSerializer, ChoiceSerializer, UserSerializer
from polls.models import Choice, Question
from rest_framework import viewsets, permissions
from .filters import QuestionFilter, ChoiceFilter, UserFilter
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filterset_class = QuestionFilter
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class ChoicesViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    filterset_class = ChoiceFilter
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter
