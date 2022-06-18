from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('candidates/<int:pk>/', views.CandidateDetailView.as_view(), name='candidate'),
    path('candidates/', views.CandidateListView.as_view(), name='candidates'),
    path('candidates/<int:pk>/add/', views.tag_create, name='add_tags'),
    path('candidates/<int:candidate_id>/<int:pk>/delete_tag/', views.tag_delete, name='delete_tag'),
]
