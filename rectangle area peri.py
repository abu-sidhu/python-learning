#The area and perimeter of a rectangle
def area_rec(x,y):
    print('The area of given rectangle =', x*y)
def peri_rec(x,y):
    print("The perimeter of given rectangle =", 2*(x+y))
    
length=int(input("Enter the length of rectangle "))
breadth=int(input("Enter the breadth of rectangle "))
area_rec(length , breadth )
peri_rec(length , breadth )