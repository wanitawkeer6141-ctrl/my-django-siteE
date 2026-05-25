from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



# urlpatterns = [
#     path('login/', views.login_view, name='login'),   
#     path('signup/', views.sign_up, name='signup'),
#     path('', views.home, name='home'),
# ]


urlpatterns = [
    # path('login/', views.login_view, name='login'),  
    path('home/', views.home, name='home'),
    # path('signup/', views.sign_up, name='signup'),
    path('',views.front,name='front'),
    path('taa/',views.taa,name='taa'),
    # path('logout/', views.logout_view, name='logout'),
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)