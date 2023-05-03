from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=50)
    lastname = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=50)

    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'address']