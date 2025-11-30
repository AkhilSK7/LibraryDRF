"""
URL configuration for LibraryAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import SimpleRouter
from books import views
from rest_framework_simplejwt import views as jwt_views

router=SimpleRouter()
router.register('library',views.LibraryView)
router.register('users',views.RegisterAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
path('search',views.SearchAPIView.as_view(),name="search"),
    path('login/',jwt_views.TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(),name='token_refresh'),
    path('logout',views.LogoutView.as_view(),name='logout')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

