from rest_framework import serializers

from . import models

class UserOperationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Todo
        fields = ('id','title','text','created_at','finish')
