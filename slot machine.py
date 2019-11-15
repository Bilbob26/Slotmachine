import  random
again="y"
while again==("y"):
    slot1=random.randint(0,8)
    slot2=random.randint(0,8)
    slot3=random.randint(0,8)
    fruit=["cherry","banana","coins","strawberry","orange","lemon","bar","potatoe","tomatoe"]
    print(fruit[slot1])
    print(fruit[slot2])
    print(fruit[slot3])
    if slot1==slot2:
        
        print("you got a reward")
        
    elif slot1==slot3:
        
        print("you got a reward")
    elif slot3==slot2:
        
        print("you got a reward")
    elif slot1==slot2 and slot1==slot3:
        
        print("you got a big reward")
    else:
        print("you got nothing")
    again=input("want to go again? :  y/n")
        
