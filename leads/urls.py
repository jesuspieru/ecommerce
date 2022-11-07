from django.urls import path
from .views import lead_delete, LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name="lead-list"),
    path('<int:pk>/', LeadDetailView.as_view()),
    path('<int:pk>/update/', LeadUpdateView.as_view()),
    path('<int:pk>/delete/', lead_delete),
    path('create/', LeadCreateView.as_view()),
]