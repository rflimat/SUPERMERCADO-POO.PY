#MENUS DE TODAS LAS OPCIONES

def menu():
    print("\tSISTEMA DE FACTURACION PARA SUPERMERCADO\n"+
    "\t     SUPERMERCADO XD (VERSION 1.0)")
    print("\n\tMENU DE OPCIONES\n"+
        "\n[1] Proveedores"+
        "\n[2] Productos"+
        "\n[3] Clientes"+
        "\n[4] Facturas"+
        "\n[5] Salir")

def menu_pr():
    print("\tSISTEMA DE PROVEEDORES")
    print("\n\tMENU DE OPCIONES\n"+
            "\n[1] Registrar proveedor"+
            "\n[2] Modificar proveedor"+
            "\n[3] Ver proveedor"+
            "\n[4] Salir")

def menu_mpr():
    print("\nEliga el dato que desea modificar:\n"+
            "\n[1] Nombre"+
            "\n[2] RUC"+
            "\n[3] Telefono"+
            "\n[4] Direccion"+
            "\n[5] Todo"+
            "\n[6] Salir")

def menu_p():
    print("\tSISTEMA DE PRODUCTOS")
    print("\n\tMENU DE OPCIONES\n"+
            "\n[1] Registrar producto"+
            "\n[2] Modificar producto"+
            "\n[3] Ver producto"+
            "\n[4] Salir")

def menu_mp():
    print("\nEliga el dato que desea modificar:\n"+
            "\n[1] Nombre"+
            "\n[2] Cantidad"+
            "\n[3] Categoria"+
            "\n[4] Precio unitario"+
            "\n[5] Proveedor"+
            "\n[6] Todo"+
            "\n[7] Salir")

def menu_c():
    print("\tSISTEMA DE CLIENTES")
    print("\n\tMENU DE OPCIONES\n"+
            "\n[1] Registrar cliente"+
            "\n[2] Modificar cliente"+
            "\n[3] Ver cliente"+
            "\n[4] Salir")

def menu_mc():
    print("\nEliga el dato que desea modificar:\n"+
            "\n[1] Nombres"+
            "\n[2] Apellidos"+
            "\n[3] DNI"+
            "\n[4] RUC"+
            "\n[5] Telefono"+
            "\n[6] Todo"+
            "\n[7] Salir")

def menu_f():
    print("\tSISTEMA DE FACTURAS")
    print("\n\tMENU DE OPCIONES\n"+
            "\n[1] Generar factura"+
            "\n[2] Ver facturas"+
            "\n[3] Salir")

def menu_vf():
    print("\tVER FACTURAS\n"+
            "\nBuscar a traves del: \n"+
            "\n[1] Codigo de factura"+
            "\n[2] Codigo de cliente"+
            "\n[3] Salir")
