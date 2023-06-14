# Data Analysis for Vacation Planning
import math


def cost_of_trip(cities, budget=0, duration=0):
    """
    cities - we have data of few different cities for which you can do calculations
     Budget - What's your budget?
     Duration - For how long you wanna have fun !(in no. of days
    """
    total_cost = [0] * len(cities)
    i = 0
    if not budget:
        for city in cities:
            total_cost[i] = (
                city["return_flight"]
                + city["hotel_per_day"] * duration
                + city["car_rental"] * math.ceil(duration / 7)
            )
            i += 1
        cost = min(total_cost)
        index = total_cost.index(cost)
        print(
            "\nFor spending least amount on {}-days trip , you should visit {} , costing ${} for the trip.".format(
                duration, cities[index]["city_name"], cost
            )
        )
    else:
        days = [1] * len(cities)
        for city in cities:
            while True:
                total_cost[i] = (
                    city["return_flight"]
                    + city["hotel_per_day"] * duration
                    + city["car_rental"] * math.ceil(duration / 7)
                )
                if total_cost[i] > budget:
                    days[i] -= 1
                    total_cost[i] = (
                        city["return_flight"]
                        + city["hotel_per_day"] * duration
                        + city["car_rental"] * math.ceil(duration / 7)
                    )
                    break
                else:
                    days[i] += 1
            i += 1

        # For longer outing in budget
        max_days = max(days)
        index_max = days.index(max_days)

        print("\nFor budget ${} ".format(budget))
        print(
            "You should visit {} , for {} days, costing ${} (Max Days)".format(
                cities[index_max]["city_name"], max_days, total_cost[index_max]
            )
        )

        # For shorter outing in budget
        min_days = min(days)
        index_min = days.index(min_days)
        print(
            "You should visit {} , for {} days, costing ${} (Min Days)".format(
                cities[index_min]["city_name"], min_days, total_cost[index_min]
            )
        )


places = [
    {
        "city_name": "Paris",
        "return_flight": 200,
        "hotel_per_day": 20,
        "car_rental": 200,
    },
    {
        "city_name": "London",
        "return_flight": 250,
        "hotel_per_day": 30,
        "car_rental": 120,
    },
    {"city_name": "Dubai", "return_flight": 370, "hotel_per_day": 15, "car_rental": 80},
    {
        "city_name": "Mumbai",
        "return_flight": 450,
        "hotel_per_day": 10,
        "car_rental": 70,
    },
]

cost_of_trip(cities=places, duration=7)

cost_of_trip(cities=places, duration=4)
cost_of_trip(cities=places, duration=10)
cost_of_trip(cities=places, duration=14)

cost_of_trip(cities=places, budget=1000)
cost_of_trip(cities=places, budget=600)
cost_of_trip(cities=places, budget=2000)
cost_of_trip(cities=places, budget=1500)

print()
