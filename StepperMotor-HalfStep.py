from machine import Pin
import time

in1 = Pin(12, Pin.OUT)
in2 = Pin(14, Pin.OUT)
in3 = Pin(26, Pin.OUT)
in4 = Pin(33, Pin.OUT)

while True:
    in1.value(1)
    in2.value(1)
    in3.value(0)
    in4.value(0)
    time.sleep(0.005) #1
    
    in1.value(0)
    in2.value(1)
    in3.value(0)
    in4.value(0)
    time.sleep(0.005) #2
    
    in1.value(0)
    in2.value(1)
    in3.value(1)
    in4.value(0)
    time.sleep(0.005) #3
    
    in1.value(0)
    in2.value(0)
    in3.value(1)
    in4.value(0)
    time.sleep(0.005) #4
    
    in1.value(0)
    in2.value(0)
    in3.value(1)
    in4.value(1)
    time.sleep(0.005) #5
    
    in1.value(0)
    in2.value(0)
    in3.value(0)
    in4.value(1)
    time.sleep(0.005) #6
    
    in1.value(1)
    in2.value(0)
    in3.value(0)
    in4.value(1)
    time.sleep(0.005) #7
    
    in1.value(1)
    in2.value(0)
    in3.value(0)
    in4.value(0)
    time.sleep(0.005) #8
