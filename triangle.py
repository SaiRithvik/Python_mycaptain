a = float(input())

b = float(input())

c = float(input())

if(a==b and a==c):
	print("the triangle with length of sides as a,b,c is EQUILATERAL ")

elif(a==b or b==c or c==a):
	print("the triangle with length of sides as a,b,c is ISOSCELES ")

else:
	print("the triangle with length of sides as a,b,c is SCAELENE ")


