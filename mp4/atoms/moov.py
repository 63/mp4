from mp4 import mp4
from mp4.atom import atom
from mp4.atoms import trak

class moov(atom):
    def __init__(self):
        atom.__init__(self)
        self.trak = []

    def parse_atom(self, data):
        if len(data) < 8:
            return
        atoms = mp4.read_atoms(data)
        for atom in atoms:
            if atom.name == 'trak':
                trak_atom = trak.trak()
                trak_atom.parse_atom(atom.data)
                self.trak.append(trak_atom)
    
    def __str__ (self):
        return f'moov: trak={self.trak}'