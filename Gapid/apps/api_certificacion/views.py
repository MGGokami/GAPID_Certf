from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, mixins, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from apps.api_base.models import *
from .models import *
from .serializers import *
# Create your views here.

class Periodo(viewsets.ModelViewSet):
    queryset = CertCertificationPeriod.objects.all()
    serializer_class = CertCertificationPeriodSerializer
