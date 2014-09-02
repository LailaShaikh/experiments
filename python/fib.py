def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)


print F(6)
"""
0 + 1 + 2 + 3 + 4 + 5
"""
