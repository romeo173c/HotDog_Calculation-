#Make a menu for the user and ask for the amount of hots dogs and buns required
def main ():
    print("Welcome to your friendly hotdog calculator")
    total_people = int(input("How many people will be in attendance?: "))
    dogs_recieved = int(input("How many hot dogs will each person recieve?: "))

    #Make it where you have the amount of people coming, how many hot dogs will be given, and the left overs 
    
    total_needed = total_people * dogs_recieved

    hotdog_package = 0
    hotdogs = 0
    while hotdogs < total_needed:
            hotdogs += 10
            hotdog_package += 1

    
    bun_package = 0 
    total_buns = 0
    while total_buns < total_needed:
            total_buns += 8
            bun_package += 1

    leftover_hotdogs = hotdogs - total_needed
    leftover_buns =  total_buns - total_needed

    #make a menu that will print the results 

    print("We did all the heavy lifting on the Math side and here are our results")
    print(f"The hot dog packages required are {hotdog_package} and the buns required are {bun_package}")
    print(f"Your left over hotdogs will be {leftover_hotdogs} and your left over buns will be {leftover_buns}")
    print("Enjoy the party and don't forget to same us some too :) ") 

main()