from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tbl_categoria'

    def __str__(self):
        return self.nombre

class Area(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tbl_area'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.RESTRICT)
    area = models.ForeignKey(Area,on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=255,null=True)
    descripcion = models.TextField(null=True)
    detalle = models.TextField(null=True)
    precio = models.DecimalField(max_digits=6,decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now=True)
    size_disponible = models.CharField(max_length=100)
    material = models.CharField(max_length=150)
    tecnologia_fabricada= models.CharField(max_length=255)
    color_disponible=models.CharField(max_length=255)
    musical= models.CharField(max_length=200)
    luces_interno=models.CharField(max_length=200)
    personalizable=models.CharField(max_length=255)
    popularidad = models.DecimalField(max_digits=4,decimal_places=1)
    sku = models.CharField(max_length=10,null=True,unique=True)
    
    class Meta:
        db_table = 'tbl_producto'

    def __str__(self):
        return self.nombre

@receiver(post_save,sender=Producto)
def generar_sku(sender,instance,created,**kwargs):
    if created:
        categoria_cod = instance.categoria.nombre[:2].upper()
        correlativo = str(Producto.objects.count()).zfill(3)
        instance.sku = f'{categoria_cod}{correlativo}'
        instance.save()


class ProductoImagen(models.Model):
    producto = models.ForeignKey(Producto,on_delete=models.RESTRICT)
    imagen = models.ImageField(upload_to='galeria',blank=True)
    orden = models.IntegerField(default=1)
    fecha_registro = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tbl_producto_imagen'
        verbose_name_plural = 'Imagenes del Producto'
        verbose_name = 'Imagen del Producto'

    def __str__(self):
        return str(self.imagen)

### modelos para usuarios y cliente ###

from django.contrib.auth.models import User

class Cliente(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=255)
    dni= models.CharField(max_length=8)
    sexo = models.CharField(max_length=1)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(null=True)
    direccion = models.TextField()

    class Meta:
        db_table = 'tbl_cliente'

    def __str__(self):
        return self.nombre


##### pedidos #####

class Pedido(models.Model):

    ESTADO_CHOICES = (
        ('0','Solicitado'),
        ('1','Pagado')
    )

    cliente = models.ForeignKey(Cliente,on_delete=models.RESTRICT)
    fecha_registro = models.DateTimeField(auto_now=True)
    nro_pedido = models.CharField(max_length=20,null=True)
    monto_total = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    estado = models.CharField(max_length=1,default='0',choices=ESTADO_CHOICES)

    class Meta:
        db_table = 'tbl_pedido'

    def __str__(self):
        return self.nro_pedido

class PedidoDetalle(models.Model):
    pedido = models.ForeignKey(Pedido,on_delete=models.RESTRICT)
    producto = models.ForeignKey(Producto,on_delete=models.RESTRICT)
    cantidad = models.IntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        db_table = 'tbl_pedido_detalle'

    def __str__(self):
        return self.producto.nombre