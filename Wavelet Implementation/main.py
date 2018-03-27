from csv import reader
from numpy import mean, sqrt, square, arange
import numpy as np
import pywt
import time
import csv
from pd import peakdet
from cekvrms import cekfault
from location import lokasi
from ui import gui
from stored import store
import sys
import os
from time import sleep
import urllib2
import pygame

	
s1 = []
r1 = RingBuffer(capacity=1000, dtype=np.float)
r2 = RingBuffer(capacity=1000, dtype=np.float)
r3 = RingBuffer(capacity=1000, dtype=np.float)
ser = serial.Serial('/dev/ttyACM0', 115200)
f = float

while True:
    data = ser.readline()   #read data from serial
    if data:                #if there is data, append it to s
        s1.append(data)
    if len(s1) == 1:         #when s is 3 elements long, (all data has been retrieved)
        d1=s1[0]
        if d1[0] == '1' or d1[0] == '2' or d1[0] == '3':        
            nom1=d1[:4]
            dec1=d1[5:7]
            f=float(nom1)
        else:
            error=1
    
    if (f<2000):
        r1.append(f)
    elif (f>2000) and (f<3000):
        r2.append(f)
    elif (f>3000):
        r3.append(f)

        
    if len(r1)==1000 and len(r2)==1000 and len(r3)==1000:
        #print r1
        #print r2
        #print r3
        #fasa1=r1
        #fasa2=r2
        #fasa3=r3
        fasa1=np.array(r1)-1500
        fasa2=np.array(r2)-2500
        fasa3=np.array(r3)-3500
        print fasa1
        print fasa2
        print fasa3
        #Varms = sqrt(mean((fasa1**2)))
        #Vbrms = sqrt(mean((fasa2**2)))
        #Vcrms = sqrt(mean((fasa3**2)))
        #print Varms
        #print Vbrms
        #print Vcrms
    else:
        #print 'array belum penuh'
        s1 = []              #and then reset s to start over.   

[Vaf,Vbf,Vcf,Varms,Vbrms,Vcrms]=cekfault(fasa1,fasa2,fasa3)
Varmst=str(Varms)
Vbrmst=str(Vbrms)
Vcrmst=str(Vcrms)

if (Vaf==1):
    Vateks='Fault'
else:
     Vateks='Normal'
if (Vbf==1):
    Vbteks='Fault'
else:
    Vbteks='Normal'
if (Vcf==1):
    Vcteks='Fault'
else:
    Vcteks='Normal'
    
    #jika terdeteksi hubung singkat maka akan dilakukan pendeteksian dengan transformasi Wavelet
if (Vaf==1) or (Vbf==1) or (Vcf==1):
    posisi=lokasi(Va,Vb,Vc)
    posisis=str(posisi)
    now = time.strftime("%c")
    with open('log.csv', 'ab') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow([time.strftime("%c   "), "   %f   "%posisi,     "   %i   "%Vaf,"   %i   "%Vbf,"   %i   "%Vcf])
    
   






        
        


    myAPI = "3ENQDEQ049AARFYH"
    myDelay = 5 #how many seconds between posting data
    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
    
    f = urllib2.urlopen(baseURL + 
                                "&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s&field6=%s&field7=%s" % (Vateks, Vbteks,Vcteks,posisis,Varmst,Vbrmst,Vcrmst))

    sleep(5)

    
    pygame.mixer.init()
    pygame.mixer.music.load("sound.mp3")
    pygame.mixer.music.play()       
else:
    print 'normal'
    posisis='Normal'


    
    #Setup our API and delay
myAPI = "3ENQDEQ049AARFYH"
myDelay = 5 #how many seconds between posting data
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

f = urllib2.urlopen(baseURL + 
                                "&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s&field6=%s&field7=%s" % (Vateks, Vbteks,Vcteks,posisis,Varmst,Vbrmst,Vcrmst))

    
