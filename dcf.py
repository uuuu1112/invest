from baseDf import *

def futureEpsList(eps,startGrowth,normalGrowth=0.02):
    epsNow=eps
    epsList=[]
    for i in range(5):
        epsNow=epsNow*(1+startGrowth)
        epsList.append(epsNow)
    for j in range(5):
        epsNow=epsNow*(1+normalGrowth)
        epsList.append(epsNow)
    return epsList

def discountValue(epsList,discountRate=0.1,gdpGrowth=0.02):
    epsDiscount=0
    for i in range(10):
        epsDiscount=epsDiscount+epsList[i]*((1+discountRate)**(-i-1))
        print(epsList[i]*((1+discountRate)**(-i-1)))
    outOf10Dis=epsList[-1]*(1+gdpGrowth)/(discountRate-gdpGrowth)/((1+discountRate)**10)
    epsDiscount=epsDiscount+outOf10Dis
    return epsDiscount