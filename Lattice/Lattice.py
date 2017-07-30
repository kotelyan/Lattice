from Particle import *
import random

class Lattice(object):
   """defines a square 2D Lattice of Particle's type A and B and H(holes) 
       Copyright M.Kotelyanskii 
       7/30/2017 - just set up a 2D rectangular PBC grid and flip particles at random, no interactions
   """
   def __init__(self,x_size=2,y_size=2,x_h=1,x_A=0,):
        self.X_size=x_size
        self.Y_size=y_size
        self.x_H=x_h
        self.x_A=x_A
        self.x_B=1-self.x_H-self.x_A
        self.Grid=[[Particle(x=col,y=row) for col in range(self.X_size)] for row in range(self.Y_size)]


if __name__=="__main__":
    la=Lattice()
    apa=la.Grid[0][0]
    print('la(0,0)',str(la.Grid[0][0].Type))
    la.Grid[1][0].SetType(PartType.B)
    print('la(0,0)',str(la.Grid[0][0].Type))
    print('la(1,0)',la.Grid[1][0].Type)
    print('apa value +1',apa.Type.value+3)
    
    
    


