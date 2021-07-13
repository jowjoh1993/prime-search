"""
NAME:    sieve_of_eratosthenes.py
AUTHOR:  Joshua Johnstone
PURPOSE: Find all primes up to and including a given integer, n
DATE:    2020-MAY-22

DESCRIPTION:
    Initialize a dict of odd number indexes ranging from 3 up to (and 
    including) n, whose values are all True. 
    
    Iterate through the dictionary. If the current index is True, then we have
    encountered a prime. We then mark all the multiples of the prime as False.
    If the current index is False, go to the next iteration.
    
    For a prime p, all multiples less than p^2 will have already been marked, 
    so we can skip those. Beyond that, we can also skip every second multiple of
    p, since adding an odd number switches the parity (odd+odd=even, and 
    even+odd=odd) and there's no need to mark even numbers.
    
    After the algorithm is finished, all composite numbers will have been 
    marked False, and the remaining numbers marked True will be prime. Return 
    the list of indexes whose values are True (also, sneakily prepend 2, the 
    only even prime, to the list).

"""

# Josh's change 
# Change on the test branch

import time

def soe(n):
    d = {}
    for k in range(3,n+1,2): d[k] = True
    for p, v in d.items():
        if v is False: continue
        for m in range(p**2,n,2*p): d[m] = False
    return [2]+[k for k,v in d.items() if v is True]

# 2 more lines of code, but builds the list of primes along the way. This is
# about 5% faster than soe() on average, since we skip the dict search at the
# end.
def soe2(n):
    d = {}
    l = [2]
    for k in range(3,n+1,2): d[k] = True
    for p, v in d.items():
        if v is False: continue
        l.append(p)
        for m in range(p**2,n,2*p): d[m] = False
    return l


def test_timing(n):
    print(40*'-')
    print("Timing Test")
    print(40*'-')
    print(f"Searching for all primes between 1 and {format(n, '5,.0f')}...")
    
    start = time.time()
    primes = soe2(n)
    
    # Print Results
    print(f"Search took {round(time.time()-start, ndigits=4)} seconds.")
    num = format(len(primes), "5,.0f")
    print(f"Found {num} primes between 1 and {format(n, '5,.0f')}.")    

def test_timing_compare(n, ntrials):
    print(40*'-')
    print("Timing Comparison Test")
    print(40*'-')
    soe_times = []
    soe2_times = []
    for i in range(ntrials):
        print(f"Running trial {i+1} of {ntrials}...")
        start = time.time()   
        primes = soe(n)
        soe_times.append(round(time.time()-start,ndigits=4))
    
        start = time.time()   
        primes = soe2(n)
        soe2_times.append(round(time.time()-start,ndigits=4))
    
    soe_time = sum(soe_times)/len(soe_times)
    soe2_time = sum(soe2_times)/len(soe2_times)
    improvement = round(100*(soe_time-soe2_time)/soe_time, ndigits=3)
    
    # Print Results    
    print(f"On average, soe2 was {improvement}% faster than soe.")    

# Test the algorithm
if __name__=='__main__':
    test_timing(int(1e7))
    #test_timing_compare(int(1e6), 30)
