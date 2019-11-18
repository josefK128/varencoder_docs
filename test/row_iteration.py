# row_iteration.py
# test matrix-row operations (for VAE variation.py)


import numpy as np


def distance(a, b):
    if len(a) != len(b):
        print('\n' + str(a) + ' and ' + str(b) + ' have different lengths')
        return None

    print('\n\ndistance: find d(a,b) where a = ' + str(a) + '; b = ' + str(b))
    v = np.subtract(a,b)
    print('\nel diffs = ' + str(v))
    v = np.square(v)
    print('\ndiffs squared = ' + str(v))
    sum = np.sum(v)
    print('\nsum diffs-sqd = ' + str(sum))
    d = np.sqrt([sum])
    print('\nsqrt sum sqd-diffs is d = ' + str(d))
    return d
        


def action():

    m = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

    rows = {}
    i = 0
    for row in m:
      print(str(row))
      rows[i] = row
      i += 1

    print('\n\nrows =' + str(rows))

    print('\naction received d = ' + str(distance(rows[0],rows[1])))
    distance([1,2], [2,3,4])


action()
                 
