from functools import reduce
def time(yrs):
    if yrs < 10:
        return yrs* 2 
    if yrs <20:
       
        return (yrs-10)*2.25 + 20
    return (yrs-20)*2.5 + 42.5
        
def salary(sal):
    sal.sort(reverse=True)
    return reduce(lambda x,y:x+y,sal[0:3])/3

def pension(sal,yrs):
    return salary(sal) * time(yrs) / 100

pension([78000,82500,91000],19.75)

def presentvalue(annuity):
    return annuity * (1 - (1 + 0.04) ** -27) / 0.04


