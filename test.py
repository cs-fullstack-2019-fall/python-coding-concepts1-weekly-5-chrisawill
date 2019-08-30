### Problem 1:
# Ask a user for the year they were born by calculating their age. Assuming they already had their birthday and it’s 2019 print “You are [AGE] years old”
# user = int(input("What year were you born in?"))
# age = 2019 - user
# print(f"You are {age} years old.")
#
# ### Problem 2:
# # Ask the user for a string. If they enter “Kenn”, “Kevin”, “Erin”, or “Autumn” print “Hello Teacher”. Otherwise print “Hello Student”
# #My arrray and input
# teacherNames = ["kenn", "kevin", "Erin", "Autumn"]
# user = input("Enter a string. press q to quit- ")
# # for eachelemt in teacherNames:
# #     print(eachelemt)
# if user != "q":
#     if user == teacherNames[0]:
#         print("Hello teacher!")
#     elif user == teacherNames[1]:
#         print("Hello teacher!")
#     elif user == teacherNames[2]:
#         print("Hello teacher!")
#     elif user == teacherNames[3]:
#         print("Hello teacher!")
#     else:
#         print("Hello student")
#




# ### Problem 3:
# Ask the user for a negative number. Print from 7 down to the user's negative number. You must include the user's number.
# user = int(input("Enter a negative number- "))
# for num in user:
#     range(7, num, -1)
# print(num)
#
#





# ### Problem 4:
# Ask the user to enter a number between -10 to -5. If their input is not between the two numbers ask them to do it again until they get it right. Afterward they print the correct number, print "Good job"
#
# user = int(input("Enter a number between -10 to -5: "))
# while user == str(""):
#     if user <= -5 and >= -10:

# ### Problem 5:
# Create the list: squad = ["One", "Two", "Three", "Four", "Five"]. Print the list in reverse without using a list method.
# squad = ["One", "Two", "Three", "Four", "Five"]
# for eachElemnt in squad:
#         print(eachElemnt[])
#

# ### Problem 6:
# Create a function that will have the string firstName as a parameter. In the function ask the user for their last name. Print "Hello [FIRST & LAST NAME]" in the function. Call that function
# def main():
#     fName = input("Enter first name: ")
#     lname = input("enter last name: ")
#     prob()
# def prob():
#    print(fName)
# main()
#
#
# ### Problem 7:
# Create the class Books with name, rating, genre, and author properties/attributes. Create a class method that will change the rating of the book. Outside of the class, create three objects of the class Book and put them in an array. Lastly, USING THE ARRAY print only the names of the books using any method we’ve learned in class.
# class Books:
#     def __init__(self,name, rating, genre, author):
#         self.name = name
#         self.rating = rating
#         self.genre = genre
#         self.author = author
#
#     def bookchange(self):
#         book2[0] = self.name
#
#
# book1 = Books[("A good book", "5", "scifi", "Gee Rils")]
# book2 = [Books("RITE", "3", "Romance", "Doe Gane")]
# book3 = [Books("Dawn", "4", "Bio", "Dawn Rivers")]
# #
# for eachelement in book1:
#       print(eachelement)
#

# ### Problem
# Create a function that asks the user to enter a number. If the number is between and include -50 and 5, return "Funds too low". If the number is between 5 and 50, return “You should add more funds.” If the number is more than 50, return “Just enough.”
# def main():
#     user = int(input("Enter funds: "))
#     if user >= -50 and <= 5:
#         prob()
#     elif user >= 5 and <= 50:
#       prob2
#     else:
#         prob3
# def prob():
#     print("Funds too low")
# def prob2():
#     print("You should add more funds")
# def prob3():
#     print("just enough")
#main()


# ### Problem 9:
# Ask the user for a positive number. Create an empty array and starting from zero, add each number by 1 into the array. Print EACH ELEMENT of the array.
useer = int(input("Enter a positive number"))
myArray = []
for eachelement in myArray:
    range(0, useer, +1) go


# ### Problem 10:
# Create a new empty array called pet_list. Create a Pet class with a type and breed attribute/property. Include a method that will print each attribute/property. Add 3 pet objects to the pet_list array. Print the attributes/properties for each pet.