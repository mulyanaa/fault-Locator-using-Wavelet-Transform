from numpy import mean, sqrt, square, arange
import sys

import os

import urllib2


def cekfault(Va,Vb,Vc):
    #nilai tegangan RMS saat normal (dari percobaan simulasi)
    Varmsn = 337008
    Vbrmsn = 338237.4
    Vcrmsn = 336890.7
 
    #menghitung VRMS tiap fasa
    Varms = sqrt(mean((Va**2)))
    Vbrms = sqrt(mean((Vb**2)))
    Vcrms = sqrt(mean((Vc**2)))
 
    #konstanta batas pengurangan
    k=0.863022517
 
    #batas tegangan terdeteksi Fault
    Vabatas=Varmsn*k
    Vbbatas=Vbrmsn*k
    Vcbatas=Vcrmsn*k


    #fasa a yang fault
    #Vaf,Vbf,Vcf merupakan indikator apakah fasa mengalami fault, nilai satu berarti fault dan nol berarti normal

    if (Varms <= Vabatas):
        Vaf=1
	Vateks='Fault'
    else :
	Vaf=0
        Vateks='NORMAL'

    #fasa b yang fault    
    if (Vbrms <= Vbbatas): 
        Vbf=1
	Vbteks='Fault'
    else :
	Vbf=0
	Vbteks='NORMAL'

    if (Vcrms <= Vbbatas): 
        Vcf=1
	Vcteks='Fault'
    else :
	Vcf=0
	Vcteks='Normal'
        
    
    
    return Vaf,Vbf,Vcf,Varms,Vbrms,Vcrms
