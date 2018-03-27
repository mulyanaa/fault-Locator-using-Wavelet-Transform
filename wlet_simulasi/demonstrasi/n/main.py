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







#membuka file csv
with open('normal.csv', 'r') as f:
    data = list(reader(f))
	
	
#memasukan data kedalam array 
t = [i[0] for i in data[1::]]
Va = [i[1] for i in data[1::]]
Vb = [i[2] for i in data[1::]]
Vc = [i[3] for i in data[1::]]

Va=np.array(Va,dtype=float)
Vb=np.array(Vb,dtype=float)
Vc=np.array(Vc,dtype=float)
for i in range(1,10000):
    [Vaf,Vbf,Vcf,Varms,Vbrms,Vcrms]=cekfault(Va,Vb,Vc)
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

    
