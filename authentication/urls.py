from django.urls import path, include
from . import views

urlpatterns =\
[
    path('users/', views.users, name='users'),
    path('users/<int:user_id>/', views.user_item, name='user_item'),
    path('users/delete/<int:user_id>/', views.delete_user),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/signup/', views.register, name="create_user"),
    path('users/signup/<int:user_id>/', views.update_user, name="update_user"),
    path('accounts/profile/', views.user_profile, name='user_profile'),
]