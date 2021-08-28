#list1=[["Pradip", 5],["Anaya",10],["Aniket",15]]
#dict1=dict(list1)
#for item in dict1:
 #   print (item)
#for item, lollypop in list1:
 #   print(item,lollypop)


Items = [int, float, "Pradip", 56, 27, 78, 5, 3, 4, 78 ]
for item in Items:
    if str(item).isnumeric() and item>=6:
         print(item)
