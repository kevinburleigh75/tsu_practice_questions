# LEVEL 1:
#   Write a method that takes an integer argument, 'length', and prints out a square of x's where the sides are 'length' long.
#   You can write your solution in any language you choose. In java, the solution would look like the following:
#     void printSquare (int length)  {
#       // your code here
#       // your code here
#     }

def draw_square(side_length):
    # for rr in range(side_length):
    #     xs = ''.join(['x' for _ in range(side_length)])
    #     print(xs)

    for rr in range(side_length):
        for cc in range(side_length):
            print('x', end='')
        print('')


if __name__ == '__main__':
    import sys
    draw_square(int(sys.argv[1]))
