from bidirectional_list import BList

v = BList([0,3,2,1,0],[1,2,3], print_format='number')
print(v)
v[8] = 8
print(v)
v[8] = 0
v[-4] = 4
print(v)