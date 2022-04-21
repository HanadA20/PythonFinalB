#4. Create a list of names using 5 strings.
#Use a for loop and the enumerate function to
#iterate through the elements and display each
#element’s index and value.


#I will not accept any questions about
#what you need to do about this final after Sunday, March 6.
#If you need to ask questions or need clarification about this
#part of the final, do before then.

names = ["Michael", "Lebron", "Kobe", "Durant", "Melo"]

for index, names in enumerate(names):
    print(index, names)
    
    for i in enumerate(names):
        print(i)
