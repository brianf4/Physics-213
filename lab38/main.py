import numpy as np

class chargedParticle():
    #Properties of all Charged Particles (Class Properties)
    elementaryCharge=1.60e-19
    epsilon_0=8.85e-12


    #Charged Particle Initializer 
    def __init__(self, location, charge) -> None:
        self.location=location
        self.charge=charge

    #Functions associated with charged particles
    def chargeNumberCalculator(self):
        chargeNumber=self.charge/self.elementaryCharge
        return chargeNumber

    def distanceCalculator(self, locationOfInterest):
        distanceVector=locationOfInterest-self.location
        distance=np.linalg.norm(distanceVector)
        #Calculates the magnitude of a vector
        directionVector=distanceVector/distance
        return directionVector, distance

    def electricFieldCalculator(self, locationOfInterest):
        prefactors=1/4/np.pi/self.epsilon_0
        directionVector, distance = self.distanceCalculator(locationOfInterest)
        electricField=prefactors*self.charge/(distance**2)*directionVector
        return electricField
        
        
#Exercise 38.1
origin=np.array([0,0,0])
electron=chargedParticle(origin, -1.60e-19)
print(electron.location)


#Exercise 38.2
origin2=np.array([0,0,1])
proton=chargedParticle(origin2, 1.60e-19)
print(proton.charge)
print(proton.location)

#Exercise 38.3
print(electron.chargeNumberCalculator())
print(proton.chargeNumberCalculator())

print(electron.electricFieldCalculator([2,0,0]))

#Exercise 38.4


#Charge distribution 1
location1 = np.array([0.05, 0, 0])
location2 = np.array([0.15, 0, 0])
q1=chargedParticle(location1, 1e-9)
q2=chargedParticle(location2, 1e-9)

totaEfield = q1.electricFieldCalculator([0,0,0]) + q2.electricFieldCalculator([0,0,0])

print(f"Charge Distrubution 1: {totaEfield}")


#Charge distribution 2
cd2_location1 = np.array([0.05, 0, 0])
cd2_location2 = np.array([0.10, 0, 0])
cd2_location3 = np.array([0.15, 0, 0])
cd2_q1=chargedParticle(cd2_location1, 1e-9)
cd2_q2=chargedParticle(cd2_location2, 1e-9)
cd2_q3=chargedParticle(cd2_location3, 1e-9)

cd2_totaEfield = cd2_q1.electricFieldCalculator([0,0,0]) + cd2_q2.electricFieldCalculator([0,0,0]) + cd2_q3.electricFieldCalculator([0,0,0])


print(f"Charge Distrubution 2: {cd2_totaEfield}")



#Charge distribution 4
cd3_location1 = np.array([-0.05, -0.05, 0])
cd3_location2 = np.array([0.05, -0.05, 0])
cd3_q1=chargedParticle(cd3_location1, 1e-9)
cd3_q2=chargedParticle(cd3_location2, 1e-9)

cd3_totaEfield = cd3_q1.electricFieldCalculator([0,0,0]) + cd3_q2.electricFieldCalculator([0,0,0]) 

print(f"Charge Distrubution 3: {cd3_totaEfield}")

#Charge distribution 4
cd4_location1 = np.array([-0.05, -0.05, 0])
cd4_location2 = np.array([0.05, -0.05, 0])
cd4_location3 = np.array([0, -0.05, 0])
cd4_q1=chargedParticle(cd4_location1, 1e-9)
cd4_q2=chargedParticle(cd4_location2, 1e-9)
cd4_q3=chargedParticle(cd4_location3, 1e-9)

cd4_totaEfield = cd4_q1.electricFieldCalculator([0,0,0]) + cd4_q2.electricFieldCalculator([0,0,0]) + cd4_q3.electricFieldCalculator([0,0,0])

print(f"Charge Distrubution 4: {cd4_totaEfield}")
