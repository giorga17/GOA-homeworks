#  1) დაწერეთ პროგრამა, რომელიც ეკითხება მომხმარებლის ასაკს 
#  და შემდეგ დაბეჭდავს შეტყობინებას ასაკის მიხედვით: using(if-elif-else)

#  If the age is less than 18, print "You are a minor."
#  If the age is between 18 and 65, print "You are an adult."
#   If the age is 65 or older, print "You are a senior citizen."

# age = int(input("please enter your age"))

# if age < 18:
#     print("you are minor")
# elif age >= 18 and age < 65:
#     print("you are adult")
# else:
#     print("you are old")

#  2) შექმენით პროგრამა რომელიც მომხმარებელს შეეკიტხება 
#  რიცხვს და შემდეგ დაუბეჭდოს ის რიცხვი ლუწია თუ კენტია

# for i in range(5):
#     number = int(input("please enter your namber"))
#     if number % 2 == 0:
#         print(number,"is iven")
#     else:
#         print(number,"is odd")


#  3) დაწერეთ პროგრამა რომელიც თხოვს მომხმარებელს  
#  შეიყვანოს ქულები ასოებით ( A,B,C,D or F):
#  და შემდეგ დაბეწდოს ყველა შეტყობინება ასოების
#  მიხედვით.


# grade = input("please enter grad (A, B, C, D OR F): ")

# if grade == "A":
#     print("Exselent")
# elif grade == "B":
#     print("good job")
# elif grade == "C":
#     print("you pusd")
# elif grade == "D":
#     print("you can do better")
# else:
#     print("you faild")



# 4) დაწერეთ პროგრამა რომელიც ბეჭდავს 
# რიცხვებს 1-დან 10-მდე.

# num = 1 
# while num < 10:
#     print(num)
#     num = num + 1

# 5) შექმენით პროგრამა რომელიც ტხოვს მომხმარებელს 
# გამოიცნოს რიცხვი 1-დან 10-მდე.


# guess = 9
# number = int(input("please enter same namber "))
# if number == 9:
#     print("good ")
# else:
#     print("you failed")


num = 4 

number = int(input("please enter number (1-10): "))
while number != num:
    number = int(input("please enter number (1-10): "))
















