"""
    FLLIGHTS DATA ANALYSIS USING MAP, REDUCE AND FILTER
"""

# 1. iMPORT JSON PACKAGE
import json

# 2. Import data
with open("flights.json", "r") as file:
    flights = json.load(file)

# 3. Data Overview

# 3.1. Size of dataset
print(f"Number of observations: {len(flights)}")

# first 2 rows
for f in flights[0: 2]:
    print(f)

# 4. Analysis

# Q1. filter all international flights
ecuadorian_airports = ["UIO", "GYE", "GPS", "Coca", "CUE", "MEC"]
international_flights = list( filter( lambda f: f["destination"] not in ecuadorian_airports, flights ) )
print(f"Q1- International Flights (First 5):")
for f in international_flights[:5]:
    print(f"{f['origin']} - {f['destination']}")

# Q2. Compute total number of passenger around all flights
from functools import reduce
total_passengers = reduce( lambda acc, flight: acc + flight['passengers'], flights, 0 )
print(f"Q3. Total Number of Passengers: {total_passengers}")

# Q5. Calculate the average of prices
prices = list(map( lambda flight: flight['price'], flights ))
avg_price = sum(prices) / len(prices)
print(f"Q5. Avg Flights Price: ${avg_price}") 

# Q6- Compute the total revenue per international flight
total_revenues = list(map(
    lambda f: {"flight": f['flight'], "revenue": f["passengers"] * f['price']},
    international_flights
))
print(f"Q6- Revenue in International Flights")
for rev in total_revenues[:5]:
    print(f"{rev['flight']}: ${ rev['revenue'] } USD")