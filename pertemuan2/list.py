#list muttable
#list memiliki index
#memiliki fungsi len()
#bisa memiliki tipe data yg berbeda dalam satu himpunan

thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#negative indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#check if item exists
thislist = ["apple", "banana", "cherry"]
#contoh lain
print("apple" in thislist)

if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#insert items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#cherry bakali pindah ke indeks ke tiga, karna watermelon jd 2\

#remove specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#contoh lain
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#dia bakal ngehapus banana yg pertama aja
#jadi dia ngecek indeks pertama, trus kedua, ketemu banana kan, nah selesai. dia ga ngecek ke blkg lg

#ngehapus spesifik indeks
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#keyword del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#clear the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

""" loop list """
thislist = ["apple", "banana", "cherry"]
for x in thislist:      #untuk setiap x di thislist
  print(x)

#Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

  #versi pendeknya (dari yg diatas)
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#perhatiin iindentasinya


"""You can set the outcome to whatever you like:

Example
Set all values in the new list to 'hello': """
newlist = ['hello' +x for x in fruits]

#Customize Sort Function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc) #diurutkan dr yg terkecil atw selisihnya paling dekat ke 50
print(thislist)

