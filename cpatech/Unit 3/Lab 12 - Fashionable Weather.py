# Sean A
# Temperature Converter and Weather Assistant
# Get a temperature from a user and convert it into Celsius, then display a recommended outfit


try:
	temp = int(input("What is the current temperature in Fahrenheit?"))
	tempc = "{}°C".format(round((temp - 32) * 5 / 9, 1))
	print("The temperature is currently {}".format(tempc))

	if temp >= 85:
		print("It's hot! Wear something light")
	elif temp < 85 and temp >= 70:
		print("It's closer to room temperature, t-shirt and shorts should do. ")
	elif temp < 70 and temp >= 50:
		print("It's getting chilly, pants and a sweatshirt will keep you comfy")
	elif temp < 50:
		print("It's pretty cold, a coat or jacket is recommended")
except:
	print("Please enter an integer for your temperature value")

