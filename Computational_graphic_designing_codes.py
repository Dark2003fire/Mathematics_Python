from sympy import*

#Q1)
x = Point(0,0)
y = Point(2,2)
z = Point(-1,1)
w = Point(3,4)
print(x.distance(y))
print(y.distance(w))
print(x.distance(z))

#OUTPUT:-->
"""
2*sqrt(2)
sqrt(5)
sqrt(2)

""" 
#Q2)

x = Point(0,0)
y = Point(2,2)
z = Point(-1,1)
print(Point.is_collinear(x,y,z))

#OUTPUT:-->
"""

2*sqrt(2)
sqrt(5)
sqrt(2)
False

"""

#Q3)

x = Point(0,0,0)
y = Point(2,2,2)
z = Point(-1,-1,-1)
w = Point(3,4,-7)
print(Point.are_coplanar(x ,y , z, w))

#OUTPUT:-->
"""
2*sqrt(2)
sqrt(5)
sqrt(2)
False
True

"""




from sympy import*
from math import*

#Q1)Reflect the given Points through respective Lines
#1)
x, y = symbols('x y')
P = Point(3,6)
print(P.reflect(Line(x+y)))

#OUTPUT:-->
"""
Point2D(-6, -3)

"""
#2)
x , y = symbols('x y')
P = Point(2,6)
print(P.reflect(Line(2*x+y+1)))

#OUTPUT:-->
"""
Point2D(-34/5, 8/5)

"""

#2)

x , y = symbols('x y')
P = Point(0,2)
print(P.reflect(Line(x+y-5)))

#OUTPUT:-->
"""
Point2D(3, 5)

"""

#4)

x , y = symbols('x y')
P  = Point(1.5,3.6)
print(P.reflect(Line(x-2*y-1)))

#OUTPUT:-->
"""
Point2D(209/50, -44/25)

"""

#5)
x , y = symbols('x y')
P = Point(-5,-6)
print(P.reflect(Line(-4*x+3*y-11)))

#OUTPUT:-->
"""
Point2D(-197/25, -96/25)

"""

#Q2) Reflect  the Point [3,6] through the line x-2y +4=0
x ,y = symbols('x y')
P = Point(3,6)
print(P.reflect(Line(x-2*y+4)))

#OUTPUT:-->
"""
Point2D(5, 2)

"""
#Q3) Apply each of the following transformation on the Point
# P = [4,3]

#1)
P = Point(4,3)
print(P.transform(Matrix([[-1,0,0],
                          [0,1,0],
                          [0,0,1]])))

#OUTPUT:-->
"""
Point2D(-4, 3)

"""
#2)
P = Point(4,3)
print(P.reflect(Line(3*x+4*y-5)))

#OUTPUT:-->
"""
Point2D(-14/25, -77/25)

"""
#3)
P = Point(4,3)
print(P.scale(3,0))

#OUTPUT:-->
"""
Point2D(12, 0)

"""
#4)
P = Point(4,3)
print(P.scale(0,3.2))

#OUTPUT:-->
"""
Point2D(0, 48/5)

"""
#5)
P = Point(4,3)
print(P.transform(Matrix([[0,-1,0],
                          [-1,0,0],
                          [0,0,1]])))

#OUTPUT:-->
"""

Point2D(-3, -4)

"""
#6)
P = Point(4,3)
print(P.scale(0,3))

#OUTPUT:-->
"""
Point2D(0, 9)

"""

#7)
P = Point(4,3)
print(P.scale(3/2,2))

#OUTPUT:-->
"""
Point2D(6, 6)

"""
#8)
P = Point(4,3)
print(P.transform(Matrix([[1,-3,0],
                          [1,1,0],
                          [0,0,1]])))

#OUTPUT:-->
"""
Point2D(7, -9)

"""

#9)
P= Point(4,3)
angle = radians(48)
print(P.rotate(angle))

#OUTPUT:-->
"""
Point2D(1788351796013/4000000000000, 99599422419723/20000000000000)

"""



from sympy import*
from math import*


#Q1)
L1  = Line(Point(0,0) ,Point(0,3))
L2 = Line(Point(0,0) ,Point(0,1))
print(L1.angle_between(L2))

#OUTPUT:-->
"""
0

"""

#Q2)
L = Line(Point(0,8),Point(8,0))
S = Segment(Point(0,0),Point(10,10))
print(L.intersection(S))

#OUTPUT:-->
"""
[Point2D(4, 4)]

"""

#Q3)
L = Point(0,3)
M = Point(3,0)
N = Point(10,10)
print(L.length)
print(M.length)
print(N.length)

#OUTPUT:-->
"""
0
0
0

"""

#Q4)
L = Line(Point(0,0) ,Point(2,4))
print(L.slope)

