from django.contrib import admin

# Register your models here.
from .models import(
    Categoria,Area,Producto,ProductoImagen,Cliente,Pedido,PedidoDetalle
)

admin.site.register(Categoria)
admin.site.register(Area)
#admin.site.register(Producto)
#admin.site.register(Cliente)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('sku','nombre','categoria','area','precio','size_disponible')
    list_filter = ('categoria','area')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id','usuario','nombre','dni','telefono','fecha_nacimiento','direccion')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente_id','id','fecha_registro','nro_pedido','monto_total','estado')

@admin.register(PedidoDetalle)
class PedidoDetalleAdmin(admin.ModelAdmin):
    list_display = ('pedido','producto','cantidad','subtotal','pedido_id')

from django.utils.html import format_html

@admin.register(ProductoImagen)
class ProductoImagenAdmin(admin.ModelAdmin):

    def imagen_html(self,obj):
        return format_html('<img src="{}" width=150px />'.format(obj.imagen.url))

    imagen_html.short_description = 'Imagen'

    list_display = ('orden','producto', 'imagen_html')
    search_fields = ['producto__nombre']


