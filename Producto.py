from Proveedor import Proveedor

class Producto:
    codigo=""
    nombre=""
    cantidad=0
    categoria=""
    precio_u=0.00
    Proveedor=[]

    def __init__(self,c,n,cn,ct,pu,pr):
        self.codigo="P-00"+str(c+1)
        self.nombre=n
        self.cantidad=cn
        self.categoria=ct
        self.precio_u=pu
        self.Proveedor=pr

    def set_proveedor(self,pr):
        self.Proveedor=pr

    def get_codigo(self):
        return self.codigo

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_preciounitario(self):
        return self.precio_u

    def validar_registro(self,ct):
        self.cantidad=self.cantidad-ct

    def modificar_producto(self,d):
        if d==1 or d==6:
            self.nombre=input("Cambiar nombre de producto: ")
        elif d==2 or d==6:
            self.cantidad=input("Actualizar cantidad de producto: ")
        elif d==3 or d==6:
            self.categoria=input("Actualizar categoria de producto: ")
        elif d==4 or d==6:
            self.precio_u=input("Actualizar precio unitario de producto: ")

    def mostrar_producto(self):
        print('{:<16}'.format(self.codigo)+
            '{:<25}'.format(self.nombre)+
            '{:<25}'.format(self.cantidad)+
            '{:<25}'.format(self.categoria)+
            '{:<25}'.format(self.precio_u)+
            '{:<25}'.format(self.Proveedor.get_nombre()))
