# Assignment 10.1: Your Own Class
# Xezae Peshlakai

# Acknowledgements

# I recieved help from a TA

# Here I created my class variable "coffee pot"
class CoffeePot:
    # I made my variable take in two data variables, the coffee flavor and coffee pot size.
    def __init__(self, coffee, coffeepot_size):
        # I used self to access the attributes and methods.
        self.__coffee = coffee
        self.__coffeepot_size = coffeepot_size
        self.__amount = 0
  
    # This method sets the amount of coffee in the given coffee pot.
    def set_amount(self, amount):
        # If the amount of coffee set is greater than the size of the coffee pot it will raise an error.
        if amount > self.__coffeepot_size:
            raise ValueError
        # If the amount of coffee set is less than the coffee pot size it will set the amount in the coffee pot.
        if amount < self.__coffeepot_size:
            self.__amount = amount
            return(f"You have set {self.__amount} ounces in your {self.__coffee}.")

    # This method will get the amount of coffee in the coffee pot.
    def get_amount(self):
        return (f"You have {self.__amount} ounces in your {self.__coffee}.")
  
    # This method pours the coffee, given the amount to be poured.
    def pour_coffee(self, pour):
        # If the pour amount is greater then the amount in the coffee pot, it will raise an error and
        # tell the user their is not enough coffee to pour.
        if pour > self.__amount:
            return ValueError
            return("Their is not enough coffee to pour.")
        # If the pour amount is less then the amount in the coffee pot then, it will subtract the pour
        # from the coffee pit.
        if pour < self.__amount:
            self.__amount -= pour
            return(f"You poured {pour} ounces in your {self.__coffee}")
    
    # This method refills the coffee pot , given the refill amount.
    def refill_coffee(self, refill_amount):
        # If the refill amount is greater then coffee pot subtacted by the amount of coffee in the pot,
        # it will reset the coffee pot to zero, and tell the user they overpoured the coffee pot.
        if refill_amount > (self.__coffeepot_size - self.__amount):
            self.__amount = 0
            return(f"You have overpoured your {self.__coffee}.")
        # If the refill amount is less then coffee pot subtacted by the amount of coffee in the pot,
        # It will add the amount poured to the total coffee pot amount.
        if refill_amount < (self.__coffeepot_size - self.__amount):
            self.__amount += refill_amount
            return(f"You refilled {refill_amount} ounces in your {self.__coffee}")
 
def main():
    # The main calls the class "CoffeePot" and the inputs inserted is the flavor and size of the coffee pot.
    french_roast = CoffeePot("French Roast", 100)

    # Here the method set_amount is called to set the amount of coffee in the pot. The expected output is
    # suppose to return "You have set 80 ounces in your French Roast."
    print(french_roast.set_amount(80))

    # The method pour_coffee is called to subtract 30 ounces to the set amount of coffee. The expected ouput is
    # suppose to return "You have poured 30 ounces in your french roast."
    print(french_roast.pour_coffee(30))

    # The method refill_cofffe is called to add 40 ounces to the set amount of coffee. The expected ouput is
    # suppose to return "You have refilled 40 ounes in your French Roast."
    print(french_roast.refill_coffee(40))

    # Finally, to see how much coffee is in the pot after setting, pouring, and refilling the pot, the
    # method get_amount is called to get the total amount of coffee in the pot.
    # The expected output is suppose to return "You have 90 ounces in your French Roast."
    print(french_roast.get_amount())
    
if __name__ == "__main__":
   main()