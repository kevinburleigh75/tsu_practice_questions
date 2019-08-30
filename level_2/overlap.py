# LEVEL 2:
#   Write a method that takes two lines and returns true if they intersect and false if they don't.  The two lines are horizontal and at the same elevation, same y-value. The method will take four arguments, x1, x2, x3, x4. x1 and x2 form line A. x3 and x4 form line B.
#   Input:
#     x1 = -2,  x2 = -10, x3 = -3,  x4 = -1
#   Output:
#     true

#   Input: x1 = 2, x2 = 12, x3 = 13, x4 = 15
#   Output = false

#   Input: x1 = 100, x2 = 105, x3 = 105, x4 = 107
#   Output = true

#   Input: x1 = 50, x2 = 70, x3 = 60, x4 = 65
#   Output = true
#   You can write your solution in any language you choose. In java, the solution would look like the following:
#   boolean intersects(int x1, x2, x3, x4)  {
#     // your code here
#     // your code here
#   }

def swap(a,b):
    return b,a

def overlap(x1, x2, x3, x4):
    if x1 > x2:
        swap(x1, x2)
    if x3 > x4:
        swap(x3, x4)

    return (x3 <= x1 <= x4) or (x3 <= x2 <= x4) or (x1 <= x3 and x2 >= x4)

if __name__ == '__main__':
    import sys
    x1, x2, x3, x4 = [int(x) for x in sys.argv[1:]]
    print(overlap(x1, x2, x3, x4))
