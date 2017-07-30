

from enum import Enum, unique
@unique
class PartType(Enum):
    Hole=0
    A=1
    B=2
@unique
class Neighbs(Enum):
    Xup=0
    Xdown=1
    Yup=2
    Ydown=3
    Zup=4
    Zdown=5
@unique
class BondState(Enum):
    Free=0
    Bonded=1



class Particle(object):
    """defines a particle capable of complex interactions with the lattice neighbors
       ported from .C
       //     For now HB's, One Donor, One Acceptor per particle,
       //     Structureless
       //     We do not mind where they are relative to each other
       //     May be neighbor's info to add later for speed up?  
       //     For HB's also add the HB patterns (monomer structure) for different 
       //       types  
       Copyright M.Kotelyanskii 
       7/30/2017 Just constructor and SetType
    """

    def __init__(self,partType=PartType.Hole,x=0,y=0,z=0,donor=Neighbs.Xdown,
                 acceptor=Neighbs.Xup,donorbond=BondState.Free,acceptorbond=BondState.Free):
        super().__init__()
        self.X=x
        self.Y=y
        self.Z=z
        self.DonorBond=donor
        self.AcceptorBond=acceptor
        self.DonorBond=donorbond
        self.AcceptorBond=acceptorbond
        self.Type=partType
        self.Neighbor=[]


    def SetType(self,Typetobe):
        self.Type=Typetobe;     
        print('SetType call\n')


if __name__ == "__main__":
    apa=Particle()
    print('apa.Type  ', str(apa.Type))
    apa.SetType(PartType.A)
    print('apa.Type ',  str(apa.Type))


 