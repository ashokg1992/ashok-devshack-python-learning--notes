# print('hello world')

#-------------------------------------------------------------- data type -----------------------------------------------------------#

# list= [] we denote  like this, we use list- when we want to change data at any time
# tuple= () we denote like this, we use tuple - when we  do not want to change data at any time
#dictiionary {} ; {'a':'10'  , 'b': '20'}  if we want to use specific key at any time, then we use dictionary
#set  {}      we use set-  when we want to avoid duplicate data 

#--------------------------------#
# a=10       # int
# b=20.5     # float
# c=a+b
# print (c)

#--------------------------------#
# a= "ashok"
# b= "kumar"
# c= "g'akr"
# d=a+b+c
# print (d)

#--------------------------------------------------------------sring data type -----------------------------------------------------------#

# a= "ashok1"
# b=  'ashok2'
# c= '''
#    ashok
#    kumar
#    reddy'''
# d= a+b+c
# print (d)

#---------------------------------------------------------  boolean  string type---------------------------------------------------------#
#true
#false
#----------------------------------------------------------- list data type--------------------------------------------------------#

# list is collectin if items.
# items can be different data types in list. even boolean  type also.

#list is mutable.it  mean we can change values for items in list.
#a=[1,8,9,2,8,2,8,2]
#a[0]=7, i can also change this value at any time in list

#--------------------------------------------------------------tuple data type    ---------------------------------------------------------#

# it is immutable, once we enter data we can  not change data .
#a=(1,8,9,2,8,2,8,2)
#a[0]=7, i can not  change this value at any time in tuple
# list= [] we denote  like this, we use list- when we want to change data at any time
# tuple= () we denote like this, we use tuple - when we  do not want to change data at any time
#dictiionary {} ; {'a':'10'  , 'b': '20'}  if we want to use specific key at any time, then we use dictionary
#set  {}      we use set-  when we want to avoid duplicate data 

#--------------------------------------- dictionary data type--------------------------------------------------------#

# in dictionary each item is in form or key and value format
# a= {'first:ashok','second:kumar', 'thired:reddy'}   # we dont get o/p as expected
# a= {'first':'ashok','second':'kumar', 'thired':'reddy'}
# #print (a)
# print(a['first'])

#--------------------------------------- set  data type--------------------------------------------------------#

# it does not print duplicate items 
# a= {1,1,2,2,3,4,5,6,7,7,8,}
# print (a)


#---------------------------------------  arithamtic scenario  ------------------------------------------------------#
# x = 5
# y = 3

# # Arithmetic operations
# sum_result = x + y
# difference_result = x - y
# product_result = x * y
# division_result = x / y

# print ( 'addition= ', sum_result , 'diff=', difference_result , 'product=', product_result , 'div=' , division_result )

#---------------------------------------list example   ------------------------------------------------------#

# namelist=['ashok', 'kumar', 'reddy', 'gorantla']
# print (namelist)
# print (namelist[0])
# namelist[0]='gorantla'   # here we updated 0 index and changed
# print (namelist)     # it o/p is updated with 0 index value


#--------------------------------------- tuple  example   ------------------------------------------------------#


# namelist=('ashok', 'kumar', 'reddy', 'gorantla')
# print (namelist)
# print (namelist[0]) 
# # namelist[0]='gorantla'   # here we updated 0 index and changed
# # print (namelist)     # it o/p is updated with 0 index value


#--------------------------------------- List manipulation (append, remove  ) ------------------------------------------------------#
# list_var = [1, 2, 3, 4, 5]
# list_var.append(6)
# list_var.remove(2)
# print("Modified List:", list_var)
# # o/p is Modified List: [1, 3, 4, 5, 6]

#----------------- --------   Dictionary operations  --- -------------------#
# dict_var = {'a': 1, 'b': 2, 'c': 3}
# dict_var['d'] = 4
# del dict_var['a']
# print("Modified Dictionary:", dict_var)


# --------------------  Set operations----------------- --------------------#
# set_var = {1, 2, 3, 4, 5}
# set_var.add(6) 
# set_var.remove(3)
# print("Modified Set:", set_var)
# o/p is Modified Set: {1, 2, 4, 5, 6}
 
#================================= File Handling  =================================

# file=open('ashok.txt', 'r')  # it just  read file but not open, to open this file we do this as belkow
# content=file.read() # wee storing data in "content" variable and  - read file and store data , () tells it store data 
# print (content)
# file.close()    # to close read mode    


# file=open('ashok.txt', 'r')
# firstline=file.readline()  # to read first line of data only
# print(firstline)

# file=open('ashok.txt', 'r')
# firstline=file.readlines()   # to read all lines of data in file - in form of "LIST"
# print(firstline)
#file.close()
# O/P : ['hi ashok1\n', 'ashok2\n', 'ashok3\n', 'ashok4\n', 'ashok5\n', 'ashok6\n', 'ashok7\n', 'ashok8\n']


#WRITING DATA IN FILE IN 2 WAYS:
#--------------------------------------
# 1.WRITE MODE 2. APPEND MODE
   
# file=open('ashok.txt', 'r')
# file=open('ashok.txt','w')  # we enable to write data in file
# file.write("i am ashok  adding new data\n")    # THIS DATA IS ADDED AND OLD DATA IS DELETED
# content=file.read()
# print(content)
#file.close()
# WRITE MODE DELETE ALL DATA IN OLD FILE AND ENTER THE NEW DATA,  .


 #------------------ #appending data-------------------------
# file=open('ashok.txt', 'r')
# # file=open('ashok.txt', 'w')
# file=open('ashok.txt','a') 
# file.write("\nadded append line\n")
# content=file.read()
# print(content)
# file.close()

#-----------------------------  -----------------------------


