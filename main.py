import os

altitudeArr = (0,2,4,6,8,10,
               12,14,16,18,20,
               22,24,26,28,30,
               32,34,36,38,40)              #[km]
ambientTempArr = (287,276,265,250,237,224,
                  218,218,218,218,218,
                  219,220,222,224,226,
                  228,233,238,244,248)      #[K]
interval = 10                               #[min]
startTemp = 271                             #[K]
isolCondCoeff = 0.033                       #[W/(m*K)]
surface = 0.072                             #[m^2]
thickness = 0.02                            #[m]
airSpecificHeat = 1005                      #[J/(kg*K)]
airVolume = 0.001                           #[m^3]
airDensity = 1.2                            #[kg/m^3]

startHeat = airDensity*airSpecificHeat*airVolume

transferredHeatConstant = (isolCondCoeff*surface)/thickness
temp = ambientTempArr[0]

def calcTransferredHeatRate(i):
    transferedHeatRate = (temp - ambientTempArr[i])*transferredHeatConstant
    return transferedHeatRate
def calcInteriorTempChange(heatRate, time, temp):
    heatTransfer = heatRate * time
    changedTemp = heatTransfer/(airSpecificHeat*airDensity*airVolume) - temp
    return changedTemp


def main():
    
    