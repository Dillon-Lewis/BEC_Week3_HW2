#Task 1: 
# Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:

# Destinations that both airlines fly to.
# Destinations unique to your airline.
# Whether there are any destinations that neither airline shares.

Boeing = {"LAX", 'DIA', 'JFK', 'ORF'}
Spirit = {"JFK", 'DIA', 'CMW', 'MCO'}

def main():
    while True:
        choice = input('''
Lets see how we compare to our competitors in the air!
1. View destination lists
2. Destinations we both fly to
3. Monopolized Destinations
4. Destinations that we both dont share
5. Quit the program
        ''')
        if choice == '1':
            print(f"All Boing Destinations: {Boeing}")
            print(f'All Spirit Destinations: {Spirit}')
        elif choice == '2':
            both()
        elif choice == '3':
            unique()
        elif choice == '4':
            no_share()
        elif choice == '5':
            break
        else:
            print('Enter a valid number')
            continue

def both():
    same_dest =  Boeing.intersection(Spirit)
    print(f" Boeing and Spirt can both fly to: {same_dest}")
          
def unique():
    unique_destB = Boeing.difference(Spirit)
    unique_destS = Spirit.difference(Boeing)

    print(f'Boeing currently has a monopoly destinations in {unique_destB}')
    print(f'Spirit currently has a monopoly destinations in {unique_destS}')

def no_share():
    sym_dif =Boeing.symmetric_difference(Spirit)
    print(f"We currently don't share coverage in the following areas: {sym_dif}")


main()
