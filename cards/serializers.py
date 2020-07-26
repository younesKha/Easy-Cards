from rest_framework import  serializers
from .models import c_groups


from django import  forms

class group_ser(serializers.ModelSerializer):
    class Meta:
        model=c_groups
        fields=('id','name')