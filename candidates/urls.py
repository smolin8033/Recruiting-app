from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('candidate/<int:pk>/', views.CandidateDetailView.as_view(), name='candidate'),
]
