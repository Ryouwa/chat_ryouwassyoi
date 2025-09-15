from django.urls import path
from . import views
from .models import Article
from django.views import generic  

app_name = 'board'
 
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),           #http://localhost:8000/board/ なら トップページ
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view, name='create'),
    path('<int:id>/update/', views.UpdateView.as_view, name='update'),
    path('<int:id>/delete/', views.Deleteview.as_view, name='delete'),
]

