from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),

    path('ads/',views.ads,name='ads'),
    path('delete-ads/',views.delete_ads,name='delete_ads'),
    path('ads/<int:pk>/',views.ads_detail,name='ads-detail'),

    path('advertiser/dashboard/',views.ad_dasboard,name='ad-dashboard'),
     path('advertiser/my-ads/',views.my_ads,name='my-ads'),
    path('advertiser/create_ad/',views.create_ad,name='create-ad'),
    path('advertiser/create_ad/checkout/',views.create_ad_checkout,name='create-ad-checkout'),
    path('advertiser/create_ad/complete/<int:pk>',views.create_ad_checkout_complete,name='create-ad-checkout-complete'),

    path('taskers/dashboard/',views.pub_dasboard,name='pub-dashboard'),
    path('taskers/withdraw/',views.withdraw,name='pub-withdraw'),
    path('taskers/subscribe/',views.subcribe,name='pub-subcribe'),
    path('taskers/withdraw-history/',views.with_history,name='pub-history'),
]