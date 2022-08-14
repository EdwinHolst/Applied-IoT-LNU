from machine import Pin,ADC
import time
import math

def readTemp():
    SAMPLES = 10
    pin_out = Pin(25, Pin.OUT)
    pin_out.on()
    adc=ADC(Pin(32))
    adc.atten(ADC.ATTN_11DB)
    adc.width(ADC.WIDTH_12BIT)
    
    v_sample_sum = 0
    for _ in range(SAMPLES):
        v_sample_sum += adc.read_uv()
        
    v = v_sample_sum/1000000/SAMPLES
    
    if v < 3.3:
        Rt=10*v/(3.3-v)
        tempK=(1/(1/(273.15+25)+(math.log(Rt/10))/3950))
        tempC=tempK-273.15
        return tempC
    return None

def readPhotoRes():
    SAMPLES = 10
    pin_out = Pin(26, Pin.OUT)
    pin_out.on()
    adc=ADC(Pin(33))
    adc.atten(ADC.ATTN_11DB)
    adc.width(ADC.WIDTH_12BIT)
    
    v_sample_sum = 0
    for _ in range(SAMPLES):
        v_sample_sum += adc.read_uv()
        
    v = v_sample_sum/1000000/SAMPLES
    
    if v < 3.3:
        r = 10*v/(3.3-v)
        return r
    return None