import os
import matplotlib.pyplot as plt
from pylab import plot, show, close

altitudeArr = (0,2,4,6,8,10,
               12,14,16,18,20,
               22,24,26,28,30,
               32,34,36,38,40)              #[km]
ambientTempArr = (287,276,265,250,237,224,
                  218,218,218,218,218,
                  219,220,222,224,226,
                  228,233,238,244,248)      #[K]
flightUpspeedRate = 1/10                    #[h/km]

timePer2km = 12                             #[min]
isolCondCoeff = 0.033                       #[W/(m*K)]
surface = 0.072                             #[m^2]
thickness = 0.05                             #[m]
airSpecificHeat = 1005                      #[J/(kg*K)]
airVolume = 0.001                           #[m^3]
airDensity = 1.2                            #[kg/m^3]

transferredHeatConstant = (isolCondCoeff*surface)/thickness
airMass = airDensity*airVolume

def calcTransferredHeatRate(currentTemp, ambientTemp):
    transferedHeatRate = (currentTemp - ambientTemp)*transferredHeatConstant
    print("transferHeatRate = {}".format(transferedHeatRate))
    return transferedHeatRate

def calcInteriorTempChange(heatRate, time, currentTemp):
    heatTransfer = heatRate * time
    changedTemp = currentTemp - heatTransfer/(airSpecificHeat*airMass)
    return changedTemp

def main():
    startHeat = airDensity*airSpecificHeat*airVolume
    temp = ambientTempArr[0]
    tempVal = []
    tempVal.append(temp)
    altitude = altitudeArr[0]
    i = 1
    while (altitude < 39):
        heatRate = calcTransferredHeatRate(temp, ambientTempArr[i])
        temp = calcInteriorTempChange(heatRate, timePer2km, tempVal[(i-1)])
        tempVal.append(temp)
        altitude = altitudeArr[i]
        i+=1
    
    plt.plot(tempVal,altitudeArr)
    plt.plot(ambientTempArr,altitudeArr)
    plt.ylabel("label")
    plt.show()
    
if __name__== "__main__":
    main()    
