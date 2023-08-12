from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/register', views.register, name='register-user'),
    path('accounts/login/', views.login, name='login-user'),
    path('accounts/logout/', views.logout, name='logout-user'),
    path('accounts/password/reset/', views.forgot_password,
         name='password-forgot-user'),
    path('accounts/password/reset/', views.password_reset_method, name='password-reset-web-page'),
    path('accounts/update/user/profile/', views.UpdateProfileView.as_view(), name='auth_update_profile'),
    path('accounts/userprofile/',views.UserProfileView.as_view(),name="user_profile"),
    path('accounts/profilepage/',views.profileUser,name="userprofilepage"),
    path('accounts/user/ordershistory/',
         views.userOrderDetail, name="orderhistoryuser"),
    path('accounts/user/ordershistory/order-detail/<int:pk>/',
         views.userOrderDetailExpanded, name="orderhistorydetail"),
    path('accounts/register/get_otp/', views.get_otp, name='get_otp'),
    path('accounts/register/verify/', views.verify_otp, name='verify_otp'),
    path('accounts/profile/dashboard/',views.profileDashboard,name="profile-dashboard"),
    path('accounts/profile/address/', views.user_address, name="profile-address"),
    path('accounts/profile/address/delete/<int:pk>',
         views.delete_user_address, name="delete-profile-address"),
    path('accounts/profile/address/set-primary/<int:pk>',
         views.set_primary_address, name="set-primary-profile-address"),
    path('accounts/profile/payment/', views.user_payment, name="profile-payments"),
    path('accounts/profile/orders/', views.user_orders, name="profile-orders"),
    path('accounts/profile/notification/',
         views.user_notification, name="profile-notification"),
    path('accounts/profile/coupon/',
         views.user_coupon, name="profile-coupon"),
     # path('accounts/user/dashboard/',views.userDashboard,name="user-dashboard"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                          document_root=settings.MEDIA_ROOT)


