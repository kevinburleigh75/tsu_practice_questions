# LEVEL 4:
#   Container with the most water.
#   Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

#   Note: You may not slant the container and n is at least 2.

#   Input: [1,8,6,2,5,4,8,3,7]
#   Output: 49

#   Hint: The horizontal width of the container matters. That is why the answer is height x width, 7 x 7 and not 8 x 5.

def water(levels):
    memo = {}
    water_inner(levels, 0, len(levels)-1, memo)
    print('memo has {} entries'.format(len(memo)))
    return memo[(0,len(levels)-1)]

def water_inner(levels, lo, hi, memo):
    if (lo,hi) not in memo:
        if lo >= hi:
            best = 0
        else:
            v_1 = (hi-lo)*min(levels[lo], levels[hi])
            if levels[lo] < levels[hi]:
                v_2 = water_inner(levels, lo+1, hi, memo)
            else:
                v_2 = water_inner(levels, lo, hi-1, memo)
            best = max(v_1, v_2)
        memo[(lo,hi)] = best

    return memo[(lo,hi)]

if __name__ == '__main__':
    import sys
    print(water([int(x) for x in sys.argv[1:]]))
