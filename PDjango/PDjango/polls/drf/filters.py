from django_filters import rest_framework as filters
from polls.models import Choice, Question
from django.contrib.auth.models import User


class QuestionFilter(filters.FilterSet):
    class Meta:
        model = Question
        fields = {
            'question_text': ['icontains'],
            'pub_date': ['iexact', 'lte', 'gte'],
        }


class ChoiceFilter(filters.FilterSet):
    class Meta:
        model = Choice
        fields = {
            'choice_text': ['icontains'],
            'votes': ['iexact', 'lte', 'gte'],
        }


class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'username': ['icontains'],
        }
