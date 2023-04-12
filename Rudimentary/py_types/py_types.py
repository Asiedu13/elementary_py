# Python has 9 categories of data types
"""
Text -> str
Numeric -> int, float, complex
Sequence -> array, range, tuple
Mapping  -> dict
Set  -> set, frozenset
Boolean -> bool
Binary -> bytes, bytearray, memoryview
None -> None
""" 

x = 'Prince'
print(type(x))

x = 3
print(type(x))

x = 3.0
print(type(x))

x = 1j
print(type(x))

x = [1, 2]
print(type(x))

x = (1, 2, 3)
print(type(x))

x = range(6)
print(type(x))

x = {"name": 'Prince', "age": 12}
print(type(x))

x = {1, 2, 3}
print(type(x))

x = frozenset({1, 2, 3})
print(type(x))

x = b'12'
print(x)
print(type(x))

x = bytearray(5)
print(x)
print(type(x))

x = memoryview(bytes(5))
print(x)
print(type(x))

x = None
print(type(x))