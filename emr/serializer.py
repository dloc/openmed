from rest_framework import serializers
from emr.models import Doctor, Patient, Vitals
from django.contrib.auth.models import User, Group


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name']


class VitalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vitals
        fields = ['id', 'created', 'temperature', 'pulse', 'patient']


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'dob', 'doctor', 'notes']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
