class atom:
    def __init__(self):
        self.offset = 0
    
    def read(self, data, length):
        bytes = data[self.offset:self.offset+length]
        self.offset += length
        return bytes

    def read_8(self, data):
        return self.read(data, 1)

    def read_16(self, data):
        return self.read(data, 2)

    def read_32(self, data):
        return self.read(data, 4)
    
    def read_64(self, data):
        return self.read(data, 8)