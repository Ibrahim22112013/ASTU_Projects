
from cs1graphics import*
import time
village=Canvas(1000,800)
village.setBackgroundColor('green')
All=Layer()
road=Polygon()
road.addPoint(Point(0,200))
road.addPoint(Point(175,200))
road.addPoint(Point(425,375))
road.addPoint(Point(425,425))
road.addPoint(Point(175,600))
road.addPoint(Point(0,600))
road.addPoint(Point(0,700))
road.addPoint(Point(150,700))
road.addPoint(Point(150,800))
road.addPoint(Point(275,800))
road.addPoint(Point(275,685))
#road.addPoint(Point(450,575))
road.addPoint(Point(500,550))
road.addPoint(Point(750,675))
road.addPoint(Point(750,800))
road.addPoint(Point(850,800))
road.addPoint(Point(850,700))
road.addPoint(Point(1000,700))
road.addPoint(Point(1000,600))
road.addPoint(Point(825,600))
road.addPoint(Point(550,425))
road.addPoint(Point(550,375))
road.addPoint(Point(825,200))
road.addPoint(Point(1000,200))
road.addPoint(Point(1000,100))
road.addPoint(Point(850,100))
road.addPoint(Point(850,0))
road.addPoint(Point(750,0))
road.addPoint(Point(750,100))
road.addPoint(Point(550,250))
road.addPoint(Point(450,250))
road.addPoint(Point(250,100))
road.addPoint(Point(250,0))
road.addPoint(Point(150,0))
road.addPoint(Point(150,100))
road.addPoint(Point(0,100))
road.setFillColor('black')
road.setBorderColor('black')
All.add(road)


square=Circle(150,Point(500,400))
square.setFillColor('black')
square.setDepth(10)
square.setBorderColor('black')
All.add(square)

square1=Circle(50,Point(500,400))
square1.setFillColor('black')
square1.setDepth(5)
square1.setBorderWidth(5)
square1.setBorderColor('white')
square1.setBorderDash(50,30)
All.add(square1)





Line=Polygon(Point(25,150),Point(150,150))
Line.setBorderColor('white')
Line.setBorderWidth(5)
Line.setBorderDash(50,30)

All.add(Line)

Line2=Polygon(Point(200,20),Point(200,120))
Line2.setBorderColor('white')
Line2.setBorderWidth(5)
Line2.setBorderDash(50,30)
All.add(Line2)




Line3=Polygon(Point(220,150),Point(380,270))
Line3.setBorderColor('white')
Line3.setBorderWidth(5)
Line3.setBorderDash(50,30)

All.add(Line3)



Line4=Polygon(Point(800,10),Point(800,115))
Line4.setBorderColor('white')
Line4.setBorderWidth(5)
Line4.setBorderDash(50,30)

All.add(Line4)


Line5=Polygon(Point(850,150),Point(980,150))
Line5.setBorderColor('white')
Line5.setBorderWidth(5)
Line5.setBorderDash(50,30)

All.add(Line5)


Line6=Polygon(Point(618,260),Point(795,150))
Line6.setBorderColor('white')
Line6.setBorderWidth(5)
Line6.setBorderDash(50,30)
All.add(Line6)


Line7=Polygon(Point(800,680),Point(800,780))
Line7.setBorderColor('white')
Line7.setBorderWidth(5)
Line7.setBorderDash(50,30)

All.add(Line7)

Line8=Polygon(Point(830,650),Point(985,650))
Line8.setBorderColor('white')
Line8.setBorderWidth(5)
Line8.setBorderDash(50,30)
All.add(Line8)
Line9=Polygon(Point(625,540),Point(770,630))
Line9.setBorderColor('white')
Line9.setBorderWidth(5)
Line9.setBorderDash(50,30)
All.add(Line9)


Line10=Polygon(Point(25,650),Point(150,650))
Line10.setBorderColor('white')
Line10.setBorderWidth(5)
Line10.setBorderDash(50,30)
All.add(Line10)

Line11=Polygon(Point(210,780),Point(210,700))
Line11.setBorderColor('white')
Line11.setBorderWidth(5)
Line11.setBorderDash(50,30)
All.add(Line11)
Line12=Polygon(Point(230,650),Point(415,530))
Line12.setBorderColor('white')
Line12.setBorderWidth(5)
Line12.setBorderDash(50,30)
All.add(Line12)

z1 = Rectangle(50, 10, Point(105, 110))  # Width, Height, Center Point
z1.setFillColor('white')
z1.setBorderWidth(0)
All.add(z1)

