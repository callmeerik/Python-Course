"""
            TUPLES
    
    ✅ Allow duplicated values
    ✅ Ordered
    ❌ Inmutable
"""

# Create a tuple with only one item
aircraft = ('A320 Neo', )
print(type(aircraft))

# Multivalue tuple
aircrafts = ('A320', 'B787', 'B747', 'A350')

# Acces to items
print(aircrafts[0])

# unpacking a tuple
aircrafts_list = list(aircrafts)
print(aircrafts_list)

# list of tuples
floats = [
    ('A320', 230),
    ('A380', 500),
    ('B747', 430)
]

for float in floats:
    print(f' {float[0]} - {float[1]} ')