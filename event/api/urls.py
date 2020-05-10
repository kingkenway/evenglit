from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view

app_name = 'event'

schema_view = get_swagger_view(title='Event API')

urlpatterns = [
    path('swagger-docs/', schema_view),

    path('event/overview', views.apiOverview, name='api-overview'),
    path('eventtype/', views.EventTypeView.as_view(), name='event_type'),
    
    # -
    # path('event/', views.EventListView.as_view(), name='event_list'),
    # path('event/<pk>/', views.EventDetailView.as_view(), name='event_detail'),
    # path('eventtype/', views.EventTypeView.as_view(), name='event_type'),

    path('event/', views.EventListView.as_view(), name='event_list'),
    path('event/<int:id>/', views.EventDetailView.as_view(), name='event_detail'),

]