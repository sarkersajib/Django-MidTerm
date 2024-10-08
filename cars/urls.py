from django.contrib import admin
from django.urls import path, include
from . import views
#from .views import ProfileView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add/',views.AddCarCreateView.as_view(),name='add_car'),
    path('edit/<int:id>/',views.EditCarView.as_view(),name='edit_car'),
    path('delete/<int:id>/',views.DeleteCarView.as_view(),name='delete_car'),
    path('details/<int:id>/',views.DetailCarView.as_view(),name='detail_car'),
    path('buy/<int:id>/', views.buy_car, name='buy_car'),
    path('order/<int:id>/', views.ProfileView.as_view(), name='order'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)