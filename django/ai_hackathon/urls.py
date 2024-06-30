"""
URL configuration for ai_hackathon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from ai_hackathon import settings
from rest_framework.routers import DefaultRouter
from ai_hackathon_api.views import CompanyViewSet, PostStatusAIView, PostStatusView, RolesView, TaskTypeView, UsersView, TaskView, PostView, PostsView, CompanyView, CompaniesView, FileUploadView, RoleViewSet, UserView, RoleView
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'companies', CompanyViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include((router.urls, 'ai_hackathon_api'), namespace='ai_hackathon_api')),
    path('api/companies', CompaniesView.as_view(), name='ai_hackathon_api'),
    path('api/company', CompanyView.as_view(), name='ai_hackathon_api'),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('api/user/post', PostView.as_view(), name='ai_hackathon_api'),
    path('api/user/posts', PostsView.as_view(), name='ai_hackathon_api'),
    path('api/user/post/status', PostStatusView.as_view(), name='ai_hackathon_api'),
    path('api/user/post/ai', PostStatusAIView.as_view(), name='ai_hackathon_api'),

    path('api/user', UserView.as_view(), name='ai_hackathon_api'),
    path('api/users', UsersView.as_view(), name='ai_hackathon_api'),

    path('api/user/role', RoleView.as_view(), name='ai_hackathon_api'),
    path('api/user/roles', RolesView.as_view(), name='ai_hackathon_api'),

    path('api/company/task', TaskView.as_view(), name='ai_hackathon_api'),
    path('api/company/task/type', TaskTypeView.as_view(), name='ai_hackathon_api'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)