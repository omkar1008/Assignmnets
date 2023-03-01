# 1.Find largest/second largest /Smallest-
list1= [10,1,2,3,4,5,13,14,15,6,7,8,9,11,12,16]
largest = 0
secondlargest = 0
smallest = list1[0]

for each in list1:
     if each > largest:
       secondlargest = largest
       largest = each
     elif each > secondlargest and each != largest:
         secondlargest = each
         temp = secondlargest
     if each < smallest:
         smallest = each

print(largest)
print(secondlargest)
print(smallest, '\n')

#.Remove 2nd occurrence of 1 using pop
list1 = [1, 2, 1, 1, 4, 5]
count = 0
counter = 0
for each in list1:
    counter += 1
    if each == 1:
        count += 1
    if count == 2:
        counter -= 1
        list1.pop(counter)
        break

print(list1, '\n')

#delete_index_list = [7, 3, 4] .Delete using pop
list1 = [1, 4, 10, 30, 60, 70, 80 , 100]
index_list = [3, 7, 4]
index_list.sort(reverse=True)
for each in index_list:
    list1.pop(each)

print(list1)