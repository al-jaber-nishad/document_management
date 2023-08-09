from django.urls import path
from authentication.views import user_views as views

urlpatterns = [
	path('register/', views.user_registration_view, name='user-registration'),
    
    path('login/', views.user_login_view, name='user-login'),

    path('profile/', views.user_detail_view, name='user-detail'),

]
