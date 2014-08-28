# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 22:47:00 2014
@author: samarth
"""


def euclid(m, n):
    """
    Returns GCD of a m and n
       Uses Euclid's algorithm (non-recursive) to find the GCD
    """
    # step 1, check if n > m, if yes, swap them
    if n > m :
        m, n = n, m
    
    # Step 2, if remainder of division of m and n is 0, n is the GCD
    while m % n != 0:
        # Step 3, otherwise, set m <- n and n <- m/n
        r = m % n
        m = n
        n = r        
    return n


def recursive_euclid(m ,n):
    """
    Returns GCD of a m and n
       Uses Euclid's algorithm (recursive) to find the GCD
    """
    if n > m:
        m, n = n, m
    if m == n :
        return m
    return euclid(n, m % n)
    
if __name__ == "__main__":
    # tests
    assert euclid(544, 119) == 17
    assert euclid(119,544) == 17
    assert euclid(544, 544) == 544
    
    assert recursive_euclid(544, 119) == 17
    assert recursive_euclid(119,544) == 17
    assert recursive_euclid(544, 544) == 544