import numpy as np
import pywt


def dwttransform(Va,Vb,Vc):
    

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


    return cd2abs

    
