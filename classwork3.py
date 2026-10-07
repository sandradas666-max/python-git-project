has_account=True
email_verified=False

can_login= has_account and email_verified
print("user can login or not:-",can_login)

email="sandradas.666@gmail.com"
is_email_valid= "@" in email
print("email is valid or not:-",is_email_valid)

user_age=17
is_age_valid=(user_age >= 18)
print("age is valid or not:-",is_age_valid)

can_login_final=(has_account and email_verified and is_email_valid and is_age_valid)
print("final login is:-",can_login_final)

print("has_account is True:", has_account is True)







