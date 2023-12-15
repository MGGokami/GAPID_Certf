from django.db import models
from apps.api_base.models import ProjectMember, Program, Project
# Create your models here.

CRITERIA_CHOICES = [
    # Agrega aquí más opciones si las necesitas
    ('CO', 'Cumplimiento de los Objetivos'),
    ('CC', 'Cumplimiento del Cronograma'),
    ('EEP', 'Estado de Ejecución del Presupuesto'),
    ('CDG', 'Capacidad de Dirección y Gestión'),
    ('P', 'Participación activa en las sesiones de trabajo'),
    ('E', 'Evaluaciones'),
    ('CC', 'Cumplimiento en tiempo y calidad de las tareas asignadas por el trabajo realizado'),
    ('NC', 'Nivel de complejidad, aporte creativo, novedad y efectos en los resultados obtenidos'),   
   ]
class CertEvaluationCriteria(models.Model):
    criteria_id = models.AutoField(primary_key=True)
    criteria = models.CharField(max_length=3, choices=CRITERIA_CHOICES,help_text='Criterio de evaluacion')

    class Meta:
        managed = False

class CertCertificationPeriod(models.Model):
    period_id = models.BigAutoField(primary_key=True)
    start_date = models.DateField(blank=False, null=False,help_text='Fecha de inicio del Periodo')
    end_date = models.DateField(blank=False, null=False, help_text='Fecha final del Periodo')

    class Meta:
        managed = False

class CertCriteriaEvaluationInPeriod(models.Model):
    person_id = models.OneToOneField(ProjectMember, models.DO_NOTHING, db_column='person_id', primary_key=True)  
    period_id = models.ForeignKey(CertCertificationPeriod, models.DO_NOTHING, db_column='period_id')
    criteria_id = models.ForeignKey(CertEvaluationCriteria, models.DO_NOTHING, db_column='criteria_id')
    evaluation = models.IntegerField(null=False, help_text='Evaluacion por Periodo')

    class Meta:
        managed = False
        unique_together = (('person_id', 'period_id', 'criteria_id'),)
 
class CertProgramCertificationPeriod(models.Model):
    period_id = models.OneToOneField(CertCertificationPeriod, models.DO_NOTHING, db_column='period_id', primary_key=True)
    program_id = models.ForeignKey(Program, models.DO_NOTHING, db_column='program_id')

    class Meta:
        managed = False
        unique_together = (('period_id', 'program_id'),)

class CertProjectCertificationPeriod(models.Model):
    period_id = models.OneToOneField(CertCertificationPeriod, models.DO_NOTHING, db_column='period_id', primary_key=True)  
    project_id = models.ForeignKey(Project, models.DO_NOTHING, db_column='project_id')

    class Meta:
        managed = False
        unique_together = (('period_id', 'project_id'),)
