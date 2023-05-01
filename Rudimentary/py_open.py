
f = open('./py_open.py', 'r')

nf = open('../get-pip.py')
print(f)

# Reading the file

# print(f.read())

# Reading a line with readline()
# print(f.readline())

# Loop through the file line by line
for x in f:
    print(x)

print()
print(nf.readline())

print('Using the loop now')

for y in range(6):
    print(nf.readline())
    
f.close()
nf.close()