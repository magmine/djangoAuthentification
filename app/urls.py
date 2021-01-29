from . import views
from django.urls import path, include
from .views import SignUpView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(template_name='registration/signup.html'), name='signup'),
]