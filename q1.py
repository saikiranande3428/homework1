import statistics
ages = [19,22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

print("Min Age =",ages[0],"Max age =",ages[-1])
print("Median = ",statistics.median(ages))
print("Average = ",sum(ages)/len(ages))
print("Range = ",max(ages)-min(ages))
