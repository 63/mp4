from mp4 import mp4

class trak:
    def __init__(self):
        self.tkhd = ''

    def parse_atom(self, data):
        if len(data) < 8:
            return
        atoms = mp4.read_atoms(data, 0, len(data))
        for atom in atoms:
            print(atom.name)
    
    def __str__ (self):
        return f'trak: traks={self.traks}'