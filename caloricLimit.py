
#func
def caloricLimit(body_weight, activity):
    try:
        body_weight = float(body_weight)
    
    except ValueError:
        print("invalid input. Please enter a valid decimal number.")
        return None

    if activity == "sedentary":
        activity = 12
    elif activity == "moderate":
        activity = 15.5
    elif activity == "active":
        activity = 19
    else:
        activity = input("re-enter a activity level.")

    return body_weight * activity

def remaining_cals(limit):
    
    remainder = limit
    while True:
        try:
            meal1 = int(input("Enter calories in meal 1: "))
            break
        except ValueError:
           print("Ivalid input! Please enter a number.")
    
    while True:
        try:
            meal2 = int(input(("Enter calories in meal 2: ")))
            break
        except ValueError:
           print("Ivalid input! Please enter a number.")
    
    while True:
        try:
            meal3 = int(input("Enter calories in meal 2: "))
            break
        except ValueError:
           print("Ivalid input! Please enter a number.")

    total_meals = meal1 + meal2 + meal3
    remainder = limit - total_meals
    return remainder


body_weight = input("What is your weight in kg: ")
activity = input("What is your activity level (sedentary, moderate, active): ")
limit = caloricLimit(body_weight, activity)
print(limit)
remainder = (remaining_cals(limit))
print(remainder)

if remainder < 0:
    over = remainder
    print(f"You hit your caloric intake! You are over by {over}")

elif remainder == limit:
    print(f"You have reacher your limit! do not eat any more calories today")
else:
    print(f"You still have {remainder} calories remaining today.")


def multiply(x=2, y): 
    return x* y  

print(multiply(3)) 
print(multiply(3,4))

def multiply(x, y=2):
    return x*y

print(multiply(3)) 
print(multiply(3,4))