class Cliente:
    codigo=""
    nombres=""
    apellidos=""
    DNI=""
    RUC=""
    telefono=""

    def __init__(self,c,n,a,d,r,t):
        self.codigo="C-00"+str(c+1)
        self.nombres=n
        self.apellidos=a
        self.DNI=d
        self.RUC=r
        self.telefono=t

    def get_codigo(self):
        return self.codigo

    def get_nombres(self):
        return self.nombres+" "+self.apellidos

    def modificar_cliente(self,d):
        if d==1 or d==6:
            self.nombres=input("Cambiar nombres de cliente: ")
        elif d==2 or d==6:
            self.apellidos=input("Cambiar apellidos de cliente: ")
        elif d==3 or d==6:
            self.DNI=input("Cambiar DNI de cliente: ")
        elif d==4 or d==6:
            self.RUC=input("Cambiar RUC de cliente: ")
        elif d==5 or d==6:
            self.telefono=input("Actualizar telefono de cliente: ")

    def mostrar_cliente(self):
        print('{:<16}'.format(self.codigo)+
            '{:<25}'.format(self.nombres)+
            '{:<25}'.format(self.apellidos)+
            '{:<25}'.format(self.DNI)+
            '{:<25}'.format(self.RUC)+
            '{:<25}'.format(self.telefono))