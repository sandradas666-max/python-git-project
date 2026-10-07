is_logged_in=True
is_subscribed=False

user_credits=100
max_credits=200
min_credits=50

credits_valid=(user_credits >= min_credits and user_credits <= max_credits and user_credits != min_credits)
print("user_credits is within the valid range:-",credits_valid)



bonus_eligible = is_subscribed or (not is_subscribed and user_credits > min_credits)
print("user is eligible for bonus credits:-",bonus_eligible)

user_credits += 50
print("add user credits:-",user_credits)

user_credits -= 20
print("subtract user credits:-",user_credits)

user_credits *= 2
print("multiply user credits:-",user_credits)

user_credits %= 150
print("modulo user credits:-",user_credits)

power_result=(user_credits ** 2)
print("square of the final user credits:-",power_result)

full_access=(is_logged_in and is_subscribed)
print("user is both logged in and subscribed:-",full_access)

is_true_login= is_logged_in is True
print(" is_logged_in is exactly True:-",is_true_login)

access_result = is_logged_in or is_subscribed and False
print("access result:-", access_result)
