from dataclasses  import field
from pyexpat import model
from rest_framework import serializers
from api_app.models import *

# بيانات المستخدمين
class WstUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WstUser
        fields = '__all__'

#  بيانات أنواع المستخدمين
class TypeUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeUser
        fields = '__all__'
        # ['typeuser_id', 'typeuser_title']

# بيانات الحسابات البنكيه
class BankAcountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BankAcount
        fields = '__all__'

# بيانات صور المستخدمين
class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

# بيانات أنواع الخدمات 
class TypeSerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeSer
        fields = '__all__'

# بيانات الخدمات 
class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

# بيانات حالات العقد 
class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

# بيانات العقد 
class ContractSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

# بيانات التقيمات 
class EvaluationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'

# بيانات أنواع الشكاوي 
class TypeComSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeCom
        fields = '__all__'
            

# بيانات الشكاوي 
class ComplaintSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'


# بيانات أنواع الاشعارات 
class TeskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tesk
        fields = '__all__'


# بيانات الاشعارات 
class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


# بيانات الاسئله الشائعة 
class HelpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Help
        fields = '__all__'
