
import random

def password(a):
	up = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	lw = ["a","b","c","d","e",'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	num = ["1","2","3","4","5","6","7","8","9","0"]
	sym = ["!","@","#","$","%","&","*"]
	final = up+lw+num+sym

	passw = []

	for x in range(a):
		f = random.choice(final)
		passw.append(f)
	
	random.shuffle(passw)

	s = ""
	for x in passw:
		s += x
	
	return s

ask  = int(input("Enter Password Length :- \n"))
passwordf = password(ask)
print("Generated Password : ",passwordf)

