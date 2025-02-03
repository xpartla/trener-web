"""
URL configuration for fitApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('superuser/', views.show_superuser_name),
    path('', views.show_index),
    path('diet/', views.show_diet),
    path('training/', views.show_training),
    path('coaching/', views.show_coaching),
    path('body_part/new/', views.body_part_create, name='body_part_create'),  # Create
    path('body_part/<int:pk>/edit/', views.body_part_update, name='body_part_update'),  # Update
    path('body_part/<int:pk>/delete/', views.body_part_delete, name='body_part_delete'),  # Delete
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)