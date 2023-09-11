# Description
The code works for the sample input provided by the instructor with additional entries. 
    - Checking for right command syntax and provides error msg for incorrect input 
        + Ignores empty space before/after user input
    - Checks to verify that enough money has been put into the machine and whether it has enough money to make change
    - Checks to see if the item is in the inventory

## Sample Input

add item chips 20 $.50  
add item coke 5 $.75  
add item diet coke 5 $.75 
buy item coke 0 3 0 0 0  
inventory  
buy item chips 1 0 0 0 0  
buy item diet coke 0 2 0 0 0
inventory  
history  
balance
afdja;sdflkjalfjkai
add cookies 
add cookies 2 $1.00
help
        add item cookies 3 $5,00
                    add item cookies 3 $5.00            
buy item cookies 1 1 1 40 20
buy item cookies 1 1 1 40 200
buy item cookies 1 1 1 40 2000
history
balance

## Output for Sample Input

----------------------------------------
CSCE086 Vending Machine
----------------------------------------

What do you want?: add item chips 20 $.50  

-------------------------------------------------------------------------------------
          Item            |         Quantity          |           Price          
-------------------------------------------------------------------------------------
          chips           |            20             |           $ 0.5          



What do you want?: add item coke 5 $.75  

-------------------------------------------------------------------------------------
          Item            |         Quantity          |           Price          
-------------------------------------------------------------------------------------
          chips           |            20             |           $ 0.5          
          coke            |             5             |          $ 0.75          



What do you want?: add item diet coke 5 $.75 

-------------------------------------------------------------------------------------
          Item            |         Quantity          |           Price          
-------------------------------------------------------------------------------------
          chips           |            20             |           $ 0.5          
          coke            |             5             |          $ 0.75          
        diet coke         |             5             |          $ 0.75          



What do you want?: buy item coke 0 3 0 0 0  

----------------------------------------
$0.75 paid for coke (cost = $0.75)
Change given is:  $0.0
-----------------------------------------------------------------------------------------------
       Dollar        |     Quarter     |      Dime       |     Nickel      |      Penny     
-----------------------------------------------------------------------------------------------
         0           |        0        |        0        |        0        |        0       
-----------------------------------------------------------------------------------------------

Vending Machine balance is:  $10.75
-----------------------------------------------------------------------------------------------
       Dollar        |     Quarter     |      Dime       |     Nickel      |      Penny     
-----------------------------------------------------------------------------------------------
         5           |       13        |       10        |       10        |       100      
-----------------------------------------------------------------------------------------------




What do you want?: inventory  

-------------------------------------------------------------------------------------
          Item            |         Quantity          |           Price          
-------------------------------------------------------------------------------------
          chips           |            20             |           $ 0.5          
          coke            |             4             |          $ 0.75          
        diet coke         |             5             |          $ 0.75          



What do you want?: buy item chips 1 0 0 0 0  

----------------------------------------
$1.0 paid for chips (cost = $0.5)
Change given is:  $0.5
-----------------------------------------------------------------------------------------------
       Dollar        |     Quarter     |      Dime       |     Nickel      |      Penny     
-----------------------------------------------------------------------------------------------
         0           |        2        |        0        |        0        |        0       
-----------------------------------------------------------------------------------------------

Vending Machine balance is:  $11.25
-----------------------------------------------------------------------------------------------
       Dollar        |     Quarter     |      Dime       |     Nickel      |      Penny     
-----------------------------------------------------------------------------------------------
         6           |       11        |       10        |       10        |       100      
-----------------------------------------------------------------------------------------------




What do you want?: buy item diet coke 0 2 0 0 0

Error: You didn't put in enough money.



What do you want?: inventory

-------------------------------------------------------------------------------------
          Item            |         Quantity          |           Price          
-------------------------------------------------------------------------------------
          chips           |            19             |           $ 0.5          
          coke            |             4             |          $ 0.75          
        diet coke         |             5             |          $ 0.75          



What do you want?: history  

----------------------------------------
Input Log
----------------------------------------
add item chips 20 $.50  
add item coke 5 $.75  
add item diet coke 5 $.75 
buy item coke 0 3 0 0 0  
inventory  
buy item chips 1 0 0 0 0  
buy item diet coke 0 2 0 0 0
inventory
history  



What do you want?: balance

Vending Machine balance is:  $11.25
-----------------------------------------------------------------------------------------------
       Dollar        |     Quarter     |      Dime       |     Nickel      |      Penny     
-----------------------------------------------------------------------------------------------
         6           |       11        |       10        |       10        |       100      
-----------------------------------------------------------------------------------------------




