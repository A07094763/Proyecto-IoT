# archivo donde estan los tres códigos juntos.
# Conexión a la base de datos
import mysql.connector

# Configura la conexión a la base de datos MySQL
db_connection = mysql.connector.connect(
    host="tu_host",
    user="tu_usuario",
    password="tu_contraseña",
    database="nombre_de_tu_base_de_datos"
)

# codigos 
import RPi.GPIO as GPIO
from time import sleep
from bmp_280 import BMP280
import time

# Configuración de pines para motores
GPIO.setmode(GPIO.BOARD)
Motor1 = 16    # Entrada Motor1
Motor2 = 18    # Entrada Motor1
Motor3 = 22    # Habilitar Motor1
Motor4 = 23    # Entrada Motor2
Motor5 = 24    # Entrada Motor2
Motor6 = 26    # Habilitar Motor2

# Configuración de pines para sensor ultrasónico
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 23
GPIO_ECHO = 24
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.output(GPIO_TRIGGER, False)

# Inicialización del sensor BMP280
bmp = BMP280(port=1, mode=BMP280.FORCED_MODE, oversampling_p=BMP280.OVERSAMPLING_P_x16, oversampling_t=BMP280.OVERSAMPLING_T_x1,
             filter=BMP280.IIR_FILTER_OFF, standby=BMP280.T_STANDBY_1000)

try:
    # Código para controlar motores
    GPIO.setup(Motor1, GPIO.OUT)
    GPIO.setup(Motor2, GPIO.OUT)
    GPIO.setup(Motor3, GPIO.OUT)
    GPIO.setup(Motor4, GPIO.OUT)
    GPIO.setup(Motor5, GPIO.OUT)
    GPIO.setup(Motor6, GPIO.OUT)

    # Código para medir distancia con el sensor ultrasónico y guardar datos en un archivo
    sFileStamp = time.strftime('%Y%m%d%H')
    sFileName = '\out' + sFileStamp + '.txt'
    f = open(sFileName, 'a')
    f.write('TimeStamp,Value' + '\n')
    print("Inicia la toma de datos")

    while True:
        print("Acerque el objeto para medir la distancia")
        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
        start = time.time()
        while GPIO.input(GPIO_ECHO) == 0:
            start = time.time()
        while GPIO.input(GPIO_ECHO) == 1:
            stop = time.time()
        elapsed = stop - start
        distance = (elapsed * 34300) / 2
        sTimeStamp = time.strftime('%Y%m%d%H%M%S')
        f.write(sTimeStamp + ',' + str(distance) + '\n')
        print(sTimeStamp + ' ' + str(distance))
        time.sleep(1)
        sTmpFileStamp = time.strftime('%Y%m%d%H')

except KeyboardInterrupt:
    print('\n' + 'Termina la captura de datos.' + '\n')
    f.close
    GPIO.cleanup()

finally:
    # Lectura de presión y temperatura con el sensor BMP280
    pressure = bmp.read_pressure()
    temp = bmp.read_temperature()

    print("Presión (hPa): " + str(pressure))
    print("Temperatura (°C): " + str(temp))



