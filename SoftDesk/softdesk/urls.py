"""softdesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenRefreshView, \
    TokenObtainPairView
from projects import views
from data import views as data_views


router = routers.DefaultRouter()
router.register(r'signup', data_views.UserViewSet)
router.register(r'project', views.ProjectViewSet)

project_router = routers.NestedSimpleRouter(router, r'project',
                                            lookup='project')
project_router.register(r'issue', views.IssueViewSet, basename='project-issue')
project_router.register(r'users', views.ContributorViewSet,
                        basename='project-contributor')

issue_router = routers.NestedSimpleRouter(project_router, r'issue',
                                          lookup='issue')
issue_router.register(r'comment', views.CommentViewSet,
                      basename='issue-comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(project_router.urls)),
    path('', include(issue_router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
