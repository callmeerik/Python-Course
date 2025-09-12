# Generators in Python
# A generator is like a function that remembers where it left off.
# It uses 'yield' instead of 'return'.

def movie_generator():
    movies = ["Inception", "Titanic", "Avatar", "Interstellar"]
    for m in movies:
        yield m  # pause here, resume next time

# ✅ Using the generator
gen = movie_generator()

print(next(gen))  # Inception
print(next(gen))  # Titanic

print("Looping through remaining movies:")
for m in gen:
    print(m)
