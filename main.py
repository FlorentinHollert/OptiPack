import sys
import time
from ArucoDetection import CaptureAndMeasure
from algo import article
#TODO: 1 ändern der Werte im return value capture & measure
# 2 Schreiben des aufrufs in main --> 4 werte speichern, besten matchen & werte printen --> kann es sein?
#hinzügen zur Liste 
#soviele iterationen bis nuzer abbricht
#3 fixen problem mit cm werten
measuredValues = []
#input('Press any key to start packaging.\n')
while(True):
    #a,b = CaptureAndMeasure.caputureInput()
    input("press any key to continue")
    #c,d = CaptureAndMeasure.caputureInput()
    a=1.5
    b=-13.3
    c=12.9
    d=-13.5
    ac = a-c
    ad = a-d
    bc = b-c
    bd = b-d
    ac = abs(ac)
    ad = abs(ad)
    bc = abs(bc)
    bd = abs(bd)
    value = max(ac, ad, bc, bd)
    if value==ac:
        measuredValues.append(article(a,b,d))
    if value==ad:
        measuredValues.append(article(a,b,c))
    if value==bc:
        measuredValues.append(article(a,b,d))
    if value==bd:
        measuredValues.append(article(a,b,c))

    input = ("Press A to scan another item and any other key to continue to packaging")
    if (input != "A"):
        break
    
print(measuredValues)
    
    #find most similar values 
# Initialisieren der Variablen (Artikel-array)
# image recognition
    # loop
    # 1. Image für ein Artikel
    # 2. Image ""
    # Abspeichern der Variablen (Artikel)
# Start Algo
# Lösung des Problems
# Front-End