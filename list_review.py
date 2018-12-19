''' Instructions:
   Work with a partner to complete these tasks. Complete as many as you can. Assume that all variables/lists are declared and initialized (unless you are specifically asked to create/initialize a list); you need only write the code using the variables/lists indicated in the description. Write your solution below the commented description.
'''
 
''' 1. 
   Create a list of ints, faveNums, that holds 3 integers.
'''
 
 
 
''' 2. 
   Create a list of Strings, holidays, that holds 14 holidays.  
'''
 
holidays = ["memorial day", "Independance day", "Labour Day", "D day", "New years", "columbus day", "easter", "Christmas", "Thanksgiving", "MLK day", "President's day", "Veteran's day", "Chinese New Year", "Hanukkah"]
 
''' 3. 
   Create a list of characters, grades, that holds 5 letter grades.
'''
 

 
''' 4. 
   Create a list of booleans, funny, the can keep track of whether 18 things are funny or not. 
'''
 
funny = [True, True, True, False, True, True, False, False, False, False, False, False, True, False, False, True, True, False]

 
''' 5. 
   Create a list of doubles, salaries, that holds the salaries of all the employees at a university. The number of employees is stored in the int numEmployees.
'''
 
 
 
''' 6. 
   A picture's dimensions are stored in integer variables x and y. Create a single list of integers that can store the grayscale value for each pixel in the list.
'''

from PIL import Image as i
dimensions = []
for y in range(h):
   for x in range(w):
      r,g,b = H.getpixel((x,y))
      dimensions.append(r,g,b)

 
''' 7. 
   In a class, each student has 0, 1, 2 or 3 siblings. The numbers of students with no siblings is stored in the variable noSiblings, the number of students with one sibling is stored in the variable oneSibling, the number of students with two siblings is stored in the variable twoSiblings, and the number of students with three siblings is stored in the variable threeSiblings. Create a list that holds all the names of the students in the class, as well as the names of all their siblings.
'''
 
 
 
''' 8. 
   Create a list that holds all the months in the year. (No loop.)
'''
 
 months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
 
''' 9. 
   Create a list that holds all the days of the week. (No loop.)
'''
 
 
 
''' 10. 
   Create a list that holds all the possible values for boolean variables. (No loop.)
'''
 
boolean = [0,1,False,True]
 
''' 11. 
   Create a list that holds the names of all the 3rd form dorms on campus. (No loop.)
'''
 
 
 
''' 12.  
   Create a list that holds 3 random numbers with values between 0 and 1. (Loop optional.)
'''
import random as r
for x in range(3):
  r.uniform(0,1)

 
''' 13. 
   Create a list that will represent a deck of cards. Some example data for cards would be AS (ace of spaces), 5H (5 of hearts), JC (jack of clubs), 9D (9 diamonds). (Loop required.) 
'''
 
 
 
''' 14. 
   Write a Yahtzee program that simulates the rolling of five dice and prints "Yahtzee" if all five dice are the same; otherwise it should print "Try again."
'''
import random as r
while False:
   Yahtzee = input("Roll a Yahtzee!!! ")
   if Yahtzee.lower() == yes:
      rolled = []
      a = 0
      for x in range(5):
         rolled.append(r.randint(1,7))
         if rolled[0] == rolled[x]:
            a += 1
         else:
            a = 0
      if a == 5:
         break
         print("Yahtzee")
      else:
         print("try again")
   elif Yahtzee.lower() == no:
      break

 
''' 15. 
   In a list, specials are numbers in a list that have an even number before them, an odd number behind them, and they themselves are divisible by 3. Given a list of ints called numbers, print out the location in the list of the specials, as well as the value in front of them, their value, and the value behind them. For example:
   position 4: 14, 9, 25
'''
 
 
 
''' 16. 
   Write a program to search for the "saddle points" in a 5 by 5 list of integers. A saddle point is a cell whose value is greater than or equal to any in its row, and less than or equal to any in its column. There may be more than one saddle point in the list. Print out the coordinates of any saddle points your program finds. Print out "No saddle points" if there are none.
'''
 
import random as r
saddle = [[r.randint(0,2)]*5 for x in range(5)]
print(saddle)
saddle_point = 0
saddle_point2 = 0
saddle_cell = 0
saddle_cell2 = 0
real_saddle = 0
for y in range(5):
   for x in range(5):
      for z in range(5):
         if z == 0:
            saddle_point = 0
            saddle_point2 = 0 
            saddle_cell = 0
            saddle_cell2 = 0
         if saddle[x][y] >= saddle[x][z]:
            saddle_point += 1
            if saddle_point == 5:
               saddle_cell +=1
         if saddle[x][y] <= saddle[z][y]:
            saddle_point2 += 1
            if saddle_point2 == 5:
               saddle_cell2 += 1
         if saddle_cell == 1 and saddle_cell2 == 1:
            real_saddle += 1

 
