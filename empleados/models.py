from django.db import models
from django.forms import model_to_dict


from bases.models import ClaseModelo
# Create your models here.

class Nacionalidad(ClaseModelo):
    nacionalidad = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nacionalidad

    def save(self):
        self.nacionalidad = self.nacionalidad.upper()
        super(Nacionalidad, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item
    
    class Meta:
        verbose_name_plural = "Nacionalidades"
        ordering = ['id']

class Sexo(ClaseModelo):
    tiposexo=models.CharField(max_length=50)

    def __str__(self):
        return self.tiposexo

    def save(self):
        self.tiposexo = self.tiposexo.upper()
        super(Sexo, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name_plural = "Sexos"
        ordering = ['id']

class EstadoCivil(ClaseModelo):
    ecivil = models.CharField(max_length=50)

    def __str__(self):
        return self.ecivil

    def save(self):
        self.ecivil = self.ecivil.upper()
        super(EstadoCivil, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name_plural = 'EstadosCiviles'
        ordering = ['id']

class TipoSalario(ClaseModelo):
    sircunscripcion = models.IntegerField(default=0)
    salario = models.FloatField(default=0)

    # def __str__(self):
    #     return self.sircunscripcion

    def save(self):
        self.sircunscripcion = self.sircunscripcion
        super(TipoSalario, self).save()
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name_plural = 'TiposSalarios'
        ordering = ['id']

class Gerencia(ClaseModelo):
    gerencia = models.CharField(max_length=50)

    def __str__(self):
        return self.gerencia

    def save(self):
        self.gerencia = self.gerencia.upper()
        super(Gerencia, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name_plural = 'Gerencias'
        ordering = ['id']

class Departamento(ClaseModelo):
    departamento = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.departamento

    def save(self):
        self.departamento = self.departamento.upper()
        super(Departamento, self).save()

    def toJSON(self):
        item =  model_to_dict(self)
        return item

    class Meta:
        verbose_name_plural = "Departamentos"
        ordering = ['id']

class Puesto(ClaseModelo):
    puesto = models.CharField(max_length=50)

    def __str__(self):
        return self.puesto

    def save(self):
        self.puesto = self.puesto.upper()
        super(Puesto, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name_plural = 'Puestos'
        ordering = ['id']

class Sucursal(ClaseModelo):
    sucursal = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.sucursal

    def save(self):
        self.sucursal = self.sucursal.upper()
        super(Sucursal, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name_plural = 'Sucursales'
        ordering = ['id']

class Empleado(ClaseModelo):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)
    zona = models.IntegerField(default=0)
    departamento = models.CharField(max_length=100)
    muni = models.CharField(max_length=100)
    tel = models.IntegerField(default=0)
    cel = models.IntegerField(default=0)
    fechanace = models.DateField(auto_now=False, auto_now_add=False)
    lnace = models.CharField(max_length=100)
    dpi = models.CharField(max_length=13)
    nit = models.IntegerField(default=0, unique=True)
    email = models.EmailField(max_length=254)
    ecivil = models.ForeignKey("EstadoCivil", on_delete=models.CASCADE)
    hijo = models.CharField(max_length=2)
    nacionalidad = models.ForeignKey("Nacionalidad", on_delete=models.CASCADE)
    sexo = models.ForeignKey("Sexo", on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)

    def __str__(self):
        return self.dpi

    def save(self):
        self.dpi = self.dpi
        super(Empleado, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name_plural = 'Empleados'
        ordering = ['id']

class DatosNomina(ClaseModelo):
    dpi = models.ForeignKey("Empleado", on_delete=models.CASCADE)
    cuenta = models.IntegerField(default=0, unique=True)
    licencia = models.CharField(max_length=50) 
    fechaingreso = models.DateField(auto_now=False, auto_now_add=False)
    profesion = models.CharField(max_length=50)
    salario = models.ForeignKey("TipoSalario", on_delete=models.CASCADE)
    gerencia = models.ForeignKey("Gerencia", on_delete=models.CASCADE)
    departamento = models.ForeignKey("Departamento", on_delete=models.CASCADE)
    puesto = models.ForeignKey("Puesto", on_delete=models.CASCADE)
    agencia = models.ForeignKey("Sucursal", on_delete=models.CASCADE)

    def __str__(self):
        return self.cuenta

    def save(self):
        self.cuenta = self.cuenta
        super(DatosNomina, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name_plural = 'Datos Nominas'
        ordering= ['id']

class Papeleria(ClaseModelo):
    dpi = models.ForeignKey("Empleado", on_delete=models.CASCADE)
    curriculum = models.BooleanField(default=False)
    fotografia = models.BooleanField(default=False)
    diploma = models.BooleanField(default=False)
    constancianit = models.BooleanField(default=False)
    apenales = models.BooleanField(default=False)
    apoliciacos = models.BooleanField(default=False)
    fdpi = models.BooleanField(default=False)
    ornato = models.BooleanField(default=False)
    observaciones = models.TextField()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name_plural = 'Papelerias'
        ordering = ['id']
