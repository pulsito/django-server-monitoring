from django.contrib import admin
from django.urls import path, include
from studyproject import settings
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('servermonitoring.urls')),
    path('profile/', include('django.contrib.auth.urls')),
    path('profile/oauth/', include('social_django.urls', namespace='social')),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL},
         name='logout'),
]
