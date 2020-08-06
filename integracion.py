from sympy import Symbol
from sympy import integrate
from scipy.integrate import tplquad
from math import pi
from math import e

Z=Symbol('Z')
a=Symbol('a')
fi=Symbol('fi')
teta=Symbol('teta')
r=Symbol('r')
g= (1/( 81*(3*pi)**(1/2) ))  *  ( (Z/a)**(3/2) ) * (27-18*(Z*r/a)+2*((Z**2)*(r**2)/(a**2))) * (e**((-Z*r)/(3*a)))  
print( integrate( integrate(integrate(g,fi),teta),r)     )





