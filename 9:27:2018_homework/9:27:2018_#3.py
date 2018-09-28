# Name: Justin Lin
# Date: 9/27/2018
# Description: Generate  a  list  of  100  numbers,  1  to  100,  without  using  a  traditional  looping  technique  (investigate  list  comprehensions).  Shuffle  the  list  up  so  the  numbers  are  not  in  order.  (Ms.  Healey)  
# Source: none

import sys
import math
import random

l = [x+1 for x in range(100)]
random.shuffle(l)


print(l)