#unordered list 
#syntax

dict_name = {
    "Key" : "value",
    "key1" : "value1"
}
print(dict_name)

student = {
    'Fname' : 'James', #string
    'Sname' : 'Bond', #string
    'Tel' : 8508447, #integer
    'Shoes' : ['Fila', 'Airmax' , 'Dior'], #list
    'Male' : True

}
print(student)

#ACCESSING ITEMS IN THE DICTIONARY
#1 Using the get keys and values method

x = student.keys()#using key
print(x)

x = student.values()
print(x)


# 2 USING THE KEY NAMES AND VALUES
x = student['Fname']
print(x)


##CHECKING IF  KEY EXISTS IN A DICT
if "Shoes" in student:
    print('The student has shoes')
else:
    print('No shoes')


##CHANGING/Updating ITEMS IN THE DIC
#you change the value by reffring to a key

student['Fname'] = 'Bill' #this changes the value of key 'Fname' from 'james' to 'Bill'
print(student)

## 2. updating Using the  the update() method


##adding item to the dict

student['Age'] = 19
print(student)


#removing items from dict- 4 methids: pop(), popitem(), del and clear()

student.pop('Sname')
print(student)
student.popitem()
print(student)
del student['Tel']
print(student)
student.clear()
print(student)


##looops in a dict
student = {
    'Fname' : 'James', #string
    'Sname' : 'Bond', #string
    'Tel' : 8508447, #integer
    'Shoes' : ['Fila', 'Airmax' , 'Dior'], #list
    'Male' : True

}

for x in student:
    print(x)

for x in student.values():
    print ( '\n' + str(x) )

for x , y in student.items():
    
    print('\nKey: ' + str(x) + '\nValue: ' + str(y) + '\n')

###NESTED DICTIONARIES- Dictionary inside a dictionary

zetech = {

    'bscit' : {
        'Department' : 'Engineering',
        'population' : 200,
        'Ongoing?' : True
    }

   

    
}