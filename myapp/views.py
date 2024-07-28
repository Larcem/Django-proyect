from rest_framework import generics
from rest_framework import generics
from .models.Asistencia import Asistencia
from .models.Estudiante import Estudiante
from .models.FaltaAsistencia import FaltaAsistencia
from .models.FaltaPago import FaltaPago
from .models.Justificacion import Justificacion
from .models.Pago import Pago
from .models.servicio import servicio
from .models.University import University
from .serializers import AsistenciaSerializer, EstudianteSerializer, FaltaAsistenciaSerializer, FaltaPagoSerializer, JustificacionSerializer, PagoSerializer, ServicioSerializer, UniversitySerializer

from .serializers import AsistenciaSerializer, EstudianteSerializer, FaltaAsistenciaSerializer, FaltaPagoSerializer, JustificacionSerializer, PagoSerializer, ServicioSerializer, UniversitySerializer

# Vistas para el modelo Asistencia
class AsistenciaListCreate(generics.ListCreateAPIView):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer

class AsistenciaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer

# Vistas para el modelo Estudiante
class EstudianteListCreate(generics.ListCreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class EstudianteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

# Vistas para el modelo FaltaAsistencia
class FaltaAsistenciaListCreate(generics.ListCreateAPIView):
    queryset = FaltaAsistencia.objects.all()
    serializer_class = FaltaAsistenciaSerializer

class FaltaAsistenciaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FaltaAsistencia.objects.all()
    serializer_class = FaltaAsistenciaSerializer

# Vistas para el modelo FaltaPago
class FaltaPagoListCreate(generics.ListCreateAPIView):
    queryset = FaltaPago.objects.all()
    serializer_class = FaltaPagoSerializer

class FaltaPagoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FaltaPago.objects.all()
    serializer_class = FaltaPagoSerializer

# Vistas para el modelo Justificacion
class JustificacionListCreate(generics.ListCreateAPIView):
    queryset = Justificacion.objects.all()
    serializer_class = JustificacionSerializer

class JustificacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Justificacion.objects.all()
    serializer_class = JustificacionSerializer

# Vistas para el modelo Pago
class PagoListCreate(generics.ListCreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class PagoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

# Vistas para el modelo Servicio
class ServicioListCreate(generics.ListCreateAPIView):
    queryset = servicio.objects.all()
    serializer_class = ServicioSerializer

class ServicioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = servicio.objects.all()
    serializer_class = ServicioSerializer

# Vistas para el modelo University
class UniversityListCreate(generics.ListCreateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class UniversityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
