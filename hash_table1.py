import csv

with open("nyc_weather.csv", "r") as f:
    lines = f.readlines()

temperatures = []
for line in lines[1:]:
    tokens = line.strip().split(',')
    if tokens[1] != "":
        temperatures.append(int(tokens[1]))

#average temp of week first
first_week = temperatures[0:7]
avg_temp = sum(first_week)/len(first_week)
print("average temp in first week of jan is:", avg_temp)

#max temp in first 10 days(jan1 - jan 10)
max_temp = max(temperatures[0:10])
print("max temp in first 10 days is:", max_temp)