''' 17. 
   In the game of chess, a queen can attack pieces which are on the same row, column, or diagonal. A chessboard can be represented by an 8 by 8 list. A 1 in the list represents a queen on the corresponding square, and a O in the list represents an unoccupied square. Given the two locations for queens (row1, col1, row2, col2), place the queens in the 2D list, chessboard. Then process the board and indicate whether or not the two queens are positioned so that they attack each other. 
'''
 

 
''' 18. 
   Given a list, write code that will reverse the order of the elements in the list. For example, dog, cat, bunny should become bunny, cat, dog.
'''
 
lst = ["dog", "cat", "bunny"]
reverse = []
for x in range(1, len(lst)+1):
   # reverse += lst[-x]
   reverse.append(lst[-x])

 
''' 19. 
   Given a list, doorknobs, that holds strings, swap the elements at positions 1 and 3, if possible.
'''
 
 
 
''' 20. 
   In a list of ints called numbers, find the largest number in the list and place it at the end of the list.
'''
 
numbers = [1,5,4,2,3]
a = 0
b = 0
for x in range(len(numbers)):
   if a <= numbers[x]:
      a = numbers[x]
      b = x
numbers += [numbers.pop(b)]

 
''' 21. 
   In a 2D list with dimensions w by h, filled with random numbers from from 1 to 100, replace every odd number with either 2 or 22; 2 if the number was a single digit number, 22 if the number was a 2-digit number. 
'''
 
 
 
''' 22. 
   In a 2D list with dimensions w by h, holding grayscale values for an image, adjust the colors so the image is inverted. All light portions should be dark, all dark portions should be light. A value of 200 should be 5, a value of 100 should be 155, etc. Remember, there are 256 levels for color, including 0.
'''

from PIL import Image as i 
w,h=512,512
H = i.new("RGB", (w,h))
# grid_size = [[0]*w for x in range(h)]
for x in range(img_sizex):
   for y in range(img_sizey):
      r,g,b = H.getpixel((x,y))
      average_rgb = ((r+g+b)//3)
      average_rgb_inverted = 255-((r+g+b)//3)
      H.putpixel((x,y),(average_rgb_inverted,average_rgb_inverted,average_rgb_inverted))
H.show("x", "PNG")

 
''' 23.
   In a list, shifters, holding ints, shift all elements forward 1 position. For example, position 2 should move to position 1, position 1 to position 0, and position 0 to the end of the list (etc.)
'''
 
 
 
''' 24. 
   Given an N-by-N grid of elevation values (in meters), a peak is a grid point for which all four neighboring cells are strictly lower. Write a code fragment that counts the number of peaks in a given N-by-N grid.
'''
 
grid_size = [[0]*(N+1) for x in range(N+1)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
peak=0
h = []
for y in range(1,len(grid_size[0])-1):
   for x in range (1, len(grid_size)-1):
         for a in range(4):
            if grid_size[y+dy[a]][x+dx[a]] < grid_size[x][y]:
               h.append(x,y)
      if (x,y) not in h:
         peak += 1


 
''' 25. 
   90% of incoming college students rate themselves as above average. Write some code that, given a list of student rankings (stored in integer list rankings), prints the fraction of values that are strictly above the average value.
'''
 

 
''' 26. 
   Given a 9-by-9 list of integers between 1 and 9, check if it is a valid solution to a Sudoku puzzle: each row, column, and block should contain the 9 integers exactly once.
'''

for y in range(len(Sudoku[0])):
   for x in range(len(Sudoku)):
      for z in range(9):
         if len(Sudoku) == 9 and len(Sudoku[0]) == 9:
            if Sudoku[x][y] != Sudoku[x][z] and Sudoku[x][y] != Sudoku[z][y]:
               a = 0
               a += 1
            if a == 1296:
               if Sudoku[x][y]
                  print("True")


 
'''
    27. Create a list of 100 numbers between 1 and 10 (inclusive), create a new list whose first value is the number of 1s in the original list, whose 2nd value is the number of 2s in the original list, and so on. Average the number of occurences of each number in the list over 100 repetitions. Average the averages. Print the result to the screen.
'''
 
 
 
''' Sources
   http://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html
   http://introcs.cs.princeton.edu/java/14array/
'''