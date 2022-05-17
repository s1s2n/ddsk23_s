from django.contrib import admin
from .models import carrera
from .models import estudiante
from .models import curso
from .models import matricula

# Register your models here.fsddf
admin.site.Register(carrera)
admin.site.Register(estudiante)
admin.site.Register(curso)
admin.site.Register(matricula)
