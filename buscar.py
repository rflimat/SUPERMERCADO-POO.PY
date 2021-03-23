def buscar(dato,listObjects):
    x=0
    pos=-1
    for object in listObjects:
        if dato==object.get_codigo():
            pos=x
            break
        else:
            x=x+1
    return pos