def divide(numerator, denominator):
    try:
        print("Computing the result...")
        result = numerator / denominator
        print("Computation Successfull")
    except:
        print("Failed to compute result due to Zero Division Error")
        result = None
    return result


numerator = int(input("Numerator: "))
denominator = int(input("Denominator: "))

print(divide(numerator, denominator))