#OUTPUT:-->
"""
2

"""
#Q5)
S = Segment(Point(1,0) , Point(2,-1))
print(S.midpoint)

#OUTPUT:-->

Point2D(3/2, -1/2)


#Q6)
x ,y = symbols('x y')
L = Line(x+y-5)
print(L.points)

#OUTPUT:-->
"""
Point2D(0,5)
Point2D(1,4)

"""

#Q7)

L = Line(Point(0,0) ,Point(0,1))
print(L.rotate(pi/6))
l1 = L.rotate(pi/6)
print(l1.equation())

#OUTPUT:-->

"""
Point2D(3/2, -1/2)
Line2D(Point2D(0, 0), Point2D(-1/2, 866025403784439/1000000000000000))
-866025403784439*x/1000000000000000 - y/2
"""

#Q8)

S = Segment(Point(1,0) ,Point(2,-1))
print(S.rotate(pi))

#OUTPUT:-->
"""
Segment2D(Point2D
(-1, 24492935982947/200000000000000000000000000000), Point2D(-2, 1))

"""

#Q9)
R = Ray(Point(0,0) , Point(4,4))
print(R.rotate(pi/2))

#OUTPUT:-->
"""
Ray2D(Point2D(0, 0), Point2D(-4, 4))

"""

#Q10)
R = Ray(Point(0,0) ,Point(4,4))
print(R.rotate(pi))

#OUTPUT:-->
"""
Ray2D(Point2D(0, 0), Point2D(-4, -4))
"""

#Q11)
x ,y = symbols('x y')
L = Line(4*x+3*y-5)
L1 = Line(x+y)
Line = L.reflect(L1)
print(Line.equation())

#OUTPUT:-->
"""
 x +4y/3 +5/3
"""

#Q12)

P = Point(2,3)
Q = Point(4,6)
S = Segment(P, Q)
x ,y = symbols('x y')
L = Line(7*x+6*y-3)
print(S.reflect(L))

#OUTPUT:-->
"""
Segment2D(Point2D(-236/65 ,93/85) ,
          Point2D(-514/85 ,-222/85))

"""

#Q13)

P = Point(0,0)
Q = Point(2,4)
R = Ray(P ,Q)
x ,y = symbols('x y')
L = Line(x-2+y-3)
print(R,reflect(L))

#OUTPUT:-->
"""
Ray2D(Point2D(6/5  , -12/5) ,Point2D(28/5 ,16/5))


"""

#14)

A = Point(1,1)
B = Point(5,5)
print(A.rotate(pi/2))
print(B.rotate(pi/2))

#OUTPUT:-->
"""
Point2D(-1, 1)
Point2D(-5, 5)

"""

#Q15)

A = Point(2,5)
B = Point(4,-13)
A1 = A.transform(Matrix([[2,3,0],
                         [4,1,0],
                         [0,0,1]]))
B1 = B.transform(Matrix([2,3,0],
                        [4,1,0],
                        [0,0,1]]))
S = Segment(A1 , B1)
print(S.midpoint)
print(S.slope)

