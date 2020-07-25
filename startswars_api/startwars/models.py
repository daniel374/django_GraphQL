from django.db import models

# Create your models here.


class Peliculas(models.Model):
    idpl = models.AutoField(db_column='idPl', primary_key=True)  # Field name made lowercase.
    nombrepl = models.CharField(db_column='nombrePl', max_length=60)  # Field name made lowercase.
    productorespl = models.CharField(db_column='productoresPl', max_length=500)  # Field name made lowercase.
    detallePl = models.CharField(db_column='detallePl', max_length=500)  # Field name made lowercase.
    directorpl = models.CharField(db_column='directorPl', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'peliculas'


class Personajes(models.Model):
    idpj = models.AutoField(db_column='idPj', primary_key=True)  # Field name made lowercase.
    nombrepj = models.CharField(db_column='nombrePj', max_length=45)  # Field name made lowercase.

    def __str__(self):
        return self.nombrepj
    class Meta:
        managed = False
        db_table = 'personajes'

class Planetas(models.Model):
    idPla = models.AutoField(db_column='idPla', primary_key=True)  # Field name made lowercase.
    nombrePla = models.CharField(db_column='nombrePla', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'planetas'

class Persopelis(models.Model):
    idpeli = models.OneToOneField(Peliculas, models.DO_NOTHING, db_column='idpeli', primary_key=True)
    idper = models.ForeignKey(Personajes, models.DO_NOTHING, db_column='idper')

    class Meta:
        managed = False
        db_table = 'persopelis'
        unique_together = (('idpeli', 'idper'),)

class Planetaspelis(models.Model):
    idpeli = models.OneToOneField(Peliculas, models.DO_NOTHING, db_column='idpeli', primary_key=True)
    idplaneta = models.ForeignKey(Planetas, models.DO_NOTHING, db_column='idplaneta')

    class Meta:
        managed = False
        db_table = 'planetaspelis'
        unique_together = (('idpeli', 'idplaneta'),)