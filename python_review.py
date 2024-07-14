import random as rand


days_of_the_week = ["Sunday","Monday","Tuesday","Wednsday","Thursday","Friday","Saturday"]
temperatures = []
good_days_count = 0
high_temp = 0
low_temp = 41
high_temp_day = ""
low_temp_day = ""
avg_temp = 0
above_avg = []


for i in range(7):
	temperatures.append(rand.randint(26,40))
	avg_temp += temperatures[i]


	if temperatures[i] % 2 == 0:
		good_days_count += 1
	if temperatures[i] > high_temp:
		high_temp = temperatures[i]
		high_temp_day = days_of_the_week[i]
	if temperatures[i] < low_temp:
		low_temp = temperatures[i]
		low_temp_day = days_of_the_week[i]

avg_temp /= 7



print("The weather report:")
for i in range(7):
	print("Temperature of the days: " + str(days_of_the_week[i]) + ": " + str(temperatures[i]))
	if temperatures[i] > avg_temp:
		above_avg.append(temperatures[i])
print("Shelly had " + str(good_days_count) + " good days")
print("The day with the highest temp: " + str(high_temp_day) + "with the temp of: " + str(high_temp))
print("The day with the lowest temp: " + str(low_temp_day) + "with the temp of: " + str(low_temp))
print("The average temp was: " + str(avg_temp))
print("The days with above average temp were: " + str(above_avg))
