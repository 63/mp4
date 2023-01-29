from mp4 import mp4
from mp4.atom import atom
from mp4.atoms import tkhd

class trak(atom):
    def __init__(self):
        atom.__init__(self)
        self.tkhd = tkhd.tkhd()

    def parse_atom(self, data):
        if len(data) < 8:
            return
        atoms = mp4.read_atoms(data)
        for atom in atoms:
            if atom.name == 'tkhd':
                self.tkhd.parse_atom(atom.data)
            else:
                #print(atom.name)
                pass
    
    def __str__ (self):
        return f'trak: tkhd={self.tkhd}'