import matplotlib.pyplot as plt 
import numpy as np
from math import*
h=float(input('Enter initial height: '));   #initial value of height
v=float(input('Enter velocity in m/s: '));  #Value of velocity in m/s
r=float(input('Enter angle in degrees: ')); #User input angle in degree but python reads as radian
ax=float(input('Enter x-component of acceleration: ')); #x component of acceleration
ay=float(input('Enter y-component of acceleration: ')); #y component of acceleration

if ay==0: #Condition if x is equal to zero
   print('Vertical acceleration must not be equal to zero') #Prints error when vertical acceleration is 0

d=r*(pi/180) #Angle in radian to degree conversion
totalt=((v*sin(d))+sqrt((v*sin(d))**2+(2*abs(ay)*h)))/abs(ay) #total flight time

t=np.linspace(0,totalt,100) #array containing 100 values from 0 to total time
  
x=(v*cos(d)*t)+(1/2)*(ax)*(t**2) #values of horizontal positions with respect to time ranging from 0 to total time
y=(h+v*sin(d)*t)+(1/2)*(ay)*(t**2) #values of vertical positions with respect to time ranging from 0 to total time

x_ideal=v*cos(d)*t;                         #x-component of ideal motion where ax=0
y_ideal=h+v*sin(d)*t+(1/2)*ay*t**2;        #y-component of ideal motion 

plt.plot(x,y,'r',linewidth=2,label="Non-ideal motion") #plots non ideal motion
plt.plot(x_ideal,y_ideal,'-.b',linewidth=2,label="Ideal motion") #plots ideal motion
plt.xlabel('Horizonal Displacement') #x- axis label
plt.ylabel('Vertical Displacement') #y-axis label
plt.title('Trajectory of Projectile Motion') #Plot title
plt.grid() #Plot grid
plt.legend(loc="best") #Plot legend