z2 = Rectangle(50, 10, Point(105, 130))
z2.setFillColor('white')
z2.setBorderWidth(0)
All.add(z2)

z3 = Rectangle(10, 10, Point(80, 150))  # Making a square to represent a vertical line
z3.setFillColor('white')
z3.setBorderWidth(0)
All.add(z3)

z4 = Rectangle(50, 10, Point(105, 170))
z4.setFillColor('white')
z4.setBorderWidth(0)
All.add(z4)

z5 = Rectangle(50, 10, Point(105, 190))
z5.setFillColor('white')
z5.setBorderWidth(0)
All.add(z5)


# Create rectangles using the given points as center points
r1 = Rectangle(50, 10, Point(100, 610))  # Width: 50, Height: 10
r1.setFillColor('white')
r1.setBorderWidth(0)
All.add(r1)

r2 = Rectangle(50, 10, Point(100, 630))  # Width: 50, Height: 10
r2.setFillColor('white')
r2.setBorderWidth(0)
All.add(r2)

r3 = Rectangle(50, 10, Point(100, 650))  # Width: 50, Height: 10
r3.setFillColor('white')
r3.setBorderWidth(0)
All.add(r3)

r4 = Rectangle(50, 10, Point(100, 670))  # Width: 50, Height: 10
r4.setFillColor('white')
r4.setBorderWidth(0)
All.add(r4)

r5 = Rectangle(50, 10, Point(100, 690))  # Width: 50, Height: 10
r5.setFillColor('white')
r5.setBorderWidth(0)
All.add(r5)

# Create rectangles using the new pair points as center points
rect1 = Rectangle(10, 50, Point(160, 55))  # Width: 20, Height: 50, Center (160, 75)
rect1.setFillColor('white')
rect1.setBorderWidth(0)
All.add(rect1)

rect2 = Rectangle(10, 50, Point(180, 55))  # Width: 20, Height: 50, Center (180, 75)
rect2.setFillColor('white')
rect2.setBorderWidth(0)
All.add(rect2)

rect3 = Rectangle(10, 50, Point(200, 55))  # Width: 20, Height: 50, Center (200, 75)
rect3.setFillColor('white')
rect3.setBorderWidth(0)
All.add(rect3)

rect4 = Rectangle(10, 50, Point(220, 55))  # Width: 20, Height: 50, Center (220, 75)
rect4.setFillColor('white')
rect4.setBorderWidth(0)
All.add(rect4)

rect5 = Rectangle(10, 50, Point(240, 55))  # Width: 20, Height: 50, Center (240, 75)
rect5.setFillColor('white')
rect5.setBorderWidth(0)
All.add(rect5)




recta1 = Rectangle(10, 50, Point(760, 55))  # Width: 20, Height: 50, Center (160, 75)
recta1.setFillColor('white')
recta1.setBorderWidth(0)
All.add(recta1)

recta2 = Rectangle(10, 50, Point(780, 55))  # Width: 20, Height: 50, Center (180, 75)
recta2.setFillColor('white')
recta2.setBorderWidth(0)
All.add(recta2)

recta3 = Rectangle(10, 50, Point(800, 55))  # Width: 20, Height: 50, Center (200, 75)
recta3.setFillColor('white')
recta3.setBorderWidth(0)
All.add(recta3)

recta4 = Rectangle(10, 50, Point(820, 55))  # Width: 20, Height: 50, Center (220, 75)
recta4.setFillColor('white')
recta4.setBorderWidth(0)
All.add(recta4)

recta5 = Rectangle(10, 50, Point(840, 55))  # Width: 20, Height: 50, Center (240, 75)
recta5.setFillColor('white')
recta5.setBorderWidth(0)
All.add(recta5)



# Create rectangles using the new pair points as center points
rectA = Rectangle(10, 50, Point(160, 755))  # Width: 10, Height: 50, Center (160, 755)
rectA.setFillColor('white')
rectA.setBorderWidth(0)
All.add(rectA)

rectB = Rectangle(10, 50, Point(180, 755))  # Width: 10, Height: 50, Center (180, 755)
rectB.setFillColor('white')
rectB.setBorderWidth(0)
All.add(rectB)

rectC = Rectangle(10, 50, Point(200, 755))  # Width: 10, Height: 50, Center (200, 755)
rectC.setFillColor('white')
rectC.setBorderWidth(0)
All.add(rectC)

