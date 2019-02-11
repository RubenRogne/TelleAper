from pylab import *

år = 24
måneder = 12*år
k = 0.01
p = 28

liste=[28]
måned = [0]                                            



for i in range(måneder):
    p = p*(k+1)
    liste.append(p)
    måned.append(i+1)
    print(i)





y1 = liste 
x1 = måned
plot(x1,y1,color = "red")
grid("on")
xlabel("Måneder")
ylabel("Antall aper")
show()



