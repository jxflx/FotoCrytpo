from cryptosteganography import CryptoSteganography
from getpass import getpass


def encode():
    inputimg  = input('Introduce la dirección de la imagen: ')
    imgName = inputimg.split('.')
    outputimg = f"{imgName[0]}-encr.png"
    separator()
    password = getpass()
    message  = input('Escribe tu mensaje a ocultar: ')

    crypto_steganography = CryptoSteganography(password)
    crypto_steganography.hide(inputimg, outputimg, message)
    separator()
    print('Done!')

def decode():
    password = getpass()
    targetImg = input('Introduce la ruta de la imagen: ')
    separator()
    crypto_steganography = CryptoSteganography(password)
    secret = crypto_steganography.retrieve(targetImg)
    
    if(secret == None):
        print('Contraseña incorrecta')
    else:
        print('Tu mensaje oculto es: ')
        separator()
        print(secret)
        



def start():
    print('Binevenidos a este menú interactivo')
    while(True):
        print("""¿Qué desea hacer?
        1) Crear una imagen con un mensaje
        2) Leer una imagen
        3) Salir
        """)
        op = input()
        separator()
        if op == '1':
            encode()
            separator()
        elif op == '2':
            decode()
            separator()
        elif op == '3':
            print('Hasta la próximaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!')
            break
        else:
            print('La opción: ' + op + ' no existe, inténtalo de nuevo')




def separator():
    """Función que imprime asteriscos :3"""
    print('*' * 25)

if __name__ == "__main__":
    start()
    
