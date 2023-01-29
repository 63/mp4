from mp4.atom import atom

class ftyp(atom):
    def __init__(self):
        atom.__init__(self)
        self.major_brand = ''
        self.major_brand_version = 0
        self.compatible_brands = []

    def parse_atom(self, data):
        if len(data) < 8:
            return
        self.major_brand = self.read_32(data).decode('utf-8')
        self.major_brand_version = int.from_bytes(self.read_32(data), 'big')
        for i in range(8, len(data), 4):
            self.compatible_brands.append(self.read_32(data).decode('utf-8'))

    def __str__(self):
        return f'ftyp: major_brand={self.major_brand} major_brand_version={self.major_brand_version} compatible_brands={self.compatible_brands}'
