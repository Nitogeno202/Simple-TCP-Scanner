import socket
import datetime
import sys

# Variables
direccion_ip = input("Ingresa la IP a escanear: ")
puertos = [
    22, 80, 88, 123, 135, 139, 162, 389, 443, 445, 514, 636, 1395, 1433, 3000, 3306, 3389,
    4443, 4444, 5000, 5044, 5045, 5432, 5555, 5985, 5986, 6379, 6514, 6660, 6661, 6662, 6663,
    6664, 6665, 6666, 6667, 6668, 6669, 6697, 8000, 8080, 8089, 8443, 9443, 9997, 10443, 27017,
    40080, 50050
]

print("Iniciando escaneo en", direccion_ip)

# Funcion
def escanear(ip, p):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        resultado = s.connect_ex((ip, p))
        
        if resultado == 0:
            print(f"[+] Puerto {p}: ABIERTO")
            s.close()
            return True # <--- ESTO ES LA CLAVE
        
        s.close()
        return False # <--- Si no es 0, devolvemos Falso
    except:
        return False

# Bucle
puertos_abiertos = 0

for p in puertos:
    # Si modificamos la función para que devuelva True al encontrar uno:
    if escanear(direccion_ip, p):
        puertos_abiertos += 1

if puertos_abiertos == 0:
    print("\n[!] No se encontraron puertos abiertos en los rangos especificados.")
else:
    print(f"\n[+] Escaneo completado. Se encontraron {puertos_abiertos} puertos abiertos.")


print("Escaneo finalizado")



