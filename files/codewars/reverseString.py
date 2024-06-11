#Could also do  return string[::-1]

def solution(string):
    new = ""
    for i in range((len(string)),0,-1):
        new +=string[i-1]
        
    return new
    pass
