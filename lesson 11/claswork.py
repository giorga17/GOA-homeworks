# მომხმარებელს შემოატანინეთ input-ით ფულის რაოდენობა.
# თუ ის აღემატება 100-ს მაშინ დავბეჭდოთ, რომ მას გააჩნია
# საკმარისი თანხა. სხვა შემთხვევაში კი დავბეჭდოთ რომ
# საკმარისი თანხა არ აქვს.


money = int(input("enter your money"))
money = 100

if money > 100:
    print("you have enough money,")
else:
    print("you do not have enough money,")

# მომხმარებელს შეეკითხეთ თავისი ასაკი. თუ ის
# აღემატება თვრამეტს გამოიტანეთ, რომ 
# სრულწლოვანია. სხვა შემთხვევაში დაბეჭდეთ რომ არის ბავშვი.



age = int(input("please enteryour age: "))
age = 18 

if age > 18:
    print(" you are 18, ")
else:
    print("you ate chaild")