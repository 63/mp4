from mp4.atoms import ftyp, moov

class MP4:
    def __init__(self):
        self.ftyp = ftyp.ftyp()
        self.moov = moov.moov()

class atom_container:
    def __init__(self, size, name, data):
        self.size = size
        self.name = name
        self.data = data

def read_atom(data, offset):
    size = int.from_bytes(data[offset:offset+4], byteorder='big')
    name = data[offset+4:offset+8].decode('utf-8')
    data = data[offset+8:size]
    return atom_container(size, name, data)

def read_atoms(data):
    atoms = []
    offset = 0
    while offset < len(data):
        atom = read_atom(data, offset)
        atoms.append(atom)
        offset += atom.size
    return atoms

def parse_mp4(data):
    mp4 = MP4()
    atoms = read_atoms(data)
    for atom in atoms:
        if atom.name == 'ftyp':
            mp4.ftyp.parse_atom(atom.data)
        elif atom.name == 'moov':
            mp4.moov.parse_atom(atom.data)
    return mp4