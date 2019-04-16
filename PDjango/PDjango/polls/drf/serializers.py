from polls.models import Question, Choice
from rest_framework import serializers
# from django.contrib.auth.models import User


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'url', 'question_text', 'pub_date')

    def save(self, *args, **kwargs):
        super().save(owner=self.context['request'].user)


class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'url', 'question', 'choice_text', 'votes')


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'url', 'choice_text', 'votes')


# class UserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ('id', 'username')
