from rest_framework import serializers
from .models import  Pupil, JWTPayloadTrack




class PupilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupil
        fields = '__all__'

class JWTPayloadTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = JWTPayloadTrack
        fields = '__all__'

