# coffee-machine
## You can check it out [HERE]( https://mohamedsbaih.github.io/coffee-machine/)

---

## Team Members:-

- [Mohamed Ayman Sbaih](https://github.com/MohamedSbaih)


## Coffee Machine Program Requirements
- Prompt user by asking “
What would you like? espresso/latte/cappuccino):​
”
a.Check the user’s input to decide what to do next.b.The prompt should show every time action has completed, e.g. once the drink isdispensed. The prompt should show again to serve the next customer.
- Turn off the Coffee Machine by entering “off​” to the prompt.
a.For maintainers of the coffee machine, they can use “off” as the secret word to turn offthe machine. Your code should end execution when this happens.
- Print report.
a.When the user enters “report” to the prompt, a report should be generated that showsthe current resource values. e.g.
Water: 100mlMilk: 50mlCoffee: 76gMoney: $2.5
- Check resources sufficient?
a.When the user chooses a drink, the program should check if there are enoughresources to make that drink.b.E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It shouldnot continue to make the drink but print: “
Sorry there is not enough water.​
”c.The same should happen if another resource is depleted, e.g. milk or coffee.
- Process coins.
a.If there are sufficient resources to make the drink selected, then the program shouldprompt the user to insert coins.b.Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01c.Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
- Check transaction successful?
a.Check that the user has inserted enough money to purchase the drink they selected.E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins theprogram should say 
“Sorry that's not enough money. Money refunded.​
”.b.But if the user has inserted enough money, then the cost of the drink gets added to themachine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100mlMilk: 50mlCoffee: 76gMoney: $2.5
 c.If the user has inserted too much money, the machine should offer change.


## How do I get the project on my local machine?
- git clone https://github.com/MohamedSbaih/coffee-machine.git
- git code .

