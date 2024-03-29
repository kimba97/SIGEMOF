from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Persona(models.Model):
	nombrePersona=models.CharField(max_length=200)
	dui=models.CharField(max_length=10, unique=True)
	direccion=models.CharField(max_length=250)
	telefono=models.CharField(max_length=250)
	fechaNac=models.DateField()
	edad=models.IntegerField()

	class Meta:
		verbose_name='Persona'
		verbose_name_plural='Personas'
	def __str__(self):
		return '%s' %(self.nombrePersona)

class Secretaria(Persona):
	isss=models.CharField(max_length=12, unique=True)
	afp=models.CharField(max_length=9, unique=True)
	class Meta:
		verbose_name='Secretaria'
		verbose_name_plural='Secretarias'
	def __str__(self):
		return '%s' %(self.nombrePersona)

class Doctora(Secretaria):
	jvpm=models.CharField(max_length=10, unique=True)
	class Meta:
		verbose_name='Doctora'
		verbose_name_plural='Doctoras'
	def __str__(self):
		return '%s' %(self.nombrePersona)

class Paciente(Persona):
	remitente=models.CharField(max_length=50)
	class Meta:
		verbose_name='Paciente'
		verbose_name_plural='Pacientes'
	def __str__(self):
		return '%s' %(self.nombrePersona)

class Expediente(models.Model):
	NumExp=models.CharField(max_length=50, unique=True)
	paciente=models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True, blank=True)
	class Meta:
		verbose_name='Expediente'
		verbose_name_plural='Expedientes'
	def __str__(self):
		return '%s' %(self.paciente.nombrePersona)

class Consulta(models.Model):
	fecha=models.DateField()
	diag=models.CharField(max_length=500)
	expedientePac=models.ForeignKey(Expediente, on_delete=models.CASCADE, null=True, blank=True)
	class Meta:
		verbose_name='Consulta'
		verbose_name_plural='Consultas'
	def __str__(self):
		return '%s' %(self.id)








