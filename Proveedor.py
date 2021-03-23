import re

class Proveedor:
    codigo=""
    nombre=""
    RUC=""
    telefono=""
    direccion=""

    def __init__(self,c,n,r,t,d):
        self.codigo="PRO-00"+str(c+1)
        self.nombre=n
        self.RUC=r
        self.telefono=t
        self.direccion=d

    def get_codigo(self):
        return self.codigo

    def get_nombre(self):
        return self.nombre

    def modificar_proveedor(self,d):
        if d==1 or d==5:
            self.nombre=input("Cambiar nombre de proveedor: ")
        elif d==2 or d==5:
            self.RUC=input("Cambiar RUC de proveedor:")
        elif d==3 or d==5:
            self.telefono=input("Actualizar telefono: ")
        elif d==4 or d==5:
            self.direccion=input("Actualizar direccion: ")

    def mostrar_proveedor(self):
        print('{:<16}'.format(self.codigo)+
            '{:<25}'.format(self.nombre)+
            '{:<25}'.format(self.RUC)+
            '{:<25}'.format(self.telefono)+
            '{:<25}'.format(self.direccion))