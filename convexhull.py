# Chris Collander
# October 2019
# Convex Hull graphic demonstration
# Algorithm from Chapter 1 of Computational Geometry by Mark de Berg

from graphics import *
from operator import attrgetter
import time

NUM_POINTS = 50

# Used for the algorithm. Essentially tests the sign of the determinant of this 3x3 matrix
# | 1 A.x A.y |
# | 1 C.x C.y |
# | 1 B.x B.y |
def is_not_right_turn(A,B,C):
	left = C.x*B.y + A.x*C.y + A.y*B.x
	right = C.y*B.x + A.x*B.y + A.y*C.x
	return left>=right

win = GraphWin("Convex Hull", 800, 600)

points = []

# User input for points
for i in range(NUM_POINTS):
	temp_point = win.getMouse()
	temp_point.draw(win)
	points.append(temp_point)
	print(f"{i+1}/{NUM_POINTS}:\t({temp_point.x},{temp_point.y})")

# Sort points, lexographically
points = sorted(points, key=attrgetter('x', 'y'))

# Upper
Lu = [points[0], points[1]]
for i in range(2, len(points)):
	Lu.append(points[i])
	while len(Lu)>2 and is_not_right_turn(Lu[-3], Lu[-2], Lu[-1]):
		del Lu[-2]

# Lower
Ll = [points[-1],points[-2]]
for i in range(len(points)-3,-1,-1):
	Ll.append(points[i])
	while len(Ll)>2 and is_not_right_turn(Ll[-3], Ll[-2], Ll[-1]):
		del Ll[-2]
L = Lu + Ll[1:-1:1]
print(L)

# Show edges
for i in range(len(L)-1):
	line = Line(L[i],L[i+1])
	line.setWidth(1)
	line.draw(win)
	time.sleep(0.5)
line = Line(L[0],L[-1])
line.setWidth(1)
line.draw(win)

win.getMouse() # pause for click in window
win.close()