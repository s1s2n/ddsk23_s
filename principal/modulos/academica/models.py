from django.db import models

# Create your models here.
class carrera(models.model):
    codigo= models.CharField(max_length=3,primary_key=True)
    nombre= models.CharField(max_length=50)
    duracion= models.positivesmallintegerfield(default=5)

class estudiante(models.model):
    dni= models.CharField(max_length=8, primary_key=True)
    apellidopaterno=models.CharField(max_length=35)
    apellidomaterno=models.CharField(max_length=35)
    nombres=models.CharField(max_length=35)
    fechanacimiento=models.DateField()
    sexos=[
        ('f','femenino')
        ('m', 'masculino')
    ]
    sexo=models.CharField(max_length=1,choices=sexos,default='f')
    carrera=models.ForeignKey(carrera, null=False,blank=False, on_delete=models.cascada)
    vigencia= models.Booleanfield(default=True)

    def nombrecompleto(self):
        txt="{0} {1},{2}"
        return txt.format(self.apellidopaterno,self.apellidomaterno,self.nombres)

class curso(models.model):
    codigo=models.CharField(max_length=6,primary_key=True)
    nombre=models.CharField(max_length=30)
    creditos=models.positivesmallintegerfield()
    docente=models.CharField(max_length=100)

class matricula(models.model):
    id=models.AutoField(primary_key=True)
    estudiante=models.ForeignKey(estudiante,null=False,blank=False,on_delete=models.cascade)
    curso=models.ForeignKey(curso,null=False,blank=False,on_delete=models.cascada)
    fechamatricula=models.datetimefield(auto_now_add=True)

