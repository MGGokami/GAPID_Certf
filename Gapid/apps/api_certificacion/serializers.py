from rest_framework import serializers
from .models import CertCertificationPeriod,CertCriteriaEvaluationInPeriod

class CertCertificationPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertCertificationPeriod
        fields = ['period_id', 'start_date', 'end_date']
    
    def validate(self, data):
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("La fecha de inicio no puede ser mayor que la fecha final")
        else:
            return data
        
class CertCriteriaEvaluationInPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertCriteriaEvaluationInPeriod
        fields = ['person_id', 'period_id', 'criteria_id', 'evaluation']       