from PIL import Image

config = {}

try:
    archivo = open("config.txt", 'r')
except FileNotFoundError:
    raise FileNotFoundError('No se encontró el archivo "config.txt".')

try:
    for linea in archivo:
        try:
            clave, valor = linea.strip().split("=")
            config[clave] = float(valor) if "." in valor else int(valor)
        except ValueError:
            raise ValueError('Línea inválida en "config.txt": ' + linea.strip())
finally:
    archivo.close()

#print(config)
try:
    with open("clase.csv", 'r') as data:
        datos = data.readlines() #
except FileNotFoundError:
    raise FileNotFoundError('No se encontró el archivo "clase.csv".')

try:
    alto, ancho, max_iter =config["alto"], config["ancho"], config["max_iter"]
except KeyError as e:
    raise KeyError('Falta la clave ' + str(e) + ' en "config.txt".')

try:
    img = Image.new("HSV", (ancho, alto))
except Exception as e:
    raise Exception('No se pudo crear la imagen: ' + str(e))

#QUITAR ENCABEZADOS
try:
    encabezados = datos.pop(0)
except IndexError:
    raise IndexError('El archivo "clase.csv" está vacío.')

#print(encabezados)
try:
    for dato in datos:
        try:
            fila, columna, iteraciones = map(int, dato.strip().split(","))
        except ValueError:
            raise ValueError('Fila inválida en "clase.csv": ' + dato.strip())

        brillo = 40 if (iteraciones == max_iter) else int((iteraciones / max_iter) * 255)

        try:
            img.putpixel((columna, fila), (brillo, 255, 255))
        except IndexError:
            raise IndexError('Coordenadas fuera de rango: (' + str(columna) + ', ' + str(fila) + ')')
except ZeroDivisionError:
    raise ZeroDivisionError('"max_iter" no puede ser 0 en "config.txt".')

try:
    img_rgb = img.convert('RGB')
    img_rgb.save("mandelbrot-clase.png")
except Exception as e:
    raise Exception('No se pudo guardar la imagen: ' + str(e))

print("DONE")
