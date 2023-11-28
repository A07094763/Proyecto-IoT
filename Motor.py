import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor1 = 16    # Entrada Motor1
Motor2 = 18    # Entrada Motor1
Motor3 = 22    # Habilitar Motor1
Motor4 = 23    # Entrada Motor2
Motor5 = 24    # Entrada Motor2
Motor6 = 26    # Habilitar Motor2

GPIO.setup(Motor1, GPIO.OUT)
GPIO.setup(Motor2, GPIO.OUT)
GPIO.setup(Motor3, GPIO.OUT)
GPIO.setup(Motor4, GPIO.OUT)
GPIO.setup(Motor5, GPIO.OUT)
GPIO.setup(Motor6, GPIO.OUT)

try:
    # Motor 1
    print("Adelante Motor 1")
    GPIO.output(Motor1, GPIO.HIGH)
    GPIO.output(Motor2, GPIO.LOW)
    GPIO.output(Motor3, GPIO.HIGH)
    sleep(3)

    print("Atras Motor 1")
    GPIO.output(Motor1, GPIO.LOW)
    GPIO.output(Motor2, GPIO.HIGH)
    GPIO.output(Motor3, GPIO.HIGH)
    sleep(3)

    print("Detener Motor 1")
    GPIO.output(Motor3, GPIO.LOW)
    sleep(1)

    # Motor 2
    print("Adelante Motor 2")
    GPIO.output(Motor4, GPIO.HIGH)
    GPIO.output(Motor5, GPIO.LOW)
    GPIO.output(Motor6, GPIO.HIGH)
    sleep(3)

    print("Atras Motor 2")
    GPIO.output(Motor4, GPIO.LOW)
    GPIO.output(Motor5, GPIO.HIGH)
    GPIO.output(Motor6, GPIO.HIGH)
    sleep(3)

    print("Detener Motor 2")
    GPIO.output(Motor6, GPIO.LOW)
    sleep(1)

finally:
    GPIO.cleanup()
