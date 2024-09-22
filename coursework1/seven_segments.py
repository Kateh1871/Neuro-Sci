from math import *
import numpy as np

# probably for systems that don't support fancy UNICODE characters
fancy=False

def seven_segment(pattern):
    # deciding which characters to write with
    # \ is a linebreak. Lines 11, 12, 13 are actually one line
    global fancy
    left,lower,right = \
        ('▕','__','▏') if fancy else \
        ('|','__','|')
    def vert(d1,d2,d3):
        print(
        (left  if d1 else " ")+
        (lower if d3 else "  ")+
        (right if d2 else " "))
    
    # actually printing the characters now
    bits = [(ai==1) for ai in pattern]
    # prints the first, top horizontal
    print(" "+lower+" " if bits[0] else "   ")
    # prints the second row, 2 verticals and central horizontal
    vert(*bits[1:4])
    # prints the third, bottom row
    vert(*bits[4:7])

    # calculates the number from the final 4 bits of the vector
    number=0
    for i in range(0,4):
        # if the bit is positive, perform the binary -> base 10 calculation
        if bits[7+i]:
            number+=pow(2,i)
    # convert the number to hexadecimal ('%X') and print to console
    print('%X'%int(number))

# Characters 0-9, a-f stored in a 7, 4 vector (16 hexadecimal digits)
# First 7 digits correspond to vertices top to bottom, horizontals are 0,3,6
# Last 4 digits are the number represented in  kind-of-binary
# *2-1 maps [0, 1] -> [-1, 1]
hexdigits = np.int8([\
    [1,1,1,0,1,1,1, 0,0,0,0],
    [0,0,1,0,0,1,0, 1,0,0,0],
    [1,0,1,1,1,0,1, 0,1,0,0],
    [1,0,1,1,0,1,1, 1,1,0,0],
    [0,1,1,1,0,1,0, 0,0,1,0],
    [1,1,0,1,0,1,1, 1,0,1,0],
    [1,1,0,1,1,1,1, 0,1,1,0],
    [1,0,1,0,0,1,0, 1,1,1,0],
    [1,1,1,1,1,1,1, 0,0,0,1],
    [1,1,1,1,0,1,1, 1,0,0,1],
    [1,1,1,1,1,1,0, 0,1,0,1],
    [0,1,0,1,1,1,1, 1,1,0,1],
    [1,1,0,0,1,0,1, 0,0,1,1],
    [0,0,1,1,1,1,1, 1,0,1,1],
    [1,1,0,1,1,0,1, 0,1,1,1],
    [1,1,0,1,1,0,0, 1,1,1,1]])*2-1

# stores each of the above vectors into a names variable for ease when calling
zero, one, two, three, four, five, six, seven, eight, nine, hexA, hexB, hexC, hexD, hexE, hexF = hexdigits

# ???
test1 = np.int8([1,-1,1,1,-1,1,1,-1,-1,-1,-1])
test2 = np.int8([1,1,1,1,1,1,1,-1,-1,-1,-1])

if __name__=="__main__":
    # displays all characters (idk why)
    for d in hexdigits: seven_segment(d)
    
    # displays character 1, 3, 6 (idk why again)
    seven_segment(three)
    seven_segment(six)
    seven_segment(one)
    
    # displays 2 test characters (obviously 3 & 8)
    print("test1")
    seven_segment(test1)
    print("test2")
    seven_segment(test2)




