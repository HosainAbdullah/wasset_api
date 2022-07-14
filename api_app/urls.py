from django.urls import path, include
from rest_framework import permissions
from rest_framework import viewsets
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'User' , views.WstUserViewSet)
router.register(r'TypeUser', views.TypeUserViewSet)
router.register(r'BankAcount', views.BankAcountViewSet)
router.register(r'Image', views.ImageViewSet)
router.register(r'TypeSer', views.TypeSerViewSet)
router.register(r'Service', views.ServiceViewSet)
router.register(r'Status', views.StatusViewSet)
router.register(r'Contract', views.ContractViewSet)
router.register(r'Evaluation', views.EvaluationViewSet)
router.register(r'TypeCom', views.TypeComViewSet)
router.register(r'Complaint', views.ComplaintViewSet)
router.register(r'Tesk', views.TeskViewSet)
router.register(r'Notification', views.NotificationViewSet)
router.register(r'Help', views.HelpViewSet)

urlpatterns = [
    # path('home/',views.UserPage),
    path('', include(router.urls)),
    path('api-waseet/', include('rest_framework.urls', namespace='rest_framework'))
]