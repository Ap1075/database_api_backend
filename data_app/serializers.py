from rest_framework import serializers
from .models import *


class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model=ImagePathDb
        fields = "__all__"