rectD = Rectangle(10, 50, Point(220, 755))  # Width: 10, Height: 50, Center (220, 755)
rectD.setFillColor('white')
rectD.setBorderWidth(0)
All.add(rectD)

rectE = Rectangle(10, 50, Point(240, 755))  # Width: 10, Height: 50, Center (240, 755)
rectE.setFillColor('white')
rectE.setBorderWidth(0)
All.add(rectE)

rectF = Rectangle(10, 50, Point(260, 755))  # Width: 10, Height: 50, Center (260, 755)
rectF.setFillColor('white')
rectF.setBorderWidth(0)
All.add(rectF)



# Create rectangles using updated X-axis points and other specifications
rect1 = Rectangle(10, 50, Point(760, 755))  # Width: 10, Height: 50, Center (770, 755)
rect1.setFillColor('white')
rect1.setBorderWidth(0)
All.add(rect1)

rect2 = Rectangle(10, 50, Point(780, 755))  # Width: 10, Height: 50, Center (790, 755)
rect2.setFillColor('white')
rect2.setBorderWidth(0)
All.add(rect2)

rect3 = Rectangle(10, 50, Point(820, 755))  # Width: 10, Height: 50, Center (810, 755)
rect3.setFillColor('white')
rect3.setBorderWidth(0)
All.add(rect3)

rect4 = Rectangle(10, 50, Point(840, 755))  # Width: 10, Height: 50, Center (830, 755)
rect4.setFillColor('white')
rect4.setBorderWidth(0)
All.add(rect4)


# New points for z1 to z5
points1 = [(900, 610), (900, 630), (900, 650), (900, 670), (900, 690)]

# Create the rectangles explicitly without using a loop
rect1_1 = Rectangle(50, 10, Point(*points1[0]))
rect1_2 = Rectangle(50, 10, Point(*points1[1]))
rect1_3 = Rectangle(50, 10, Point(*points1[2]))
rect1_4 = Rectangle(50, 10, Point(*points1[3]))
rect1_5 = Rectangle(50, 10, Point(*points1[4]))

# Set the fill color and border width for each rectangle
rect1_1.setFillColor('white')
rect1_1.setBorderWidth(0)
rect1_2.setFillColor('white')
rect1_2.setBorderWidth(0)
rect1_3.setFillColor('white')
rect1_3.setBorderWidth(0)
rect1_4.setFillColor('white')
rect1_4.setBorderWidth(0)
rect1_5.setFillColor('white')
rect1_5.setBorderWidth(0)

# Create a set to store the rectangles (rect2_* are deleted)
rectangles = set([rect1_1, rect1_2, rect1_3, rect1_4, rect1_5])

# Add rectangles to the canvas or group
for rect in rectangles:
    All.add(rect)







new1 = Rectangle(50, 10, Point(900, 190))  # Width, Height, Center Point
new1.setFillColor('white')
new1.setBorderWidth(0)
All.add(new1)

new2 = Rectangle(50, 10, Point(900, 170))
new2.setFillColor('white')
new2.setBorderWidth(0)
All.add(new2)

new3 = Rectangle(50, 10, Point(900, 150))
new3.setFillColor('white')
new3.setBorderWidth(0)
All.add(new3)

new4 = Rectangle(50, 10, Point(900, 130))
new4.setFillColor('white')
new4.setBorderWidth(0)
All.add(new4)

new5 = Rectangle(50, 10, Point(900, 110))
new5.setFillColor('white')
new5.setBorderWidth(0)
All.add(new5)

All.setDepth(15)
village.add(All)
c=Layer()

b=Rectangle(100,150,Point(200,100))
b.setFillColor('brown')
c.add(b)

l=Rectangle(14,10,Point(158,30))
l.setDepth(1)
l.setFillColor('orange')
c.add(l)

li=Rectangle(14,10,Point(241,30))
li.setDepth(1)
li.setFillColor('orange')
c.add(li)

bl=Rectangle(60,150,Point(200,100))
bl.setFillColor('brown')
c.add(bl)

m=Circle(14,Point(159,170))
m.setDepth(11)
m.setFillColor('red')
c.add(m)

mi=Circle(14,Point(240,170))
mi.setDepth(11)
mi.setFillColor('red')
c.add(mi)
k=Rectangle(60,80,Point(200,100))
k.setFillColor('light blue')
k.setDepth(1)
c.add(k)
c.setDepth(0)
c.scale(0.5)
c.moveTo(100,-170)
village.add(c)

