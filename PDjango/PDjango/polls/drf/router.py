from polls.drf.viewsets import QuestionsViewSet, ChoicesViewSet, UsersViewSet
from rest_framework import routers
from django.urls import path

router = routers.DefaultRouter()
router.register('questions', QuestionsViewSet)
router.register('choices', ChoicesViewSet)
router.register('users', UsersViewSet)

