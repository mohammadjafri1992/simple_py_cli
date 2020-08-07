def _greet_user(user):
	print("Hello, ", user)

def get_user():
	user = input("What is your name?")
	return user

def interface_with_user(user):
	_greet_user(user)