e=Layer()
g=Rectangle(150,100,Point(100,100))
g.setFillColor('brown')
g.setDepth(5)
e.add(g)


h=Polygon(Point(25,50),Point(50,100),Point(25,150))
h.setFillColor('black')
h.setDepth(1)

e.add(h)


l=Polygon(Point(175,50),Point(150,100),Point(175,150))
l.setFillColor('black')
l.setDepth(1)
e.add(l)


p=Polygon(Point(50,100),Point(150,100))
p.setFillColor('black')
p.setBorderWidth(3)
p.setDepth(1)
e.add(p)
e.moveTo(-10,-39)
e.scale(0.9)
village.add(e)

Tree2=Layer()
e1=Circle(25,Point(25,100))
e1.setFillColor('dark green')
e1.setDepth(0)
e1.setBorderColor('dark green')
Tree2.add(e1)

e2=Circle(25,Point(25,75))
e2.setFillColor('dark green')
e2.setDepth(0)
e2.setBorderColor('dark green')
Tree2.add(e2)


e3=Circle(25,Point(40,120))
e3.setFillColor('dark green')
e3.setDepth(0)
e3.setBorderColor('dark green')
Tree2.add(e3)
e4=Circle(25,Point(40,50))
e4.setFillColor('dark green')
e4.setDepth(0)
e4.setBorderColor('dark green')
Tree2.add(e4)


e5=Circle(25,Point(60,100))
e5.setFillColor('dark green')
e5.setDepth(0)
e5.setBorderColor('dark green')
Tree2.add(e5)

e6=Circle(25,Point(60,75))
e6.setFillColor('dark green')
e6.setDepth(0)
e6.setBorderColor('dark green')
Tree2.add(e6)
Tree2.moveTo(280,-30)
Tree2.scale(1.3)


village.add(Tree2)


Tree=Layer()
e1=Circle(25,Point(25,100))
e1.setFillColor('dark green')
e1.setDepth(0)
e1.setBorderColor('dark green')
Tree.add(e1)

e2=Circle(25,Point(25,75))
e2.setFillColor('dark green')
e2.setDepth(0)
e2.setBorderColor('dark green')
Tree.add(e2)


e3=Circle(25,Point(40,120))
e3.setFillColor('dark green')
e3.setDepth(0)
e3.setBorderColor('dark green')
Tree.add(e3)
e4=Circle(25,Point(40,50))
e4.setFillColor('dark green')
e4.setDepth(0)
e4.setBorderColor('dark green')
Tree.add(e4)


e5=Circle(25,Point(60,100))
e5.setFillColor('dark green')
e5.setDepth(0)
e5.setBorderColor('dark green')
Tree.add(e5)

e6=Circle(25,Point(60,75))
e6.setFillColor('dark green')
e6.setDepth(0)
e6.setBorderColor('dark green')
Tree.add(e6)
Tree.moveTo(610,-60)
Tree.scale(1.3)
village.add(Tree)


Tree3=Layer()
e1=Circle(25,Point(25,100))
e1.setFillColor('dark green')
e1.setDepth(0)
e1.setBorderColor('dark green')
Tree3.add(e1)

e2=Circle(25,Point(25,75))
e2.setFillColor('dark green')
e2.setDepth(0)
e2.setBorderColor('dark green')
Tree3.add(e2)


e3=Circle(25,Point(40,120))
e3.setFillColor('dark green')
e3.setDepth(0)
e3.setBorderColor('dark green')
Tree3.add(e3)
e4=Circle(25,Point(40,50))
e4.setFillColor('dark green')
e4.setDepth(0)
e4.setBorderColor('dark green')
Tree3.add(e4)


e5=Circle(25,Point(60,100))
e5.setFillColor('dark green')
e5.setDepth(0)
e5.setBorderColor('dark green')
Tree3.add(e5)

e6=Circle(25,Point(60,75))
e6.setFillColor('dark green')
e6.setDepth(0)
e6.setBorderColor('dark green')
Tree3.add(e6)
Tree3.rotate(90)
Tree3.scale(1.5)
Tree3.moveTo(220,200)
village.add(Tree3)




Tree4=Layer()
e1=Circle(25,Point(25,100))
e1.setFillColor('dark green')
e1.setDepth(0)
e1.setBorderColor('dark green')
Tree4.add(e1)

e2=Circle(25,Point(25,75))
e2.setFillColor('dark green')
e2.setDepth(0)
e2.setBorderColor('dark green')
Tree4.add(e2)


