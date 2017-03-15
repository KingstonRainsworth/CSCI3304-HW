stringa = "butterfly"
stringb = "butterfree"
stringc = "butter"
stringd = "butler"

def alignString(x,y):
	S = [[0 for i in range(len(x))] for j in range(len(y))]
	for i in range(1,len(x)):
		for j in range(len(y)):
			S[i][j] = cost(i,j)
	return S

def cost(i,j,x,y,S):
	if i = 0:
		if j = 0:
			return 0
		else:
			return 1*j
	if j = 0:
		if i = 0:
			return 0
		else:
			return 1*i
	if i > 0 && j > 0:
		swapcost = S[i-2][j-2] + 10
		 		 
		