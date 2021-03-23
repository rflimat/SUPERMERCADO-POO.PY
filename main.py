from Cliente import Cliente
from Producto import Producto
from Proveedor import Proveedor
from Factura import Factura
import buscar
import efunciones
from os import system

listaProveedores=[]
listaProductos=[]
listaClientes=[]
listaFacturas=[]

op=None
while op!=5:
    system("cls")
    efunciones.menu()
    op=int(input("\nIngrese una opcion: "))
    system("cls")
    if op==1:
        opr=None
        efunciones.menu_pr()
        opr=int(input("\nIngrese una opcion: "))
        system("cls")
        if opr==1:
            print("\tREGISTRAR PROVEEDOR\n")
            n=input("Ingrese nombre de proveedor: ")
            r=input("Ingrese RUC de proveedor: ")
            t=input("Ingrese telefono de proveedor: ")
            d=input("Ingrese direccion de proveedor: ")
            objProveedor=Proveedor(len(listaProveedores),n,r,t,d)
            listaProveedores.append(objProveedor)
        elif opr==2:
            print("\tMODIFICAR PROVEEDOR")
            c=input("\nIngrese codigo de proveedor: ")
            pos=buscar.buscar(c,listObjects=listaProveedores)
            if pos>=0:
                print("\nCodigo correcto")
                efunciones.menu_mpr()
                opr=int(input("\nIngrese una opcion: "))
                if opr==6:
                    continue
                else:
                    print()
                    listaProveedores[pos].modificar_proveedor(opr)
            else:
                print("\nCodigo incorrecto. Ingrese de nuevo!")
                system("pause")
        elif opr==3:
            print("\tLISTA DE PROVEEDORES\n")
            print('{:<16}'.format("Codigo")+
            '{:<25}'.format("Nombre")+
            '{:<25}'.format("RUC")+
            '{:<25}'.format("Telefono")+
            '{:<25}'.format("Direccion"))
            for proveedor in listaProveedores:
                proveedor.mostrar_proveedor()
            print("")
            system("pause")
        elif opr==4:
            continue
        else:
            print("Opcion incorrecta. Ingrese de nuevo!")
            system("pause")
    elif op==2:
        opp=None
        efunciones.menu_p()
        opp=int(input("\nIngrese una opcion: "))
        system("cls")
        if opp==1:
            print("\tREGISTRAR PRODUCTO\n")
            n=input("Ingrese nombre de producto: ")
            cn=int(input("Ingrese cantidad de producto: "))
            ct=input("Ingrese categoria de producto: ")
            pu=float(input("Ingrese precio unitario de producto: "))
            c=input("Ingrese codigo de proveedor: ")
            pos=buscar.buscar(c,listObjects=listaProveedores)
            if pos>=0:
                print("\nCodigo correcto")
                objProducto=Producto(len(listaProductos),n,cn,ct,pu,listaProveedores[pos])
                listaProductos.append(objProducto)
                system("pause")
                continue
            else:
                print("\nCodigo incorrecto. Ingrese de nuevo!")
                system("pause")
        elif opp==2:
            print("\tMODIFICAR PRODUCTO")
            c=input("\nIngrese codigo de producto: ")
            pos=buscar.buscar(c,listObjects=listaProductos)
            if pos>=0:
                print("\nCodigo correcto")
                efunciones.menu_mp()
                opp=int(input("\nIngrese una opcion: "))
                if opp==5:
                    cprr=input("\nIngrese codigo de proveedor: ")
                    pos1=buscar.buscar(cprr,listObjects=listaProveedores)
                    if pos1>=0:
                        print("\nCodigo correcto")
                        listaProductos[pos].set_proveedor(listaProveedores[pos1])
                        system("pause")
                    else:
                        print("\nCodigo incorrecto. Ingrese de nuevo!")
                        system("pause")
                elif opp==7:
                    continue
                else:
                    print()
                    listaProductos[pos].modificar_producto(opp)
            else:
                print("\nCodigo incorrecto. Ingrese de nuevo!")
                system("pause")
        elif opp==3:
            print("\tLISTA DE PRODUCTOS\n")
            print('{:<16}'.format("Codigo")+
            '{:<25}'.format("Nombre")+
            '{:<25}'.format("Cantidad")+
            '{:<25}'.format("Categoria")+
            '{:<25}'.format("Precio Unitario")+
            '{:<25}'.format("Proveedor"))
            for producto in listaProductos:
                producto.mostrar_producto()
            print("")
            system("pause")
        elif opp==4:
            continue
        else:
            print("Opcion incorrecta. Ingrese de nuevo!")
            system("pause")
    elif op==3:
        oc=None
        efunciones.menu_c()
        oc=int(input("\nIngrese una opcion: "))
        system("cls")
        if oc==1:
            print("\tREGISTRAR CLIENTE\n")
            n=input("Ingrese nombres de cliente: ")
            a=input("Ingrese apellidos de cliente: ")
            d=input("Ingrese DNI de cliente: ")
            r=input("Ingrese RUC de cliente: ")
            t=input("Ingrese telefono de cliente: ")
            objCliente=Cliente(len(listaClientes),n,a,d,r,t)
            listaClientes.append(objCliente)
        elif oc==2:
            print("\tMODIFICAR CLIENTE")
            c=input("\nIngrese codigo de cliente: ")
            pos=buscar.buscar(c,listObjects=listaClientes)
            if pos>=0:
                print("\nCodigo correcto")
                efunciones.menu_mc()
                oc=int(input("\nIngrese una opcion: "))
                if oc==7:
                    continue
                else:
                    print()
                    listaClientes[pos].modificar_cliente(oc)
            else:
                print("\nCodigo incorrecto. Ingrese de nuevo!")
                system("pause")
        elif oc==3:
            print("\tLISTA DE CLIENTES\n")
            print('{:<16}'.format("Codigo")+
            '{:<25}'.format("Nombres")+
            '{:<25}'.format("Apellidos")+
            '{:<25}'.format("DNI")+
            '{:<25}'.format("RUC")+
            '{:<25}'.format("Telefono"))
            for cliente in listaClientes:
                cliente.mostrar_cliente()
            print("")
            system("pause")
        elif oc==4:
            continue
        else:
            print("Opcion incorrecta. Ingrese de nuevo!")
            system("pause")
    elif op==4:
        of=None
        efunciones.menu_f()
        of=int(input("\nIngrese una opcion: "))
        system("cls")
        if of==1:
            print("\tREGISTRAR CLIENTE\n")
            cc=input("Ingrese codigo de cliente: ")
            pos=buscar.buscar(cc,listObjects=listaClientes)
            if pos>=0:
                print("Codigo correcto")
                objFactura=Factura(len(listaFacturas),listaClientes[pos])
                det="Si"
                y=0
                while det=="Si" or det=="si" and y<20:
                    cp=input("\nIngrese codigo de producto: ")
                    pos1=buscar.buscar(cp,listObjects=listaProductos)
                    if pos1>=0:
                        print("Codigo correcto")
                        ctp=int(input("\nIngrese cantidad de productos: "))
                        if listaProductos[pos1].get_cantidad()==0:
                            print("Producto agotado")
                        elif listaProductos[pos1].get_cantidad()-ctp<0:
                            print("Esta disponible solamente "+str(listaProductos[pos1].get_cantidad()))
                        else:
                            objFactura.set_productos(listaProductos[pos1],ctp)
                            print("Producto registrado")
                            y=y+1
                        det=input("\nDesea registrar mas productos (Si/No): ")
                    else:
                        print("\nCodigo incorrecto. Ingrese de nuevo!")
                listaFacturas.append(objFactura)
            else:
                print("\nCodigo incorrecto. Ingrese de nuevo!")
            system("pause")
        elif of==2:
            ofv=None
            efunciones.menu_vf()
            ofv=int(input("\nIngrese una opcion: "))
            system("cls")
            if ofv==1:
                print("\tBUSCAR FACTURA\n")
                cf=input("Ingrese codigo de factura: ")
                pos=buscar.buscar(cf,listObjects=listaFacturas)
                system("cls")
                if pos>=0:
                    listaFacturas[pos].ver_factura()
                    print("")
                else:
                    print("\nCodigo incorrecto. Ingrese de nuevo!")
                system("pause")
            elif ofv==2:
                print("\tLISTA DE FACTURAS\n")
                cc=input("Ingrese codigo de cliente: ")
                pos=buscar.buscar(cc,listObjects=listaClientes)
                system("cls")
                if pos>=0:
                    print("\tLISTA DE FACTURAS\n")
                    print('{:<16}'.format("Codigo")+
                    '{:<25}'.format("Nombre")+
                    '{:<25}'.format("Fecha")+
                    '{:<25}'.format("Total"))
                    for factura in listaFacturas:
                        if factura.get_codigoc()==cc:
                            factura.lista_facturas()
                    print("")
                    cf=input("Ingrese codigo de factura: ")
                    pos1=buscar.buscar(cf,listObjects=listaFacturas)
                    system("cls")
                    if pos1>=0:
                        listaFacturas[pos1].ver_factura()
                        print("")
                    else:
                        print("\nCodigo incorrecto. Ingrese de nuevo!")
                    system("pause")
                elif ofv==3:
                    continue
        elif of==3:
            continue
        else:
            print("Opcion incorrecta. Ingrese de nuevo!")
            system("pause")
    elif op==5:
        continue
    else:
        print("Opcion incorrecta. Ingrese de nuevo!")
        system("pause")

