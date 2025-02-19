import numpy as np

class chargedParticle():
#Properties of all Charged Particles (Class Properties)
    elementaryCharge=1.60e-19
    epsilon_0=8.85e-12

    def __init__(self,location,charge):
         self.location=location 
         self.charge=charge

    def chargeNumberCalculator(self):
         chargeNumber=self.charge/self.elementaryCharge
         return chargeNumber
 
    def distanceCalculator(self,locationOfInterest):
         distanceVector=locationOfInterest-self.location
         distance=np.linalg.norm(distanceVector) 
         directionVector=distanceVector/distance
         return directionVector, distance

    def electricFieldCalculator(self,locationOfInterest):
         prefactors=1/4/np.pi/self.epsilon_0 
         directionVector, distance = self.distanceCalculator(locationOfInterest)
         electricField=prefactors*self.charge/(distance**2)*directionVector
         return electricField

d = -5e-2
L = 10e-2
Q = 10e-9
numberOfPieces = 10
numberOfPieces2 = 1000000
locationOfPieces = np.linspace(0, L, numberOfPieces)
locationOfPieces2 = np.linspace(0, L, numberOfPieces2)
electricFieldAtP = [0,0,0]
electricFieldAtP2 = [0,0,0]
dq = Q / numberOfPieces
dq2 = Q / numberOfPieces2



for x in locationOfPieces:
    littleChargedParticle = chargedParticle(np.array([x, 0, 0]), dq)

    electricFieldAtP += littleChargedParticle.electricFieldCalculator(np.array([d, 0, 0]))

E1 = electricFieldAtP
print(E1[0])

for x in locationOfPieces2:
    littleChargedParticle = chargedParticle(np.array([x, 0, 0]), dq2)

    electricFieldAtP2 += littleChargedParticle.electricFieldCalculator(np.array([d, 0, 0]))
E2 = electricFieldAtP2
print(E2[0])


absolute = abs(E1[0] - E2[0])
percent_difference = absolute / (E1[0] * 100)
print(percent_difference)

