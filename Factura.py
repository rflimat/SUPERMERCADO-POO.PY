from datetime import date

class Factura:
    codigo=""
    cliente=[]
    cantidad_p=[]
    productos=[]
    fecha=date.today()
    total=0.00

    def __init__(self,c,cliente):
        self.codigo="F-00"+str(c+1)
        self.cliente=cliente

    def get_codigo(self):
        return self.codigo

    def get_codigoc(self):
        cc=self.cliente.get_codigo()
        return cc

    def set_productos(self,producto,cantidad):
        self.productos.append(producto)
        self.cantidad_p.append(cantidad)
        producto.validar_registro(cantidad)
        self.total=self.total+producto.get_preciounitario()

    def ver_factura(self):
        print("\t\tSUPERMERCADO XD\n")
        print("Codigo de factura: "+self.codigo)
        print("Nombre del cliente: "+self.cliente.get_nombres())
        print("Fecha: "+str(self.fecha))
        print('{:<16}'.format("Codigo")+
            '{:<25}'.format("Nombre")+
            '{:<25}'.format("Cantidad")+
            '{:<25}'.format("Precio Unitario")+
            '{:<25}'.format("Subtotal"))
        x=0
        for producto in self.productos:
            print('{:<16}'.format(producto.get_codigo())+
            '{:<25}'.format(producto.get_nombre())+
            '{:<25}'.format(self.cantidad_p[x])+
            '{:<25}'.format(producto.get_preciounitario())+
            '{:<25}'.format(self.cantidad_p[x]*producto.get_preciounitario()))  
            x=x+1      
        print("\nTotal: "+str(self.total))

    def lista_facturas(self):
        print('{:<16}'.format(self.codigo)+
            '{:<25}'.format(self.cliente.get_nombres())+
            '{:<25}'.format(str(self.fecha))+
            '{:<25}'.format(str(self.total)))