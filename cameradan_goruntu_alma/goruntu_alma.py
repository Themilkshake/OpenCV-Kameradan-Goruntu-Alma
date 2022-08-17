import cv2
import numpy as np


"""
cv2.VideoCapture(0): bilgisayarda tanımlı olan kameraları çalıştırır. 
(0): bilgisayarın kendi kamerasını çalıştırır.
(1): usbye tanımlı olan kameradan görüntüyü alır.
(2): attığımız videodaki görüntüyü alır.
"""
kamera=cv2.VideoCapture(0)

""" 
ret: kameranın çalışıp çalışmadığını kontrol et.
kamera.read(): kamerayı oku.
"""
""" Döngüye giriyor.*** """
while True:
    ret,goruntu=kamera.read()
    
    """ 
    cv2.imshow("deneme", goruntu):
     30 ms'de 1 görüntü çekiyor.
    """
    
    cv2.imshow("deneme", goruntu)
    """ 32 değeri ascıı'de space tuşu.
    """
    if cv2.waitKey(30) & 0xFF == 32:
        break
    


"""
kamerayı serbest bırakıkyor.
"""
kamera.release()





"""
Parantez içerisindeki tüm pencereleri kapat anlamına gelir. Hiçbir şey yazmazsak,
hiçbir pencereyi kapatma anlamına gelir.
"""
cv2.destroyAllWindows()