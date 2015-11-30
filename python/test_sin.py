from math import sin


def tight_loop_slow(iterations):
    """
    >>> %timeit tight_loop_slow(10000000)
    1 loops, best of 3: 2.21 s per loop
    """
    result = 0
    for i in xrange(iterations):
        # this call to sin requires a global lookup
        result += sin(i)
    return result


def tight_loop_fast(iterations):
    """
    >>> %timeit tight_loop_fast(10000000)
    1 loops, best of 3: 2.02 s per loop
    """
    result = 0
    local_sin = sin
    for i in xrange(iterations):
        result += local_sin(i)
    return result


if __name__ == '__main__':
    import time
    
    print "Slow lookup"
    st = time.time()
    tight_loop_slow(10000000)
    print(time.time() - st)
 
    print "Fast Lookup"
    st = time.time()
    tight_loop_fast(10000000)
    print(time.time() - st)
