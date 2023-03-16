#Challenge Exercise #1
#def main(): 
 # texas()
  #california()

#def texas():
 # texas_birds = int(input('Enter the number of birds in Texas: '))
  #print(f'Texas has {texas_birds} birds.')

#def california():
 # california_birds = int(input('Enter the number if birds in California: '))
  #print(f'California has {california_birds} birds.')

#main()












#Challenge Exercise #2
#def get_user_info():
#    last_name = input("Enter your last name: ")
 #   first_name = input("Enter your first name: ")
  #  address = input("Enter your address: ")
   # city = input("Enter your city: ")
    #state = input("Enter your state: ")
    #zip_code = input("Enter your zip code: ")
    #return last_name, first_name, address, city, state, zip_code

#last_name, first_name, address, city, state, zip_code = get_user_info()

#print("\nHere's your information:")
#print(f"{first_name} {last_name}")
#print(f"{address}")
#print(f"{city}, {state} {zip_code}")


















#Challenge Exercise #3
#def add (num1,num2,num3):
 # global total
 # total = num1 + num2+ num3
  #return total
#add(3,4,5)
#print(total)































#Challenge Exercise #4
#num1 = 0
#num2 = 0
#num3 = 0
#sum = 0
#avg = 0

#def get_user_input():
 #   global num1, num2, num3
  #  num1 = int(input("Enter the first number: "))
   # num2 = int(input("Enter the second number: "))
    #num3 = int(input("Enter the third number: "))

#def calculate_sum():
 #   global sum
  #  sum = num1 + num2 + num3

#def calculate_avg():
 #   global avg
  #  avg = sum / 3

#get_user_input()
#calculate_sum()
#calculate_avg()

#print(f"The sum of {num1}, {num2}, and {num3} is: {sum}")
#print(f"The average of {num1}, {num2}, and {num3} is: {avg}")























#Challenge Exercise #5
#def calculate_pay(hours_worked, hourly_pay_rate):
 #   pay = hours_worked * hourly_pay_rate
  #  return pay

#hours_worked = float(input("Enter the number of hours worked: "))
#hourly_pay_rate = float(input("Enter the hourly pay rate: "))

#total_pay = calculate_pay(hours_worked, hourly_pay_rate)

#print(f"The total pay for {hours_worked} hours worked at ${hourly_pay_rate:.2f} per hour is: ${total_pay:.2f}")








































#Part 2

#Challenge Exercise #1
# ask user to enter distance in kilometers
#kilometers = float(input("Enter distance in kilometers: "))

# convert kilometers to miles
#conversion_factor = 0.6214
#miles = kilometers * conversion_factor

# print the result
#print(f"{kilometers} kilometers is equal to {miles} miles.")
















#Challenge Exercise #2
# ask user to enter monthly expenses
loan_payment = float(input("Enter monthly loan payment: "))
insurance = float(input("Enter monthly insurance cost: "))
gas = float(input("Enter monthly gas cost: "))
oil = float(input("Enter monthly oil cost: "))
tires = float(input("Enter monthly tire cost: "))
maintenance = float(input("Enter monthly maintenance cost: "))

# calculate total monthly cost
total_monthly_cost = loan_payment + insurance + gas + oil + tires + maintenance

# calculate total annual cost
total_annual_cost = total_monthly_cost * 12

# print the results
print(f"Total monthly cost: {total_monthly_cost:.2f}")
print(f"Total annual cost: {total_annual_cost:.2f}")
