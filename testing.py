'''
    On this assignment, you should work with a partner. You must submit what you have completed at the end of the class period, but you do not need to complete any leftover problems for homework. 
 
    For some of these problems you will need to create a class; for others, you will need to use a library. 
    You do NOT need to put all your solutions in this file, however you should keep all your solutions together, clearly labeled with descriptive file names, in one folder. 
'''
 
 
 
 
 
''' 1.
    Create a class, Point, that keeps track of two properties: x and y
    When a point is created, values for x and y should be provided.
 
    The methods for this class are as follows:
    rotate90: rotate the point 90° about the origin
    rotate180: rotate the point 180° about the origin
    rotaten90: rotate -90° about the origin
    translate: given 2 values, translate the point by the given amount.
    flip_horizontally: flip the point on the x-axis
    flip_vertically: flip the point on the y-axis
'''
class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Rotate90(self):
        self.x = y
        self.y = -x

    def Rotate180(self):
        self.x = -x
        self.y = -y

    def RotateNeg90(self):
        self.x = -y
        self.y = x

    def Translate(self,a,b):
        self.x = x+a
        self.y = y+b

    def FlipHor(self):
        self.x = x
        self.y = -y

    def FlipVer(self):
        self.x = -x
        self.y = y
 
 
''' 2.
    Create a class, Bicycle, that keeps track of three properties: cadence, gear, speed. 
    When a Bicycle is created, cadence, gear, and speed are accepted as arguments.
 
    The methods for this class are as follows:
    set_gear: given a value, set the gear to that value
    set_cadence: given a value, set the cadence to that value
    apply_brake: given a value, decrease the speed of the bike by that value
    speed_up: given a value, increase the speed of the bike by that value
'''
 
 class Bicycle():

    def __init__(self, cadence, gear, speed):
        self.cadence = cadence
        self.gear = gear
        self.speed = speed

    def set_gear(self, gear):
        self.gear = gear

    def set_cadence(self, cadence):
        self.cadence = cadence

    def set_brake(self, brake):
        self.speed = speed // brake

bike = Bicycle(90, 4, 60)
bike.set_gear(3)
bike.set_cadence(100)
bike.set_brake(2)
 
 
 
''' 3.
    Create a class, student, that keeps track of four properties: energy, hunger, stress, and hours.
    These properties have a range from 0-100, except hours, which has a range from 0-24. 100 energy means they are energetic; 100 hunger means they are very hungry; 100 stress means they are extremely stressed. When you create a new student, assume they have moderate hunger, low stress, a lot of energy, and 24 hours.
 
    The methods for the student class are as follows:
    study: Given a value (to adjust hours), study for that given length of time. Studying decreases energy and increases hunger based on the length of the study.
    sports: Given a value (to adjust hours), play sports for that given length of time. This decreases energy, increases hunger, and decreases stress based on the length of the sports.
    class: Given a value (to adjust hours), attend classes for a given length of time. This decreases energy, increases hunger, and increases stress based on the length of the class.
    take_test: Given a value (to adjust hours), this increases stress. 
    submit_paper: this decreases stress.
    eat_meal: Given a value (to adjust hours), this decreases stress, decreases hunger, and increases energy.
    sleep: Given a time (to adjust hours), this decreases stress, increases energy, and increases hunger.
    new_day: resets the hours in a day.
 
    You may not let a student do more than 24 hours worth of activities in a given day. 
'''
class Student():
    
    def __init__(self, energy, hunger, stress, hours):
        self.energy = energy
        self.hunger = hunger 
        self.stress = stress
        self.hours = hours

    def Study(self, value):
        self.hours -= value
        self.energy -= 10*value
        self.hunger += 7*value

    def Sports(self, value):
        self.hours -= value
        self.energy -= 15*value
        self.hunger += 14*value
        self.stress -= 5*value

    def Class(self, value):        
        self.hours -= value
        self.energy -= 11*value
        self.hunger += 8*value
        self.stress += 3*value

    def Take_Test(self, value):
        self.hours -= value
        self.stress += 8*value

    def Submit_Paper(self):
        self.stress -= 8*value

    def Eat_Meal(self, value):
        self.hours -= value
        self.energy += 20*value
        self.hunger -= 20*value
        self.stress -= 8*value

    def Sleep(self, value):
        self.hours -= value
        self.energy += 20*value
        self.hunger += 5*value
        self.stress -= 20*value

    def New_Day(self):
        self.hours = 24

    def Check_Student(self):
        if hours == 0:
            print('You are dead')
            break
 
 
''' 4. 
    Use numpy to create an array of numbers going from 20 to 100 by increments of .25
    Then, multiply all the values in the array by 4. 
    Then. find the sum of all the values.
'''
import numpy as np
a = np.arange(20, 100, 0.25)
b = []
for x in range(len(a)):
    b.append(a[x]*4)
print(b)
 
 
 
 
''' 5.
    Use turtle to draw a star.
'''
 
import turtle
turtle.color('red', 'yellow')
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if turtle.abs(pos()) < 1:
        break
turtle.end_fill()
turtle.done()
 
''' 6.
    Use SymPy to determine the area of a triangle given points a, b and c.
'''
 
import sympy as sp
import sympy.geometry as gm

a = gm.Point(1, 1)
b = gm.Point(2, 1)
c = gm.Point(2, 2)
t = gm.Triangle(a,b,c)
print(t.area)

 
 
 
''' 7. 
    Use VPython to build a 3D snowman.
'''
 
 
 
 
''' Sources:
    https://docs.oracle.com/javase/tutorial/java/javaOO/classes.html
'''