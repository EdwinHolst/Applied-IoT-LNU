from Ubidots import sendData
from Sensors import readTemp, readPhotoRes
import time

DELAY = 600  # Delay in seconds
N_SAMPLES = 10

while True:
    temp_sum = 0
    photo_res_sum = 0
    for i in range(N_SAMPLES):
        temp_sample = readTemp()
        while temp_sample is None:
            temp_sample = readTemp()
            
        photo_res_sample = readPhotoRes()
        while photo_res_sample is None:
            photo_res_sample = readPhotoRes()
        temp_sum += temp_sample
        photo_res_sum += photo_res_sample
        time.sleep(DELAY/N_SAMPLES)
   
 
    returnValue = sendData(temp_sum/N_SAMPLES, photo_res_sum/N_SAMPLES)
    print(returnValue)   
