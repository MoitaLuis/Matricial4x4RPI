import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
LINHAS = [21,20,16,12]
COLUNAS = [19,13,6,5]

GPIO.setup(24,GPIO.OUT)
for i in range (4):
    GPIO.setup(LINHAS[i],GPIO.OUT)
for j in range (4):
    GPIO.setup(COLUNAS[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(24,GPIO.HIGH)

def leitura(LINHAS,CARACTERES):
    GPIO.output(LINHAS,GPIO.HIGH)
    if(GPIO.input(COLUNAS[0])==1):
        print(CARACTERES[0])
        sleep(0.5)
    if(GPIO.input(COLUNAS[1])==1):
        print(CARACTERES[1])
        sleep(0.5)
    if(GPIO.input(COLUNAS[2])==1):
        print(CARACTERES[2])
        sleep(0.5)
    if(GPIO.input(COLUNAS[3])==1):
        print(CARACTERES[3])
        sleep(0.5)
    GPIO.output(LINHAS,GPIO.LOW)
try:
    while True:
        leitura(LINHAS[0],["1","2","3","A"])
        leitura(LINHAS[1],["4","5","6","B"])
        leitura(LINHAS[2],["7","8","9","C"])
        leitura(LINHAS[3],["*","0","#","D"])
        sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nE1 fim do programa")
