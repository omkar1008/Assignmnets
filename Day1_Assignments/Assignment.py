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
print(smallest)


list1 = [1, 4, 10, 30, 60, 70, 80, 100]
list1.pop(2)
count = 0
index = 0
for each in list1:
    if count == 1:
        index = count
        list1.pop(index)
        index = count + 2
    count = count + 1

print(list1)

list1 = [1, 4, 10, 30, 60, 70, 80 , 100] #delete_index_list = [7, 3, 4] .Delete using pop
index_list = [7, 3, 4]
for each in index_list:
    list1.pop(each)

print(list1)