e3=Circle(25,Point(40,120))
e3.setFillColor('dark green')
e3.setDepth(0)
e3.setBorderColor('dark green')
Tree4.add(e3)
e4=Circle(25,Point(40,50))
e4.setFillColor('dark green')
e4.setDepth(0)
e4.setBorderColor('dark green')
Tree4.add(e4)


e5=Circle(25,Point(60,100))
e5.setFillColor('dark green')
e5.setDepth(0)
e5.setBorderColor('dark green')
Tree4.add(e5)

e6=Circle(25,Point(60,75))
e6.setFillColor('dark green')
e6.setDepth(0)
e6.setBorderColor('dark green')
Tree4.add(e6)
Tree4.scale(1.4)
Tree4.moveTo(300,650)
village.add(Tree4)

ea=Layer()
g=Rectangle(150,100,Point(100,100))
g.setFillColor('brown')
g.setDepth(5)
ea.add(g)
h=Polygon(Point(25,50),Point(50,100),Point(25,150))
h.setFillColor('black')
h.setDepth(1)
ea.add(h)
l=Polygon(Point(175,50),Point(150,100),Point(175,150))
l.setFillColor('black')
l.setDepth(1)
ea.add(l)
p=Polygon(Point(50,100),Point(150,100))
p.setFillColor('black')
p.setBorderWidth(3)
p.setDepth(1)
ea.add(p)
ea.rotate(90)
ea.scale(1.4)
ea.moveTo(230,300)
village.add(ea)

eab=Layer()
g=Rectangle(150,100,Point(100,100))
g.setFillColor('brown')
g.setDepth(5)
eab.add(g)
h=Polygon(Point(25,50),Point(50,100),Point(25,150))
h.setFillColor('black')
h.setDepth(1)
eab.add(h)
l=Polygon(Point(175,50),Point(150,100),Point(175,150))
l.setFillColor('black')
l.setDepth(1)
eab.add(l)
p=Polygon(Point(50,100),Point(150,100))
p.setFillColor('black')
p.setBorderWidth(3)
p.setDepth(1)
eab.add(p)
eab.scale(1.4)
eab.moveTo(370,-70)


village.add(eab)

eabc=Layer()
g=Rectangle(150,100,Point(100,100))
g.setFillColor('brown')
g.setDepth(5)
eabc.add(g)
h=Polygon(Point(25,50),Point(50,100),Point(25,150))
h.setFillColor('black')
h.setDepth(1)
eabc.add(h)
l=Polygon(Point(175,50),Point(150,100),Point(175,150))
l.setFillColor('black')
l.setDepth(1)
eabc.add(l)
p=Polygon(Point(50,100),Point(150,100))
p.setFillColor('black')
p.setBorderWidth(3)
p.setDepth(1)
eabc.add(p)
eabc.scale(0.9)
eabc.moveTo(-15,680)
village.add(eabc)


eabcd=Layer()
g=Rectangle(150,100,Point(100,100))
g.setFillColor('brown')
g.setDepth(5)
eabcd.add(g)
h=Polygon(Point(25,50),Point(50,100),Point(25,150))
h.setFillColor('black')
h.setDepth(1)
eabcd.add(h)
l=Polygon(Point(175,50),Point(150,100),Point(175,150))
l.setFillColor('black')
l.setDepth(1)
eabcd.add(l)
p=Polygon(Point(50,100),Point(150,100))
p.setFillColor('black')
p.setBorderWidth(3)
p.setDepth(1)
eabcd.add(p)
eabcd.scale(1.45)
eabcd.moveTo(400,600)
village.add(eabcd)

eabcde=Layer()
g=Rectangle(150,100,Point(100,100))
g.setFillColor('brown')
g.setDepth(5)
eabcde.add(g)
h=Polygon(Point(25,50),Point(50,100),Point(25,150))
h.setFillColor('black')
h.setDepth(1)
eabcde.add(h)
l=Polygon(Point(175,50),Point(150,100),Point(175,150))
l.setFillColor('black')
l.setDepth(1)
eabcde.add(l)
p=Polygon(Point(50,100),Point(150,100))
p.setFillColor('black')
p.setBorderWidth(3)
p.setDepth(1)
eabcde.add(p)
eabcde.scale(1)
eabcde.moveTo(845,665)
village.add(eabcde)



