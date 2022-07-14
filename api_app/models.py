from ast import mod
from django.db import models
from datetime import date
# Create your models here.

# جدول أنواع المستخدمين
class TypeUser(models.Model):
    typeuser_id = models.BigAutoField(primary_key=True)
    typeuser_title = models.CharField(max_length=50)

# جدول المستخدمين
class WstUser(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    user_pass = models.CharField(max_length=30)
    validate = models.BooleanField()
    typeuser_id = models.ForeignKey(TypeUser, on_delete=models.CASCADE)

# جدول حسابات المستخدمين
class BankAcount(models.Model):
    bank_id = models.BigAutoField(primary_key=True)
    bank_name = models.CharField(max_length=100)
    bank_acount_number = models.IntegerField()
    acount_iban = models.IntegerField()
    user_id = models.ForeignKey(WstUser, on_delete=models.CASCADE)

# جدول صور المستخدمين
class Image(models.Model):
    img_id = models.BigAutoField(primary_key=True)
    img_link = models.TextField()
    user_id = models.ForeignKey(WstUser, on_delete=models.CASCADE)

# جدول أنواع الخدمات 
class TypeSer(models.Model):
    typeser_id = models.BigAutoField(primary_key=True)
    typeser_title = models.CharField(max_length=70)

# جدول الخدمات 
class Service(models.Model):
    serv_id = models.BigAutoField( primary_key=True)
    serv_name = models.CharField(max_length=70)
    serv_details = models.TextField()
    serv_price = models.IntegerField()
    serv_created_date = models.DateField(auto_now_add=True)
    serv_status = models.BooleanField()
    typeser_id = models.ForeignKey(TypeSer, on_delete=models.CASCADE)
    user_id = models.ForeignKey(WstUser, on_delete=models.CASCADE)

# جدول حالات العقد
class Status(models.Model):
    status_id = models.BigAutoField(primary_key=True)
    status_title = models.CharField(max_length=30)

# جدول العقود 
class Contract(models.Model):
    con_id = models.BigAutoField(primary_key=True)
    con_title = models.CharField(max_length=70)
    con_details = models.TextField()
    con_created_date = models.DateField(auto_created=True,)
    con_price = models.IntegerField()
    con_attachements = models.TextField()
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
    user_id = models.ForeignKey(WstUser, on_delete=models.CASCADE)
    serv_id = models.ForeignKey(Service, on_delete=models.CASCADE)

# جدول التقيمات
class Evaluation(models.Model):
    eval_id = models.BigAutoField(primary_key=True)
    eval_star_number = models.IntegerField()
    eval_comment = models.TextField()
    eval_created_date = models.DateField(auto_now_add=True)
    user_id = models.ForeignKey(WstUser, on_delete=models.CASCADE)
    serv_id = models.ForeignKey(Service, on_delete=models.CASCADE)

# جدول نوع الشكوي
class TypeCom(models.Model):
    typecom_id = models.BigAutoField(primary_key=True)
    typecom_title = models.CharField(max_length=70)

# جدول الشكاوي
class Complaint(models.Model):
    com_id = models.BigAutoField(primary_key=True)
    com_title = models.CharField(max_length=70)
    com_details = models.TextField()
    com_image = models.TextField()
    com_created_date = models.DateField(auto_now_add=True)
    typecom_id = models.ForeignKey(TypeCom, on_delete=models.CASCADE)
    user_id = models.ForeignKey(WstUser, on_delete=models.CASCADE)

#  جدول نوع الاشعار
class Tesk(models.Model):
    tsk_id = models.BigAutoField(primary_key=True)
    tsk_title = models.CharField(max_length=70)

# جدول الاشعارات 
class Notification(models.Model):
    not_id = models.BigAutoField(primary_key=True)
    not_title = models.CharField(max_length=70)
    not_content = models.TextField()
    not_created_date = models.DateField(auto_now_add=True)
    tsk_id = models.ForeignKey(Tesk, on_delete=models.CASCADE)

# جدول الاسئلة الشائعه
class Help(models.Model):
    help_id = models.BigAutoField(primary_key=True)
    help_question = models.TextField()
    help_answer = models.TextField()



# جدول الرصيد
class Balance(models.Model):
    bal_id = models.BigAutoField(primary_key=True)
    bal_amount = models.IntegerField()
    user_id = models.ForeignKey(WstUser, on_delete=models.CASCADE)


class TypePro(models.Model):
    typepro_id = models.BigAutoField(primary_key=True)
    type_title = models.CharField(max_length=70)

# جدول العمليات علي الرصيد 
class Proces(models.Model):
    bal_id = models.BigAutoField(primary_key=True)
    pro_created_date = models.DateField(auto_now_add=True)
    pro_amount = models.IntegerField()
    bal_id = models.ForeignKey(Balance, on_delete=models.CASCADE)
    bal_id = models.ForeignKey(TypePro, on_delete=models.CASCADE)
    

# https://docs.djangoproject.com/en/4.0/topics/db/queries/
# https://docs.djangoproject.com/en/4.0/topics/db/models/