from django.shortcuts import render
from .serializers import *
from rest_framework import permissions
from rest_framework import viewsets
from api_app.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# def HomePage(request):
#     return render(request,"index.html")

# def UserPage(request):
#     if request.method == 'GET':
#        foo_instance = WstUser.objects.create()
#        return render(request , 'index.html')

# بيانات المستخدمين 
class WstUserViewSet(viewsets.ModelViewSet):
    queryset = WstUser.objects.all()
    serializer_class = WstUserSerializer    
    permission_classes = [permissions.IsAuthenticated]


# بيانات أنواع المستخدمين
class TypeUserViewSet(viewsets.ModelViewSet):
    queryset = TypeUser.objects.all()
    serializer_class = TypeUserSerializer
    permission_classes = [permissions.IsAuthenticated]

# بيانات الحسابات البنكيه
class BankAcountViewSet(viewsets.ModelViewSet):
    queryset = BankAcount.objects.all()
    serializer_class = BankAcountSerializer
    permission_classes = [permissions.IsAuthenticated]


# بيانات صوره المستخدم
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

# بيانات أنواع الخدمات 
class TypeSerViewSet(viewsets.ModelViewSet):
    queryset = TypeSer.objects.all()
    serializer_class = TypeSerSerializer
    permission_classes = [permissions.IsAuthenticated]

# بيانات الخدمات 
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]


# بيانات حالات العقد 
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticated]

# بيانات العقد 
class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated]


# بيانات التقيمات 
class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    permission_classes = [permissions.IsAuthenticated]


# بيانات أنواع الشكاوي 
class TypeComViewSet(viewsets.ModelViewSet):
    queryset = TypeCom.objects.all()
    serializer_class = TypeComSerializer
    permission_classes = [permissions.IsAuthenticated]


# بيانات الشكاوي 
class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    permission_classes = [permissions.IsAuthenticated]


# بيانات أنواع الاشعارات 
class TeskViewSet(viewsets.ModelViewSet):
    queryset = Tesk.objects.all()
    serializer_class = TeskSerializer
    permission_classes = [permissions.IsAuthenticated]


# بيانات الاشعارات 
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]


# بيانات الاسئله الشائعة 
class HelpViewSet(viewsets.ModelViewSet):
    queryset = Help.objects.all()
    serializer_class = HelpSerializer
    permission_classes = [permissions.IsAuthenticated]
