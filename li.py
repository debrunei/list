color_list = ["Red", "Green", "Blue", "Yellow"]
print(color_list[0])
print(color_list[-1])
slice_list = color_list[1:2+1]
print(slice_list)

num_list = [4, 6, 4, 2, 9, 4, 1]
num_list.append(5)
print(num_list)
num_list.remove(4)
print(num_list)
print(num_list.count(4))
print(num_list.index(9))

fruit_list = ["Apple", "Banana", "Cherry"]

fruit_list[1] = ("Orange")
print(fruit_list)
fruit_list.pop()
print(fruit_list)