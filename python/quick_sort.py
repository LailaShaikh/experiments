def quicksort(lst):
    "Quicksort over a list-like sequence"
    if len(lst) == 0:
        return lst
    pivot = lst[0]
    pivots = [x for x in lst if x == pivot]
    print pivot, pivots, lst
    small = quicksort([x for x in lst if x < pivot])
    large = quicksort([x for x in lst if x > pivot])
    print "--", small, large
    return small + pivots + large


if __name__ == '__main__':
    print quicksort([3,1,2,45,21,12,23,0])
