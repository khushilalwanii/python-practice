with open("nyc_weather.csv", "r")as f:
    lines = f.readlines()

weather = {}

for line in lines[1:]:
    tokens = line.strip().split(',')
    day = tokens[0]
    temperature = tokens[1]
    if temperature != "":
        weather[day] = int(temperature)

print("Temperature on jan 9", weather["Jan 9"])

print("temperature on jan 4:", weather["Jan 4"])



