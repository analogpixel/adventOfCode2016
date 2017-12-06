#!/usr/bin/envpython
#
# https://adventofcode.com/2016/day/1

inp="R4,R1,L2,R1,L1,L1,R1,L5,R1,R5,L2,R3,L3,L4,R4,R4,R3,L5,L1,R5,R3,L4,R1,R5,L1,R3,L2,R3,R1,L4,L1,R1,L1,L5,R1,L2,R2,L3,L5,R1,R5,L1,R188,L3,R2,R52,R5,L3,R79,L1,R5,R186,R2,R1,L3,L5,L2,R2,R4,R5,R5,L5,L4,R5,R3,L4,R4,L4,L4,R5,L4,L3,L1,L4,R1,R2,L5,R3,L4,R3,L3,L5,R1,R1,L3,R2,R1,R2,R2,L4,R5,R1,R3,R2,L2,L2,L1,R2,L1,L3,R5,R1,R4,R5,R2,R2,R4,R4,R1,L3,R4,L2,R2,R1,R3,L5,R5,R2,R5,L1,R2,R4,L1,R5,L3,L3,R1,L4,R2,L2,R1,L1,R4,R3,L2,L3,R3,L2,R1,L4,R5,L1,R5,L2,L1,L5,L2,L5,L2,L4,L2,R3"
#inp="R2,L3"
#inp="R2,R2,R2"
#inp="R5,L5,R5,R3"
#inp="R8,R4,R4,R8"
x=0
y=0
#dirs=['w','n','e','s']
dirs=[(0,-1), (1,0), (0,1), (-1,0)]
d=1
locs = ["0,0"]

for i in inp.split(','):
	if i[0] == 'R':
		d = d + 1
	if i[0] == 'L':
		d = d - 1
	if d > 3:
		d = 0
	if d < 0:
		d = 3

	z = int(i[1:])

	for o in range(0,z):
		x = x + dirs[d][0] 
		y = y + dirs[d][1]
		tmp = "%d,%d" % (x,y)
		if tmp in locs:
			print( "twice:", abs(x) + abs(y))
		locs.append(tmp)

print(x,y, abs(x) + abs(y) )
