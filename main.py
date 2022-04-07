from machine import Pin, ADC
from time import sleep
from math import log
adc=ADC(26)
tempcero=298
beta=3950
rest=10000
vcc=3.3

while True:
    valor=adc.read_u16()
    vrx=valor*vcc/65535
    ntc=(rest*vrx)/(vcc-vrx)
    tob=beta*tempcero
    a=ntc/rest
    lg=log(a)
    lgto=tempcero*lg
    tempk=tob/(lgto+beta)
    temp=tempk-273
    print("El valor del ADC es: {}".format(valor))
    print("El valor de tension medido es: {}".format(vrx))
    print("El valor de resistencia del NTC es:{}".format(ntc))
    print("La temperatura es: {}".format(temp))
    sleep(2)
