w1, w2, w3 = 0.3, 0.2, 0.5
#! yield_of_apples = w1 * temperature + w2 * rainfall + w3 * humidity
kanto_temp = 73
kanto_rainfall = 67
kanto_humidity = 43

kanto_yield_of_apples = w1 * kanto_temp + w2 * kanto_rainfall + w3 * kanto_humidity

print(
    f"The expected yield of apples in Kanto Region is {kanto_yield_of_apples} tons per hectare"
)
# Representing the climate data in the form of vectors instead of seperate variables
kanto = [73, 67, 43]
johto = [91, 88, 64]
hoenn = [87, 134, 58]
sinnoh = [102, 43, 37]
unova = [69, 96, 70]

weights = [w1, w2, w3]


def crop_yield(region, weights):
    result = 0
    for x, w in zip(region, weights):
        result += x * w
    return result


print(crop_yield(kanto, weights))
