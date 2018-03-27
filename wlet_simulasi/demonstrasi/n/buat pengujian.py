#import library
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
from numpy_ringbuffer import RingBuffer
import serial






s1 = []
r1 = RingBuffer(capacity=10, dtype=np.float)
r2 = RingBuffer(capacity=10, dtype=np.float)
r3 = RingBuffer(capacity=10, dtype=np.float)
ser = serial.Serial('/dev/ttyACM0', 9600)
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

    
    #data di ringbuffer akan diproses apabila sudah penuh    
    if len(r1)==10 and len(r2)==10 and len(r3)==10:

        #mengubah type ringbuffer menjadi array numppy 
        Va=np.array(r1,dtype=float)
        Vb=np.array(r2,dtype=float)
        Vc=np.array(r3,dtype=float)

        #pengecekan fasa yang fault
        [Vaf,Vbf,Vcf,Varms,Vbrms,Vcrms]=cekfault(Va,Vb,Vc)
        #mengubah kondisi jalur transmisi jadi tipe string
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

            #menulis didalam file log
            now = time.strftime("%c")
            with open('log.csv', 'ab') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow([time.strftime("%c   "), "   %f   "%posisi,     "   %i   "%Vaf,"   %i   "%Vbf,"   %i   "%Vcf])
        
       






            
            

            

        
            pygame.mixer.init()
            pygame.mixer.music.load("sound.mp3")
            pygame.mixer.music.play() 
			myAPI = "3ENQDEQ049AARFYH"
			myDelay = 1 #how many seconds between posting data
			baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

			f = urllib2.urlopen(baseURL + 
                                    "&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s&field6=%s&field7=%s" % (Vateks, Vbteks,Vcteks,posisis,Varmst,Vbrmst,Vcrmst))

        
			time.sleep(100)
        else:
            print 'normal'
            posisis='Normal'


        
        #kirim data keserver thinkspeak
        myAPI = "3ENQDEQ049AARFYH"
        myDelay = 5 #how many seconds between posting data
        baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

        f = urllib2.urlopen(baseURL + 
                                    "&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s&field6=%s&field7=%s" % (Vateks, Vbteks,Vcteks,posisis,Varmst,Vbrmst,Vcrmst))

        
    
    else:
        print 'array belum penuh'
        s1 = []              #and then reset s to start over.






