import random, string
def pass_fun(length, upper = True, number = True, special = True):
	numbers = ["1","2","3","4","5","6","7","8","9","0"]
	special_char = ["!","@","#","$","%","&","*"]
	letters_lower = list(string.ascii_lowercase)
	letters_upper = list(string.ascii_uppercase)
	password = ""
	variables = []
	variables.extend(letters_lower)
	if upper == True:
                variables.extend(letters_upper)
	if number == True:
		variables.extend(numbers)
	if special == True:
		variables.extend(special_char)
	random.shuffle(variables)
	for i in range(length):
		password += (random.choice(variables))
	passlist = sorted(password)
	passlist = passlist[::-1]
	password = ""
	for p in passlist:
		password += p
	return password


if __name__ == '__main__':
	inp = input("Enter : ")
	print((inp))
	for i in list(inp):
        try:
            pass
        except:
            i = int(i)
            num += str(i)
	print(num)
