from django.db import models
from django.contrib.auth import get_user_model 
User = get_user_model()

class Entity(models.Model):
    entity_id = models.AutoField(primary_key=True)
    entity_name = models.CharField(max_length=255)
    reup_code = models.CharField(max_length=255)
    nit_code = models.CharField(max_length=255, blank=True, null=True)
    legal_domicile = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=255)
    web_site = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField()

    class Meta:
        managed = False


class Program(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    code = models.CharField(unique=True, max_length=50)
    abbreviated_name = models.CharField(max_length=100)
    management_entity_id = models.ForeignKey(Entity, models.DO_NOTHING, db_column='management_entity_id')
    leading_entity_id = models.ForeignKey(Entity, models.DO_NOTHING, db_column='leading_entity_id',
                                          related_name='programas_id_entidad_dirige_set')

    class Meta:
        managed = False


class CITMAProgram(models.Model):
    program_id = models.OneToOneField(Program, models.DO_NOTHING, db_column='program_id', primary_key=True)
    budget = models.FloatField()
    projects_amount = models.IntegerField()
    years_of_execution = models.IntegerField()
    program_level = models.CharField(max_length=255)
    is_active = models.BooleanField()

    class Meta:
        managed = False


class PCTProgram(models.Model):
    program_id = models.OneToOneField(Program, models.DO_NOTHING, db_column='program_id', primary_key=True)
    name = models.IntegerField(blank=True, null=True)
    legal_domicile = models.IntegerField(blank=True, null=True)
    email = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False


class Project(models.Model):
    project_id = models.BigAutoField(primary_key=True)
    program_id = models.ForeignKey(Program, models.DO_NOTHING, db_column='program_id')
    code = models.CharField(unique=True, max_length=100)
    title = models.CharField(max_length=200)
    abbreviated_title = models.CharField(max_length=100)
    url_logo = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500)
    is_active = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()
    director_name = models.CharField(max_length=200)

    class Meta:
        managed = False


class CITMAProject(models.Model):
    project_id = models.OneToOneField(Project, models.DO_NOTHING, db_column='project_id', primary_key=True)
    project_level = models.CharField(max_length=255)

    class Meta:
        managed = False


class ProyectosPct(models.Model):
    project_id = models.OneToOneField(Project, models.DO_NOTHING, db_column='project_id', primary_key=True)
    contract_number = models.CharField(max_length=500)
    supplement_code = models.CharField(max_length=500)
    classification = models.CharField(max_length=255)

    class Meta:
        managed = False


class CITMAMemberRole(models.Model):
    citma_role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255)

    class Meta:
        managed = False


class PCTMemberRole(models.Model):
    pct_role_id = models.BigAutoField(primary_key=True)
    role_name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False



class RoleLevelParticipantPCT(models.Model):
    level_id = models.BigAutoField(primary_key=True)
    level_name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False




class PCTProjectPaymentRate(models.Model):
    project_id = models.OneToOneField(ProyectosPct, models.DO_NOTHING, db_column='project_id',
                                       primary_key=True)  # The composite primary key (project_id, role_id, level_id) found, that is not supported. The first column is selected.
    role_id = models.ForeignKey(PCTMemberRole, models.DO_NOTHING, db_column='role_id')
    level_id = models.ForeignKey(RoleLevelParticipantPCT, models.DO_NOTHING, db_column='level_id')
    rate = models.DecimalField(max_digits=19, decimal_places=0)

    class Meta:
        managed = False
        unique_together = (('project_id', 'role_id', 'level_id'), ('role_id', 'level_id'),)


class PCTProgramPhone(models.Model):
    program_id = models.OneToOneField(PCTProgram, models.DO_NOTHING, db_column='program_id',
                                       primary_key=True)  # The composite primary key (program_id, phone) found, that is not supported. The first column is selected.
    phone = models.CharField(max_length=255)

    class Meta:
        managed = False
        unique_together = (('program_id', 'phone'),)


class ProjectParticipationType(models.Model):
    participation_type_id = models.AutoField(primary_key=True)
    participation_type = models.IntegerField()

    class Meta:
        managed = False



