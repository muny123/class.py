employees = [
    {
     "name":"Munira", 
     "details":{"age": 20, 
                "position": "CEO", 
                "tasks": ["html", "css"]
               }
    },
     {
     "name":"Ibraheem ", 
     "details":{"age": 30, 
                "position": "Consultant", 
                "tasks": ["paed", "cardics"]
               }
    },
      {
     "name":"Rahmah ", 
     "details":{"age": 9, 
                "position": " First", 
                "tasks": ["verba", "quant"]
               }
    }
     ,  {
     "name":"Aishah", 
     "details":{"age": "7 ", 
                "position": " second", 
                "tasks": ["Quran", "Hadith"]
               }
    },
        {
     "name":"Abdurrahman ", 
     "details":{"age": " 5", 
                "position": "third ", 
                "tasks": ["fiqh", "taoheed"]
               }
    }
]

task = employees[0]["details"]["tasks"][0]
print(task)
for employee in employees:
    print(employee["name"].upper())  
    

def name(employees):
    for employee in employees:
        yield employee["name"]
        


    
    
    """ 
    # Generator and Iteraor, generators uses YIELD to return insteas of the normal return fuction 
list_instance = [1,2,3,4,5]
iterator = iter(list_instance)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))



def factors(n):
    for val in range(1, n+1):
        if n% val ==0:
            yield val 
print(factors(20))
factors_of_20 = factors(20)
print(next(factors_of_20))
print(next(factors_of_20))
print(next(factors_of_20))
print(next(factors_of_20))
print(next(factors_of_20))
print(next(factors_of_20))

#another method to write a list or generator comprehesion
print(val for val in range(1, 20+1) if n % val == 0) """
      
      # map
num = [1, 2, 3, 4, 5]
""" def square(num_list: list) :
    for i in num_list:
        return i*i
print(square(num)) """ 


 
def square(num_list:list):
    return [i**2 for i in num_list]
print(square(num)) 