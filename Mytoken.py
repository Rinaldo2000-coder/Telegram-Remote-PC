def tokenID():
	file = open("tokenid.txt", 'r')
	code = file.read()
	file.close()
	return code
if __name__ == '__main__':
	print(tokenID())