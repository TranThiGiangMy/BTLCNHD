from django.urls import path, include
from . import views
from .admin import admin_site
from rest_framework.routers import DefaultRouter


router =DefaultRouter()
router.register('booking',views.RoutesViewSet)



urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin_site.urls),
    # path('user/', views.userPage, name="user-page"),
        path('register/', views.registerPage, name="register"),
        path('login/', views.loginPage, name="login"),
        # path('logout/', views.logoutUser, name="logout"),

    # path('', views.home, name="home"),
    path('', include('booking.urls')),
    # path('user/', views.userPage, name="user-page"),
    # path('products/', views.products, name='products'),
    # path('customer/<str:pk_test>/', views.customer, name="customer"),

]


