class Chai:
    temperature = "hot"
    strength = "strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "cold"
print(cutting.temperature)

del cutting.temperature
print(cutting.temperature)