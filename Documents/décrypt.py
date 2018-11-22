def get_index(letter,letters):
	for i,j in enumerate(letters):
		print(i,j)
		if j == letter:
			return i

def nex_clef(clef_index):
	for i,j in enumerate(clef_index):
		if j == 9 and i == len(clef_index)-1:
			clef_index[i] = 0
			clef_index.append(0)
		elif j == 9:
			clef_index[i] = 0
		else:
			clef_index[i] += 1


alf = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
message = ["e","l","a","v","t","e","c","n","y","r","v","o","k","l","t"]
clef_index = [0]

finish = ""
while finish != "end":
	


