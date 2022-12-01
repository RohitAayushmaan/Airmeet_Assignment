from rest_framework import serializers
from .models import student

class studentSerializer(serializers.ModelSerializer):

    class Meta:
        model =student
        # fields=('firstName','lastName')
        fields='__all__'

