topping = {}
topping["Anchovies"] = 50
topping["Artichoke"] = 60
topping["Bacon"] = 92
topping["Broccoli"] = 24
topping["Cheese"] = 80
topping["Chicken"] = 30
topping["Feta"] = 99
topping["Garlic"] = 8
topping["Ham"] = 46
topping["Jalapeno"] = 5
topping["Meatballs"] = 120
topping["Mushrooms"] = 11
topping["Olives"] = 25
topping["Onions"] = 11
topping["Pepperoni"] = 80
topping["Peppers"] = 6
topping["Pineapple"] = 21
topping["Ricotta"] = 108
topping["Sausage"] = 115
topping["Spinache"] = 18
topping["Tomatoes"] = 14

#Get the input and split it
inp = raw_input()
inp = inp.rstrip('\r')
inp = inp.split(' ')

#Parse the number of different pizza
combinaisons = int(inp[0])

#Assert the values
#assert combinaisons > 1
#assert combinaisons < 100	

#Init the stuff
calories = 0
i = 0
while i <= combinaisons:
	calories += int(inp[i+1]) * 270
	food = inp[i+2]
	if ',' in food:
		
		food = food.split(',')
		#try:
			#for elem in food:
				#if elem not in topping:
					#raise NameError()
		#except NameError():
			#print("Topping not in the list")			

		for elem in food:
			if elem in food:
				calories += int(inp[i+1]) * topping[elem]

	else:
		#try:
			#if food not in topping:
				#raise NameError()
		#except NameError():
			#print("Topping not in the list")
	
		calories += int(inp[i+1])*topping[food]
	
	i += 2

print("The total calorie intake is " + str(calories))
		
	
