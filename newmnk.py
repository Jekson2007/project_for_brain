import math
class myfirstclass:
    
    def __init__ (self, a, b):
        self.a = a
        self.b = b
                  
    def kvadrat(self):
        '''quadratic regression y=ax^2+bx+c'''
        n=len(self.a)
        lt=[i for i in range(n)]
        x2=[self.a[i]**2 for i in lt]
        x3=[self.a[i]**3 for i in lt]
        x4=[self.a[i]**4 for i in lt]
        xy=[self.a[i]*self.b[i] for i in lt]
        x2y=[(self.a[i]**2)*self.b[i] for i in lt]
        sumx=sum(self.a)#16
        sumy=sum(self.b)#15
        sumx2=sum(x2)#58
        sumx3=sum(x3)#232
        sumx4=sum(x4)#994
        sumxy=sum(xy)#40
        sumx2y=sum(x2y)#120
        s = sumx2*(sumx2*sumx2-sumx*sumx3)-sumx*(sumx3*sumx2-sumx*sumx4)+n*(sumx3*sumx3-sumx2*sumx4) 
        s1= sumy*(sumx2*sumx2-sumx*sumx3)-sumx*(sumxy*sumx2-sumx*sumx2y)+n*(sumxy*sumx3-sumx2*sumx2y)
        s2=sumx2*(sumxy*sumx2-sumx*sumx2y)-sumy*(sumx3*sumx2-sumx*sumx4)+n*(sumx3*sumx2y-sumxy*sumx4)
        s3= sumx2*(sumx2*sumx2y-sumxy*sumx3)-sumx*(sumx3*sumx2y-sumxy*sumx4)+sumy*(sumx3*sumx3-sumx2*sumx4)
        a = s1/s
        b = s2/s
        c = s3/s
        #sry=(sum(self.b)/n)
        #r0 = [(self.b[i] - (a*self.a[i]**2+b*self.a[i]+c))**2 for i in lt]
        #r1 = [(self.b[i]-sry)**2 for i in lt]
        #r = (1-(sum(r0)/sum(r1)))**0.5 # индекс кореляции
        #r2 = r**2 # индекс детерминации
        z = [abs((self.b[i] - (a*self.a[i]**2+b*self.a[i]+c))/self.b[i]) for i in lt]
        er = sum(z)/n*100 #Средняя ошибка аппроксимации:
        return a,b,c,er


if __name__ == "__main__":
    myfirstclass()