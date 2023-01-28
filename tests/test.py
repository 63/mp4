import sys
sys.path.append('../')

from mp4 import mp4

with open('files/example.mp4', 'rb') as file:
    data = file.read()

mp4 = mp4.parse_mp4(data)
print(mp4.ftyp)