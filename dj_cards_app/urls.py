from django.urls import path
from . import views

urlpatterns = [
    path('business/', views.BusinessCreateView.as_view(), name='business'),
    path('business/all/', views.BusinessCardView.as_view(), name='business_card'),
]