What do you want?: afdja;sdflkjalfjkai

Error: Invalid syntax. Type 'help' for more info.



What do you want?: add cookies 

Error: Invalid syntax. Type 'help' for more info.



What do you want?: add cookies 2 $1.00

Error: Invalid syntax. Type 'help' for more info.



What do you want?: help

-------------------------------------------------------------------------------------------------------------------
                               |                           |                                                        
Command Syntax                 | Example                   | Description              
                               |                           |                                                        
-------------------------------------------------------------------------------------------------------------------
balance                        | balance                   | Shows the balance        
-------------------------------------------------------------------------------------------------------------------
history                        | history                   | Prints list of transactions
-------------------------------------------------------------------------------------------------------------------
inventory                      | inventory                 | Prints available items with name and ID
-------------------------------------------------------------------------------------------------------------------
add item <str> <int> <float>   | add item chips 2 $1.00    | Add an item name qty price
-------------------------------------------------------------------------------------------------------------------
buy item \{5\}                 | buy item chips 1 2 2 4 3  | Buys an item with # dollars, quarters, dimes, nickles, 
                               |                           | pennies. It also shows change given and the remaining  
                               |                           | balance with currency distribution.  For change, the   
                               |                           | machine  uses the largest denominator of curenncy that 
                               |                           | is available.                                          
-------------------------------------------------------------------------------------------------------------------
exit                           | exit                      | Exit the vending machine 
-------------------------------------------------------------------------------------------------------------------



What do you want?:         add item cookies 3 $5,00

Error: Invalid syntax. Type 'help' for more info.



What do you want?:                     add item cookies 3 $5.00            

-------------------------------------------------------------------------------------
          Item            |         Quantity          |           Price          
-------------------------------------------------------------------------------------
          chips           |            19             |           $ 0.5          
          coke            |             4             |          $ 0.75          
        diet coke         |             5             |          $ 0.75          
         cookies          |             3             |           $ 5.0          



What do you want?: buy item cookies 1 1 1 40 20

Error: You didn't put in enough money.



What do you want?: buy item cookies 1 1 1 40 200

----------------------------------------
$5.35 paid for cookies (cost = $5.0)
Change given is:  $0.35
-----------------------------------------------------------------------------------------------
       Dollar        |     Quarter     |      Dime       |     Nickel      |      Penny     
-----------------------------------------------------------------------------------------------
         0           |        1        |        1        |        0        |        0       
-----------------------------------------------------------------------------------------------

Vending Machine balance is:  $16.25
-----------------------------------------------------------------------------------------------
       Dollar        |     Quarter     |      Dime       |     Nickel      |      Penny     
-----------------------------------------------------------------------------------------------
         7           |       11        |       10        |       50        |       300      
-----------------------------------------------------------------------------------------------




What do you want?: buy item cookies 1 1 1 40 2000

----------------------------------------
$23.35 paid for cookies (cost = $5.0)
Change given is:  $18.35
-----------------------------------------------------------------------------------------------
       Dollar        |     Quarter     |      Dime       |     Nickel      |      Penny     
-----------------------------------------------------------------------------------------------
         8           |       12        |       11        |       90        |       175      
-----------------------------------------------------------------------------------------------

Vending Machine balance is:  $21.25
-----------------------------------------------------------------------------------------------
       Dollar        |     Quarter     |      Dime       |     Nickel      |      Penny     
-----------------------------------------------------------------------------------------------
         0           |        0        |        0        |        0        |      2125      
-----------------------------------------------------------------------------------------------




What do you want?: history

----------------------------------------
Input Log
----------------------------------------
add item chips 20 $.50  
add item coke 5 $.75  
add item diet coke 5 $.75 
buy item coke 0 3 0 0 0  
inventory  
buy item chips 1 0 0 0 0  
buy item diet coke 0 2 0 0 0
inventory
history  
balance
afdja;sdflkjalfjkai
add cookies 
add cookies 2 $1.00
help
        add item cookies 3 $5,00
                    add item cookies 3 $5.00            
buy item cookies 1 1 1 40 20
buy item cookies 1 1 1 40 200
buy item cookies 1 1 1 40 2000
history



What do you want?: balance

Vending Machine balance is:  $21.25
-----------------------------------------------------------------------------------------------
       Dollar        |     Quarter     |      Dime       |     Nickel      |      Penny     
-----------------------------------------------------------------------------------------------
         0           |        0        |        0        |        0        |      2125      
-----------------------------------------------------------------------------------------------




What do you want?: exi

Error: Invalid syntax. Type 'help' for more info.



What do you want?: exit

----------------------------------------
Completing transaction...
----------------------------------------
