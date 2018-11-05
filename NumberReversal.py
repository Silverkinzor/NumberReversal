print("Number Reversal (not string reversal!)")
print("eg. 00034 will be interpreted as 34\n")

while True: # input and validation
    try:
        number = int(input("Enter a number: "))
        if number < 0:
            print("Positive numbers only!")
        else:
            break
    except ValueError:
        print("\nInvalid Input\n")

numbera = number # declaration
c = 0
revnumber = ""

while numbera > 9:

    while number > 9:
        number = number - 10 	# gets the number in the ones column
        c = c + 1 		# the rest from a counter

    revnumber = revnumber + str(number) # add the number to output
    number = c 				# set the number to rest and run again
    c = 0 				# reset
    numbera = number 			# if the rest is < 10, exit

    # so it will all loop like 784, 78 4, 7 48, 487

revnumber = revnumber + str(numbera) # add the final thing

print(revnumber)