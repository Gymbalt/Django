from .serializers import QuestionSerializer, ChoiceSerializer, ChoicesSerializer
from polls.models import Choice, Question
from rest_framework import viewsets, permissions
from .filters import QuestionFilter, ChoiceFilter
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import detail_route


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filterset_class = QuestionFilter
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class ChoicesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoicesSerializer
    filterset_class = ChoiceFilter


class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = ChoiceSerializer
    filterset_class = ChoiceFilter

    @detail_route(methods=['post'])
    def vote1(self, request, **kwargs):
        choice = self.get_object()
        choice.votes += 1
        choice.save()
        return Response(self.serializer_class(instance=choice).data)

    def get_queryset(self):
        return Choice.objects.filter(question=self.kwargs['question_pk'])

# class UsersViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     filterset_class = UserFilter
