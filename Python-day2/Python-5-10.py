#!/usr/bin/env python3

mySet = set('ATGTGGG')
mySet2 = {'ATGCCT'}

print("mySet\n", mySet)
print("mySet2\n", mySet2)

Set_A = {'3', '14', '15', '9', '26', '5', '35', '9'}
Set_B = {'60', '22', '14', '0', '9'}

print("Intersection", Set_A & Set_B)
print("Difference", Set_A - Set_B)
print("Union", Set_A | Set_B)
print("Symmentrical Difference", Set_A ^ Set_B)

