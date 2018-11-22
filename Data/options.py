def options():
	message_file = "message.txt"
	caracters = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

	r= (160,25,25)
	w= (150,150,150)
	p= (70,25,130)
	c= (25,80,130)

	cross = [
	r,r,r,r,r,r,r,r,
	r,w,r,r,r,r,w,r,
	r,r,w,r,r,w,r,r,
	r,r,r,w,w,r,r,r,
	r,r,r,w,w,r,r,r,
	r,r,w,r,r,w,r,r,
	r,w,r,r,r,r,w,r,
	r,r,r,r,r,r,r,r]
	triangle = [
	c,c,c,c,c,c,c,c,
	c,c,c,w,w,c,c,c,
	c,c,w,c,c,w,c,c,
	c,c,w,c,c,w,c,c,
	c,w,c,c,c,c,w,c,
	c,w,c,c,c,c,w,c,
	c,w,w,w,w,w,w,c,
	c,c,c,c,c,c,c,c]
	circle = [
	p,p,p,p,p,p,p,p,
	p,p,w,w,w,w,p,p,
	p,w,p,p,p,p,w,p,
	p,w,p,p,p,p,w,p,
	p,w,p,p,p,p,w,p,
	p,w,p,p,p,p,w,p,
	p,p,w,w,w,w,p,p,
	p,p,p,p,p,p,p,p]

	return(message_file,caracters,r,w,p,c,cross,triangle,circle)