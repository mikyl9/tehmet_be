"""
URL configuration for tehmet project.

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
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from feedback.views import EmailFormView
from projects.views import ProjectViewSet

projects_router = DefaultRouter()
projects_router.register("", ProjectViewSet, "projects")

urlpatterns = [
    path("admin24/", admin.site.urls),
    path("api/v1/projects/", include(projects_router.urls)),
    path("api/v1/feedback/", EmailFormView.as_view(), name="feedback"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
