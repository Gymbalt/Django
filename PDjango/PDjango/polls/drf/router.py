from rest_framework_nested import routers
from .viewsets import QuestionViewSet, ChoiceViewSet, ChoicesViewSet

router = routers.SimpleRouter()
router.register('questions', QuestionViewSet)
router.register('choices', ChoicesViewSet)

questions_router = routers.NestedSimpleRouter(router, 'questions', lookup='question')
questions_router.register('choices', ChoiceViewSet, base_name='question-choices')

