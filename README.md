# MP4

Simple MP4 file atom parser in python

## Example

```python
from mp4 import mp4

with open('example.mp4', 'rb') as file:
    data = file.read()

mp4 = mp4.parse_mp4(data)
print(mp4.ftyp)
```

## TODO

- Add more atoms
- Writing atoms
