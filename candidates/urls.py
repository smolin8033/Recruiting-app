from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('candidates/<int:pk>/', views.CandidateDetailView.as_view(), name='candidate'),
    path('candidates/', views.CandidateListView.as_view(), name='candidates'),
]
