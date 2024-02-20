from django.contrib.auth.views import LogoutView
from django.urls import path

from blog import settings
from .views import MainView, PostDetailView, SignUpView, SignInView, log_out

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('logout/', log_out, name='logout',),
    path('blog/<slug>/', PostDetailView.as_view(), name='post_detail'),
]
