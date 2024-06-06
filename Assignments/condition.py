#number guessing game in puthon
""" 
import random


n = random.randrange(1, 10)
attempts = 5

while attempts > 0:
   guess = int(input("make a guess: "))
   if guess < n:
       print("Too low")
   elif guess > n :
       print("Too high")
   else:
       print("You guessed it right!")  
       break
   attempts -= 1     """
    
    
""" for i in range(10):
   if i > 5:
       break
   print(i) """

""" count = 0
while count < 5:
    if count == 3:
        print("count is 3")
    count +=1 """

# for i in range(2, 10, 2):
#     print(i)
    
""" for n in range(12):
    print(n) """

""" fruits = ["orange","banana","apple","cucumber","lemon","grapes"]
for fruit in fruits:
    print(fruit) """


""" for l in range(10):
    if l%2 == 0:
        continue
    print(l)
    
for l in range(10):
    if l%2 != 0:
        continue
    print(l) """

""" def test():
    global food
    food= ["eba","yam","egg","amala"]
    for i in food:
         print(i)

test()
print(food)
print(food[2]) """
   
# def test():
#     global food
#     food= ["eba","yam","egg","amala"]
#     for i in range(len(food)):
#          print(i, food[i])

# test()
# def simple_interest(principal : int, time:int, rate ):
#    interest = (principal*time*rate)/100
#    return interest

# print(simple_interest(10, 20, 30))
movies = [
    ["Casablanca", "Michael Curtiz", 1942, "Drama"],
    ["The Godfather", "Francis Ford Coppola", 1972, "Crime"],
    ["The Shawshank Redemption", "Frank Darabont", 1994, "Drama"],
    ["The Dark Knight", "Christopher Nolan", 2008, "Action, Thriller"],
    ["Living in Bondage", "Ola Balogun", 1992, "Drama"],
    ["Nneka the Pretty Serpent", "Christian Chukwu", 1994, "Drama, Thriller"],
    ["Rattlesnake", "Amaka Igwe", 1995, "Crime, Thriller"],
    ["Aki na Ukwa", "Chico Ejiro", 2002, "Comedy"],
    ["Saworo IDE", "unknown ", 1997,"Drama"]
]
def count_by_genre(movies):
    genres = {}
    for movie in movies:
        genres = movie[3]
        print (genres)
    return genres
count_by_genre(movies)


def count_by_genre(movies):
    genres_count = {}
    for movie in movies:
        genres = movie[3].split(",")
        for genre in genres:
            if genre in genres_count:
                genres_count[genre] += 1
            else:
                genres_count[genre] = 1
    return genres_count

print(count_by_genre(movies))



         
