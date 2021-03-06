from django.contrib import admin
from django.urls import include, path
from polls.drf.router import router, questions_router

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('polls_drf/', include(router.urls)),
    path('polls_drf/', include(questions_router.urls)),
    path('drf-auth/', include('rest_framework.urls')),
]
