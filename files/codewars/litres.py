def litres(time):
    litres = 0
    
    if(time != 0):
        for i in range(int(time)):
            litres += 0.5
            
    litres = int(litres)
    return litres
