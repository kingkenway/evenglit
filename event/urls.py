from django.urls import path, include
from . import views

urlpatterns = [
    # path('e/<int:pk>-<str:slug>/', views.ArticleDetailView, name='event_detail')

    # path('api/', api_views.EventListView.as_view(), name=None),
    path('', views.event_home, name='home'),
    path('<str:slug>-<int:pk>/', views.event_detail, name='event_detail'),

    path('create/', views.create_event, name='create_event'),
    path('edit/<int:id>/', views.edit_event, name='edit_event'),
    path('delete/<int:id>/', views.delete_event, name='delete_event'),

    path('<str:username>/', views.profile_view, name="user_detail"),

    
]