print("Welcome to the food Chatbot")
name = input("What is your name? ")
age = int(input(f"Hello {name}, How old are you? " ))

if age < 15:
    print(f"Welcome {name}, Ur {age} years old?. Oh you super duper young! Anyway, how may I help you today?")
elif 15 <= age < 18:
    print(f"Welcome {name}, Ur {age} years old?. Oh you entering in the big leagues now! Anyway, how may I help you today?")
elif 18 <= age < 55:
    print(f"Welcome {name}, Ur {age} years old?. There you are all nice and grown up! Anyway, how may I help you today?")
elif 55 <= age < 100:
    print(f"Welcome {name}, Ur {age} years old?. Well dang, Keep that health in shape! Anyway, how may I help you today?")
elif  age > 100:
    print(f"Welcome {name}, Ur {age} years old?. Wow, ur defo dead or ur superhuman! Anyway, how may I help you today?")
else:
    print("invalid age")



