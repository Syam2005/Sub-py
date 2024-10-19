x,y,z= list(map(int,input("enter 3 numbers").split(",")))
if x>y:
	if x>z:
		print(f"{x} is larger")
	else:
	    print(f"{z} is larger")
else:
    if y>z:
        print(f"{y} is larger")
    else:
	    print(f"{z} is larger")