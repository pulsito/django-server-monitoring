from django.urls import path, include
from studyproject import settings
from django.contrib.auth.views import LogoutView
from . import views
from .views import ServersAPIView, ServerAPIView, FilesAPIView, ServerLocationAPIView

urlpatterns = [
    path('', views.index),
    path('server/<int:id>', views.get_server_info),

    path('profile/secure/', views.secure),
    path('profile/', include('django.contrib.auth.urls')),
    path('profile/oauth/', include('social_django.urls', namespace='social')),

    path('api/servers', ServersAPIView.as_view()),
    path('api/servers/<int:id>/', ServerAPIView.as_view()),
    path('api/servers/<int:id>/location', ServerLocationAPIView.as_view()),
    path('api/files/csv', FilesAPIView.as_view()),

]