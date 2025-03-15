import matplotlib.pyplot as plotter
import numpy as np
from matplotlib.patches import Circle

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

    def electricPotentialforPlotting(self, plottingX, plottingY):
        prefactors = 1/4/np.pi/self.epsilon_0
        distance = np.sqrt((plottingX - self.location[0])**2+(plottingY-self.location[1])**2)
        electricPotential = prefactors*self.charge/distance
        return electricPotential

    def electricFieldPlotting(self, plottingX, plottingY):
        prefactors = 1/4/np.pi/self.epsilon_0
        distancesquared = (plottingX - self.location[0])**2+(plottingY-self.location[1])**2

        eX, eY = prefactors*self.charge*(plottingX-self.location[0]) / distancesquared, \
                prefactors*self.charge*(plottingY-self.location[1])/distancesquared
        return eX, eY


nx=100 #Number of x points
ny=100 #Number of y points
x=np.linspace(-1,1,nx)
y=np.linspace(-1,1,ny)
#This creates a mesh on which we have all possible combinations of x and y values in the x-y plane.
#See figure to visualize mesh
X,Y =np.meshgrid(x,y)
#Same procedure as before, let's make a bunch of little charges along the half ring.
#Please do not go over 100 charges. You will overload the computers memory.
R=10e-2
numberOfPieces=100
Q=5e-9
xLocationsOnRing=R*np.cos(np.linspace(np.pi/2,-np.pi/2,numberOfPieces))
yLocationsOnRing=R*np.sin(np.linspace(np.pi/2,-np.pi/2,numberOfPieces))
dq=Q/numberOfPieces
#In order to plot in 2-D we have to create the Electric Field for all points in the x-y plane.
#Same for the potential
#We have to create objects that can hold all the Ex, Ey, and potential,
# values, which is what we are doing here.
Ex,Ey = np.zeros((ny,nx)), np.zeros((ny,nx))
potential=np.zeros((ny,nx))
#Now we're telling python we're going to make a figure
fig = plotter.figure()
#Now we're telling python to make two subplots inside that figure. One for the E field
#the other for the potential. The "121" means create a figure with 1 row, 2 columns, and this is
#the first subplot.
#Similarly the "122" means make a second figure at the second column in the same figure
#with 1 row and 2 columns
plot1 = fig.add_subplot(121)
plot2 = fig.add_subplot(122)
#These are just two colors in written for positive, red, and negative, blue.
#Don't worry too much about this line
charge_colors = {True: '#aa0000', False: '#0000aa'}
#Now we make our charges
for x,y in zip(xLocationsOnRing,yLocationsOnRing):
    littleChargedParticle=chargedParticle(np.array([x,y]),dq)
    #Now we calculate the electric field at all points in x and y for our Electric Field Plot
    #for this little charge. NOTE THAT THESE ARE CAPITAL X AND Y aka our meshes.
    ex,ey=littleChargedParticle.electricFieldPlotting(X,Y)
    #Add them to the total electric field
    Ex+=ex
    Ey+=ey
    #Same for the potential.
    potential+=littleChargedParticle.electricPotentialforPlotting(X,Y)
    #These two lines actually draw our charges as little circles on our two plots.
    #with the appropriate colors.
    plot1.add_artist(Circle(littleChargedParticle.location, 0.01, \
    color=charge_colors[littleChargedParticle.charge>0]))
    plot2.add_artist(Circle(littleChargedParticle.location, 0.01, \
    color=charge_colors[littleChargedParticle.charge>0]))
#This line just sets the colors for our electric field lines. Don't worry too much about it.
color = np.log(np.sqrt(Ex**2 + Ey**2))
#Plot the electric field at all X,Y with all the Ex and Ey components. The rest of the code
#are just statements to make the plot prettier. They are called options.
plot1.streamplot(X, Y, Ex, Ey, color=color, linewidth=1, cmap=plotter.cm.inferno,\
density=3, arrowstyle='->', arrowsize=1)
#Plot the potential with the appropriate colormap and levels. We are creating equipotential lines
#in this plot. Darker lines mean lower potential.
plot2.contour(X,Y,potential,1000,levels=np.linspace(np.min(potential),\
np.max(potential)*0.1,1000),cmap=plotter.cm.inferno,linewidth=1,density=3)
#Label your two plots and set the x and y values for the axes.
plot1.set_title('Electric Field')
plot1.set_xlabel('$x$')
plot1.set_ylabel('$y$')
plot1.set_xlim(-1,1)
plot1.set_ylim(-1,1)
plot1.set_aspect('equal')
plot2.set_title('Potential')
plot2.set_xlabel('$x$')
plot2.set_ylabel('$y$')
plot2.set_xlim(-1,1)
plot2.set_ylim(-1,1)
plot2.set_aspect('equal')
plotter.show()

# The graph looks like what we expected when potential goes down the further we get away from the ring. The calculations for the center of the ring is the same as well. The E-field is a large negative component in the x-direction and the graph will point it to the left with respect to the center.
