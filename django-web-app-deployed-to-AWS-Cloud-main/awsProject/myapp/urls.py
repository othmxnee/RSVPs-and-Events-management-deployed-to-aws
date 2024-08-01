from django.db import router
from django.urls import path,include

from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'invitations', views.InvitationViewSet, basename='invitation')

urlpatterns = [
    path('event/',views.EventView.as_view()),
    path('event/<int:pk>/',views.SingleEventView.as_view()),
    path('', include(router.urls)),
   
    
]