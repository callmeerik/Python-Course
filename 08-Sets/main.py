"""
            SETS
    ❌ Unchangeable
    ❌ Unindexed
    ✅ Add new items
    ✅ Remove items
"""

# Create a set
pizzas = {'🍕Margherita', '🍍 Hawaiian', '🌭 Pepperoni', '🧀 Four cheese'}

# access to an item
print( pizzas )

# Add items
pizzas.add('🥩Meat Lovers')
print(f'New Set: {pizzas}')

# remove items
pizzas.remove('🥩Meat Lovers')

pizzas.discard('🍍 Hawaiian')
print(pizzas)