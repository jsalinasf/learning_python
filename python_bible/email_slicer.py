email = input("Whats your email address?: ").strip()
email = email.lower()
user = email[:email.index("@")]
domain = email[(email.index("@")+1):]
message = "Your username is: {} and your domain is: {}".format(user,domain)
print (message)
