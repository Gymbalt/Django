from polls.models import Question, Choice
from rest_framework import serializers
from django.contrib.auth.models import User


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'url', 'question_text', 'pub_date')

    def save(self, *args, **kwargs):
        super().save(owner=self.context['request'].user)


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'url', 'question', 'choice_text', 'votes')

    def save(self, *args, **kwargs):
        super().save(owner=self.context['request'].user)


class UserSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())
    choices = serializers.PrimaryKeyRelatedField(many=True, queryset=Choice.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'questions', 'choices')
