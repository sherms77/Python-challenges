def find_smallest_num(lst):
    return min(lst)

# test cases
print(find_smallest_num([34, 15, 88, 2]), 2)
print(find_smallest_num([34, -345, -1, 100]), -345)
print(find_smallest_num([-76, 1.345, 1, 0]), -76)
print(find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999]), -0.9999)
print(find_smallest_num([7, 7, 7]), 7)
print(find_smallest_num([4, 6, 1, 3, 4, 5, 5, 1]), 1)
print(find_smallest_num([-4, -6, -8, -1]), -8)
print(find_smallest_num([54, 76, 23, 54]), 23)
print(find_smallest_num([100]), 100)
print(find_smallest_num([0, 1, 2, 3, 4, 5]), 0)

# all work

