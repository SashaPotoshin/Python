class triangle
    def _init_(self, a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def Perimeter (self):
        return a+b+c
    p=(a+b+c)/2
    def Square (self):
        return (p(p-a)*(p-b)*(p-c))*0.5
a = 5
b = 2
c = 2

if a+b<c and a+c<b and b+c<a:
    print ("треугольник не существует")
else:
    print (a.Perimeter)
    print (a.Square)