eabcdef=Layer()
g=Rectangle(150,100,Point(100,100))
g.setFillColor('brown')
g.setDepth(5)
eabcdef.add(g)
h=Polygon(Point(25,50),Point(50,100),Point(25,150))
h.setFillColor('black')
h.setDepth(1)
eabcdef.add(h)
l=Polygon(Point(175,50),Point(150,100),Point(175,150))
l.setFillColor('black')
l.setDepth(1)
eabcdef.add(l)
p=Polygon(Point(50,100),Point(150,100))
p.setFillColor('black')
p.setBorderWidth(3)
p.setDepth(1)
eabcdef.add(p)
eabcdef.scale(1.5)
eabcdef.rotate(90)
eabcdef.moveTo(1070,250)
village.add(eabcdef)



eabcdefg=Layer()
g=Rectangle(150,100,Point(100,100))
g.setFillColor('brown')
g.setDepth(5)
eabcdefg.add(g)
h=Polygon(Point(25,50),Point(50,100),Point(25,150))
h.setFillColor('black')
h.setDepth(1)
eabcdefg.add(h)
l=Polygon(Point(175,50),Point(150,100),Point(175,150))
l.setFillColor('black')
l.setDepth(1)
eabcdefg.add(l)
p=Polygon(Point(50,100),Point(150,100))
p.setFillColor('black')
p.setBorderWidth(3)
p.setDepth(1)
eabcdefg.add(p)
eabcdefg.scale(1)
eabcdefg.moveTo(825,-30)
village.add(eabcdefg)


o=Layer()

b=Rectangle(100,150,Point(200,100))
b.setFillColor('blue')
o.add(b)

l=Rectangle(14,10,Point(158,30))
l.setDepth(1)
l.setFillColor('orange')
o.add(l)

li=Rectangle(14,10,Point(241,30))
li.setDepth(1)
li.setFillColor('orange')
o.add(li)

bl=Rectangle(60,150,Point(200,100))
bl.setFillColor('blue')
o.add(bl)

m=Circle(14,Point(159,170))
m.setDepth(11)
m.setFillColor('red')
o.add(m)

mi=Circle(14,Point(240,170))
mi.setDepth(11)
mi.setFillColor('red')
o.add(mi)
k=Rectangle(60,80,Point(200,100))
k.setFillColor('light blue')
k.setDepth(1)
o.add(k)
o.setDepth(0)
o.scale(0.5)
o.moveTo(700,-170)
village.add(o)







p=Layer()

b=Rectangle(100,150,Point(200,100))
b.setFillColor('blue')
p.add(b)

l=Rectangle(14,10,Point(158,30))
l.setDepth(1)
l.setFillColor('orange')
p.add(l)

li=Rectangle(14,10,Point(241,30))
li.setDepth(1)
li.setFillColor('orange')
p.add(li)

bl=Rectangle(60,150,Point(200,100))
bl.setFillColor('blue')
p.add(bl)

m=Circle(14,Point(159,170))
m.setDepth(11)
m.setFillColor('red')
p.add(m)

mi=Circle(14,Point(240,170))
mi.setDepth(11)
mi.setFillColor('red')
p.add(mi)
k=Rectangle(60,80,Point(200,100))
k.setFillColor('light blue')
k.setDepth(1)
p.add(k)
p.setDepth(0)
p.scale(0.5)
p.moveTo(0,50)
p.rotate(90)
village.add(p)






for i in range(130):
    p.move(1,0)
for i in range(300):
     c.move(0,1)
     o.move(0,0.8)
for i in range(40):
    c.rotate(-1)
    o.rotate(1.12)
for i in range(180):
    p.move(0.9,0)
    c.move(1,1.2)
    o.move(-0.7,0.6)
for i in range(38):
    p.rotate(1)
    c.rotate(0.9)
    o.rotate(1)
for i in range(80):
    p.move(1.2,1.7)
    c.move(0,1.25)
    o.move(-1,0)
for i in range(4):
    p.rotate(-1)
for i in range(20):
    o.move(-1,0)
for i in range(35):
    c.rotate(1.3)
    o.rotate(1.4)
for i in range(120):
    p.move(0.5,0.3)
    c.move(-1,1)
    o.move(-1.3,-1)
for i in range(47):
    p.rotate(-0.9)
    c.rotate(1)
    o.rotate(1.3)
for i in range(15):
    p.rotate(-1)
for i in range(200):
    p.move(1,-0.3)
    c.move(-1,0)
    o.move(0,-0.5)
for i in range(10):
    p.rotate(-1)
for i in range(150):
    p.move(1,-0.6)
for i in range(35):
    p.rotate(1)
for i in range(300):
    p.move(1,0.0001)







    

