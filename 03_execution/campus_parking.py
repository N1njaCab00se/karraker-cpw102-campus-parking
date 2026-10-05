#use a named constant
#by using 2.0 as its value, it is automatically stored as a float
#in our program
COST_PER_HOUR = 2.0

def calculate_estimated_parking_cost(hours):
    estimated_cost = hours * COST_PER_HOUR
    return estimated_cost

# define the main logic of my program
def main():
    #create a variable in which I will store user-entered parked hours
    #A variable is a named space in memory
    parked_hours = float(input("Enter the number of hours you have, or will be, parked: "))
    print(parked_hours)
    estimated_cost = calculate_estimated_parking_cost(parked_hours)
    print("Estimated parking cost: $", estimated_cost)

#call my main function and execute the logic of the program
main()