from . import views
from django.urls import path, include
from .views import SignUpView

urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('login/', views.user_login, name='login'),
    path('signup/', SignUpView.as_view(template_name='registration/signup.html'), name='signup'),
]