#OUTPUT:-->
"""
Point2D(-10,5)



"""
#Q16)
x ,y = symbols('x y')
l = Line(2*x-y-5)
l1 = Line(2*x-y-5)
l2 = Line(x*3*Y+1)
P = l1.intersection
P = P[0]
P.transform(matrix([[-2,3,0],
                    [1,1,0],
                    [0,0,7]))


#OUTPUT:-->
"""

Point2D(-5,5)

"""

#Q17)
x ,y = symbols('x y')
l = Line(2*x-y-5)
points = l.points
p = points[0]
q = points[1]

p1= p.transfer(Matrix([[1,-3,0] ,
                       [2,1,0],
                       [0,0,1]]))
q1 = q.transfer(Matrix([[1,-3,0],
                        [2,1,0],
                        [0,0,1]]))

l1 = Line(p1 , q1)
print(l1.equation())

#OUTPUT:-->
"""


x/4+y/2-1/2


"""





"""


 
"""
from pulp import*

#1)

model= LpProblem(name = "Maximization Problem" ,sense = -1)
x = LpVariable(name = "x" ,lowBound = 0)
y = LpVariable(name = "y" ,lowBound = 0)

model += (4*x+6*y<=24)
model += (5*x+3*y<=15)

model += 150*x+75*y
print(model)
print(model.solve())
print(model.objective.value())
print(x.value())
print(y.value())


#OUTPUT:--->
"""
Maximization_Problem:
MAXIMIZE
150*x + 75*y + 0
SUBJECT TO
_C1: 4 x + 6 y <= 24

_C2: 5 x + 3 y <= 15

VARIABLES
x Continuous
y Continuous

1
450.0
3.0
0.0

"""

#2)

model = LpProblem(name = "Maximization Problem" ,sense = -1)
x = LpVariable(name = "x" , lowBound = 0)
y = LpVariable(name = "y" , lowBound = 0)
z = LpVariable(name = "z"  ,lowBound = 0)

model += (2*x+3*y<=8)
model += (2*y+5*z<=10)
model += (3*x+2*y+4*z<=15)


model += 3*x+5*y+4*z

print(model)
print(model.solve())
print(model.objective.value())
print(x.value)
print(y.value)
print(z.value)

#OUTPUT:-->
"""

Maximization_Problem:
MAXIMIZE
3*x + 5*y + 4*z + 0
SUBJECT TO
_C1: 2 x + 3 y <= 8

_C2: 2 y + 5 z <= 10

_C3: 3 x + 2 y + 4 z <= 15

VARIABLES
x Continuous
y Continuous
z Continuous

1
18.658536500000004

<bound method LpVariable.value of x>
<bound method LpVariable.value of y>
<bound method LpVariable.value of z>

"""

#3)

model = LpProblem(name = "Maximization Prolem" , sense = -1)
x = LpVariable(name = "x" , lowBound = 0)
y = LpVariable(name = "y"  , lowBound = 0)
z = LpVariable(name = "z" , lowBound = 0)
w = LpVariable(name = "w" , lowBound = 0)

model += (4*x+6*y-5*z-4*w >=-20)
model += (-3*x-2*y+4*z+w <=10)
model +=(-8*x-3*y+3*z+2*w <=20)

model += (4*x + y+ 3*z +5*w)

print(model)
print(model.solve())
print(model.objective.value())
print(x.value)
print(y.value)
print(z.value)
print(w.value)

#OUTPUT:--->
"""

Maximization_Prolem:
MAXIMIZE
5*w + 4*x + 1*y + 3*z + 0
SUBJECT TO
_C1: - 4 w + 4 x + 6 y - 5 z >= -20

_C2: w - 3 x - 2 y + 4 z <= 10

_C3: 2 w - 8 x - 3 y + 3 z <= 20

VARIABLES
w Continuous
x Continuous
y Continuous
z Continuous

-2
25.0
<bound method LpVariable.value of x>
<bound method LpVariable.value of y>
<bound method LpVariable.value of z>
<bound method LpVariable.value of w>


"""

#4)


model= LpProblem(name = "Minimization Problem" ,sense = 1)
x = LpVariable(name = "x" ,lowBound = 0)
y = LpVariable(name = "y" ,lowBound = 0)

model += (x>=4)
model += (y<=2)

model += 3.5*x+2*y
print(model)
print(model.solve())
print(model.objective.value())
print(x.value())
print(y.value())

#OUTPUT:--->

"""
Minimization_Problem:
MINIMIZE
3.5*x + 2*y + 0.0
SUBJECT TO
_C1: x >= 4

_C2: y <= 2

VARIABLES
x Continuous
y Continuous

1
14.0
4.0
0.0

"""

#5)
model = LpProblem(name = "Minimization Problem" ,sense = 1)
x = LpVariable(name = "x" , lowBound = 0)
y = LpVariable(name = "y" , lowBound = 0)
z = LpVariable(name = "z"  ,lowBound = 0)

model += (x+y*1/2+z*1/2<=1)
model += (3/2*x+2*y+z>=8)




model += x+2*y+z

print(model)
print(model.solve())
print(model.objective.value())
print(x.value)
print(y.value)
print(z.value)


#OUTPUT:---->

"""

Minimization_Problem:
MINIMIZE
1*x + 2*y + 1*z + 0
SUBJECT TO
_C1: x + 0.5 y + 0.5 z <= 1

_C2: 1.5 x + 2 y + z >= 8

VARIABLES
x Continuous
y Continuous
z Continuous

-1
8.8
<bound method LpVariable.value of x>
<bound method LpVariable.value of y>
<bound method LpVariable.value of z>

"""

#6)


model= LpProblem(name = "Minimization Problem" ,sense = 1)
x = LpVariable(name = "x" ,lowBound = 0)
y = LpVariable(name = "y" ,lowBound = 0)

model += (x>=6)
model += (y>=6)
model += (x+y<=11)


model += x+y
print(model)
print(model.solve())
print(model.objective.value())
print(x.value())
print(y.value())

#OUTPUT:------>

"""


Minimization_Problem:
MINIMIZE
1*x + 1*y + 0
SUBJECT TO
_C1: x >= 6

_C2: y >= 6

_C3: x + y <= 11

VARIABLES
x Continuous
y Continuous

-1
12.0
6.0
6.0

"""







































