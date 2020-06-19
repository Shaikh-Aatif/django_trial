from rest_framework import serializers
from . import models

class CredentialSerializer(serializers.ModelSerializer):
    """A serializer for our Credenetials objects"""

    class Meta:
        model = models.Credentials
        fields = ('id','username' ,'Password')
        

    