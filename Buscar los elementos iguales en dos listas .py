def FindIntersection(strArr):

    # code goes here
    arrays = [arr_string.split(', ') for arr_string in strArr]
    print(arrays)

    intersection = []

    for num in arrays[0]:
        if num in arrays[1]:
            intersection.append(int(num))

    return ','.join([str(n) for n in sorted(intersection)])

# keep this function call here


ase = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]


# keep this function call here
print(FindIntersection(ase))
