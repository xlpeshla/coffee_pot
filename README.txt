Assignment 10.1: Your Own Class
Xezae Peshlakai

Class Documentation
    Description of the Class:
        The class I created is called the "CoffeePot", it is a class created to
        model the real life object of a coffee pot. It models the actions a coffee pot
        has in the real world.

    Data Variables Within the Class:
        Within the class, it takes in several variables in order for the methods to work.
        In the real world a coffee pot has dimensions, flavor, amount in the pot, amount poured
        and amount to be refilled. Within the class "CoffeePot" the class takes in those real world
        variables. The coffee pot uses those variables for methods of a coffee pot to work.

    Description of the Methods:
        __init__
            In this method allows the class to initialize the attributes of the class. It takes
            in two arguments: coffee and coffeepot_size. This method does not return anything.
        set_amount
            This method sets the initial amount of coffee restricted by the size of the coffee pot.
            It takes in one argument: The starting amount of coffee in the pot. This method returns
            the new amount of coffee in the pot. 
        get_amount
            This method gets the amount of coffee in the pot at any given instances. It tells the user
            the amount of coffee in the pot. This method does not require any given arguments.
        pour_coffee
            This method models the function of a coffee pot when the coffee is poured from it. It
            takes in one argument, the amount to be poured from the pot. It subtracts the amount poured
            from the total amount of coffee in the pot. It also ensures that if the given amount is not
            available it raises a value error.
        refill_coffee
            This method models the function of a coffee pot when the coffee pot is refilled. It takes in
            one argument, the amount to be refilled into the pot. It adds the given amount to the coffee pot
            to the total amount of coffe in the pot. It also ensures if the given amount is more than the
            size of the coffee pot, it resets the amount in the coffee pot to zero.

Demo Program Documentation:
    Description of the demo program.
        In the demo program, the class "Coffeepot" is used. The demo example I decided to use is coffee flavor
        "french roast" and the coffeepot size entered is 100 ounces. For program the program to work, the first
        method that has to be called is the set_amount, which starts with the amount of coffee to be set in the
        coffee pot which is 80 ounces. Then the demo utilizes the pour_coffee method and 30 ounces is subtracted
        from the amount. Then the demo utilizes the refill_coffee method and 40 ounces is added to the total
        amount. Lastly the get_amount method is utilized to get the total amount of coffee in the pot after the
        coffee is poured and refilled.
    Instructions
        To run the demo program the user only has to run the python program. If the user wants to run their own 
        program they can used they must use the set_amount first in order for the other functions to work. 
        They can use the methods: pour_coffee, refill_coffee, and get_amount in any order they choose with
        their respective variables. The program will run.

