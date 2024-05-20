def dictionaryPractice():
myfamily ={
  "child1":{
    "name": "Hamnah",
    "year":2003
  },
  
  "child2":{
    "name":"Syed",
    "year": 2005
  },
  
  "child3":{
    "name": "Uzair",
    "year": 2012
  }
  
  
}

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])
