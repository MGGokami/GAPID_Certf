from rest_framework import viewsets, permissions
from .models import Perido_Certificacion,Criterio_evaluacion,Cert_periodos_certificacion_proyectos,Cert_periodos_certificacion_programas,Cert_evaluacion_periodo_evaluacion
from .serializers import Perido_CertificacionSerializer

class Perido_CertificacionViewsets(viewsets.ModelViewSet):
    queryset = Perido_Certificacion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Perido_CertificacionSerializer

