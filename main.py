import click
from os.path import exists
from PIL import Image

CONTEXT_SETTINGS = dict(help_option_names=['-h', '-help'])


@click.command(context_settings=CONTEXT_SETTINGS, no_args_is_help=True)
@click.option("-i", help="El archivo a cambiar su resolucion")
@click.option("-o", help="El nombre del archivo con su resolucion cambiada")
@click.option("-size", help="La resolucion a cambiar")
def resize(i, o, size):
    try:
        f = Image.open(i)
    except FileNotFoundError:
        print("El archivo no existe :(")
        print("Cerrando")
        return
    temp = ""
    sizes = []
    try:
        for i in size:
            if i == "x":
                sizes.append(int(temp))
                temp = ""
            else:
                temp += i
        sizes.append(int(temp))
    except:
        print("No diste un tamaño para cambiar la resolucion")
        print("Cerrando")
    del temp
    if exists(f"{o}"):
        print(f"El archivo {o} ya existe, desea sobreescribirlo")
        option = input("S/N> ")
        if option == "S":
            resized_image = f.resize(sizes)
            resized_image.save(f"{o}")
            return
        else:
            print("Cerrando....")
            return
    try:
        resized_image = f.resize(sizes)
        resized_image.save(f"{o}")
    except NameError:
        print("No diste el nombre del archivo a guardar :(")
        print("Cerrando")
        return
    except ValueError:
        if o == None:
            print("No diste el nombre del archivo a guardar :(")
            print("Cerrando")
            return
        else:
            print(f"{o} No es un nombre de archivo valido")
            return
    except OSError:
        f.convert("RGB").save(f"{o}")
        return
