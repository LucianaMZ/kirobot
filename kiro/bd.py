import sqlite3
import serial
import time

# CAMBIÁ esto por el COM real
puerto_esp32 = "COM8"

# Conexión serial con ESP32
ser = serial.Serial(puerto_esp32, 9600, timeout=1)
time.sleep(2)  # esperar que la ESP32 reinicie

# Conexión a la base de datos
conn = sqlite3.connect("kirobot.db")
cursor = conn.cursor()

# Leer todos los ejercicios
cursor.execute("SELECT nombre, accion FROM ejercicios_kirobot")
ejercicios = cursor.fetchall()

# Enviar cada ejercicio por serial
for nombre, accion in ejercicios:
    mensaje = f"{nombre}:{accion}\n"
    print(f"Enviando → {mensaje.strip()}")
    ser.write(mensaje.encode())
    time.sleep(1)  # espera entre envíos

# Cerrar conexiones
ser.close()
conn.close()
