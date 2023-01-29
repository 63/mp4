from mp4.atom import atom

class tkhd(atom):
    def __init__(self):
        atom.__init__(self)
        self.version = 0
        self.flags = 0
        self.created = 0
        self.modified = 0
        self.track_id = 0
        self.duration = 0
        self.layer = 0
        self.alternate = 0
        self.volume = 0.0
        self.matrix = [0x00010000, 0, 0, 0, 0x00010000, 0, 0, 0, 0x40000000]
        self.width = 0.0
        self.height = 0.0

    def parse_atom(self, data):
        if len(data) < 8:
            return
        self.version = int.from_bytes(self.read_8(data), 'big')
        self.flags = int.from_bytes(self.read(data, 3), 'big')
        if self.version == 0:
            self.created = int.from_bytes(self.read_32(data), 'big')
            self.modified = int.from_bytes(self.read_32(data), 'big')
            self.track_id = int.from_bytes(self.read_32(data), 'big')
            self.read_32(data) # reserved
            self.duration = int.from_bytes(self.read_32(data), 'big')
        elif self.version == 1:
            self.created = int.from_bytes(self.read_64(data), 'big')
            self.modified = int.from_bytes(self.read_64(data), 'big')
            self.track_id = int.from_bytes(self.read_32(data), 'big')
            self.read_32(data) # reserved
            self.duration = int.from_bytes(self.read_64(data), 'big')
        self.read_64(data) # reserved
        self.layer = int.from_bytes(self.read_16(data), 'big')
        self.alternate = int.from_bytes(self.read_16(data), 'big')
        self.volume = int.from_bytes(self.read_16(data), 'big')
        self.read_16(data) # reserved
        self.matrix = [
            self.read_32(data).hex(),
            self.read_32(data).hex(),
            self.read_32(data).hex(),
            self.read_32(data).hex(),
            self.read_32(data).hex(),
            self.read_32(data).hex(),
            self.read_32(data).hex(),
            self.read_32(data).hex(),
            self.read_32(data).hex(),
        ]
        self.width = int.from_bytes(self.read_32(data), 'big') / 65536
        self.height = int.from_bytes(self.read_32(data), 'big') / 65536

    def __str__ (self):
        return f'tkhd: version={self.version} flags={self.flags} created={self.created} modified={self.modified} track_id={self.track_id} duration={self.duration} layer={self.layer} alternate={self.alternate} volume={self.volume} matrix={self.matrix} width={self.width} height={self.height}'