class EntityInProject(models.Model):
    entity_id = models.OneToOneField(Entity, models.DO_NOTHING, db_column='entity_id',
                                      primary_key=True)  # The composite primary key (entity_id, project_id, participation_type_id) found, that is not supported. The first column is selected.
    project_id = models.ForeignKey(Project, models.DO_NOTHING, db_column='project_id')
    participation_type_id = models.ForeignKey('ProjectParticipationType', models.DO_NOTHING,
                                              db_column='participation_type_id')

    class Meta:
        managed = False
        unique_together = (('entity_id', 'project_id', 'participation_type_id'),)



class Person(models.Model):
    person_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    identity_card = models.CharField(unique=True, max_length=11)
    bank_account = models.CharField(unique=True, max_length=16)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    scientific_category = models.CharField(max_length=255)
    educational_category = models.CharField(max_length=255)
    scientific_degree = models.CharField(max_length=255)
    profile_pic_url = models.CharField(max_length=255, blank=True, null=True)
    wage = models.FloatField()

    class Meta:
        managed = False


class ProjectMember(models.Model):
    person_id = models.OneToOneField(Person, models.DO_NOTHING, db_column='person_id', primary_key=True)
    project_id = models.ForeignKey(Project, models.DO_NOTHING, db_column='project_id')

    class Meta:
        managed = False


class PCTProjectMember(models.Model):
    member_id = models.OneToOneField(ProjectMember, models.DO_NOTHING,
                                           db_column='member_id', primary_key=True)

    class Meta:
        managed = False


class PCTProjectMemberRole(models.Model):
    member_id = models.OneToOneField(PCTProjectMember, models.DO_NOTHING, db_column='member_id',
                                           primary_key=True)  # The composite primary key (member_id, role_id) found, that is not supported. The first column is selected.
    role_id = models.ForeignKey(PCTMemberRole, models.DO_NOTHING, db_column='role_id')

    class Meta:
        managed = False
        unique_together = (('member_id', 'role_id'),)


class NaturalPerson(models.Model):
    natural_person_id = models.AutoField(primary_key=True)
    name = models.IntegerField()
    last_name = models.IntegerField()
    nationality = models.CharField(max_length=255)
    personal_address = models.CharField(max_length=255)
    identity_card = models.CharField(unique=True, max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    passport = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False



class ProgramManagementTeamMember(models.Model):
    person_id = models.OneToOneField(Person, models.DO_NOTHING, db_column='person_id',
                                      primary_key=True)  # The composite primary key (person_id, user_id, program_id) found, that is not supported. The first column is selected.
    user_id = models.ForeignKey(User, models.DO_NOTHING, db_column='user_id')
    program_id = models.ForeignKey('Program', models.DO_NOTHING, db_column='program_id')
    position = models.CharField(max_length=255)

    class Meta:
        managed = False
        unique_together = (('person_id', 'user_id', 'program_id'),)


class NaturalPersonInProject(models.Model):
    project_id = models.OneToOneField(Project, models.DO_NOTHING, db_column='project_id',
                                       primary_key=True)  # The composite primary key (project_id, natural_person_id, participation_type) found, that is not supported. The first column is selected.
    natural_person_id = models.ForeignKey(NaturalPerson, models.DO_NOTHING, db_column='natural_person_id')
    participation_type = models.ForeignKey(ProjectParticipationType, models.DO_NOTHING,
                                           db_column='participation_type')

    class Meta:
        managed = False
        unique_together = (('project_id', 'natural_person_id', 'participation_type'),)




class CITMAProjectMember(models.Model):
    person_id = models.OneToOneField(ProjectMember, models.DO_NOTHING, db_column='person_id',
                                      primary_key=True)
    entity_id = models.ForeignKey(Entity, models.DO_NOTHING, db_column='entity_id')
    position_id = models.ForeignKey(CITMAMemberRole, models.DO_NOTHING, db_column='position_id')
    mce = models.IntegerField()
    months_in_project = models.IntegerField()
    participation_percent = models.IntegerField()

    class Meta:
        managed = False
