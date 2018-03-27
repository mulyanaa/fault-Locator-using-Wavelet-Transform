import numpy as np
import pywt
from pd import peakdet


def lokasi(Va,Vb,Vc):
    

 	#transformasi Clarke untuk mendapatkan tegangan dasar 
    V1=np.multiply(Va,0.57735)+ np.multiply(Vb,0.57735) + np.multiply(Vc,0.57735)
    V2=np.multiply(Va,0.81645)+ np.multiply(Vb,-0.40825) + np.multiply(Vc,-0.40825)
    V3=np.multiply(Vb,0.70711) + np.multiply(Vc,-0.70711)
	
	#Transformasi Wavelet db4 untuk mendapatkan coefisien detail dan koefisien aproksimasi
	#untuk mode ground dan mode aerial
    [ca1,cd1] = pywt.dwt(V1, 'db4')
    [ca2,cd2] = pywt.dwt(V2, 'db4')
	
	#mendapatkan nilai absolut dari koefisien cd2
    cd2abs=abs(cd2)
    [maxi,mini]=peakdet(cd2abs,10)
    t1=maxi[0][0]
    t2=maxi[1][0]
    t3=maxi[2][0]
    f=t2-t1
	
    if f==1 or f==2 :
        deltat=t3-t1
    else:
        deltat=f
		
    L=len(cd2abs)
    V=297074.826
    posisi=(V*deltat*0.5/L)/2


    return posisi

    
