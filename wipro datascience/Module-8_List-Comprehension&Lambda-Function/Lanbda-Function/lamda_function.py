#1)cubes every number in the given list list_1 = [1,2,3,4,5,6,7,8,9] using lambda function 
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

cubed_list = list(map(lambda x: x**3, list))

print(cubed_list)