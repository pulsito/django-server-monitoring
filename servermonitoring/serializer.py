from rest_framework import serializers
from .models import ServerMonitoring


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerMonitoring
        fields = "__all__"


class ServerLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerMonitoring
        fields = ('server_name', 'location')