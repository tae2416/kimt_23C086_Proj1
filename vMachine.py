# Print error msg
def errorMsg(msgType):
    match msgType:
        case 'notEnough':
            print('Error: You didn\'t put in enough money.')
        case 'noMoney':
            print('Error: No money for change in the machine.')
        case 'noInv':
            print('Error: Item is not in inventory.')
        case other:
            print('Error: Invalid syntax. Type \'help\' for more info.')

# Remove empty spaces from input command
def rmEmpty(command):
    while command[0] == '':
        command = command[1:]
    while command[-1] == '': 
        command = command[:-1]
    return command

# Check string for decimal number
def isFloat(strNum):
    try:
        float(strNum)
        return True
    except ValueError:
        return False
    
# Verify whether a list of strings contains numbers
def hasNum(list):
    for x in list:
        if x.isdigit():
            return True
    return False

# Verify that 'add item' command has correct syntax and execute if correct
def verifyAdd(command, invQ, invP):
    match command[1]:
        case 'item' if len(command) > 2 and command[2].isdigit() != True:    
            # Command has 'add item' and specifies 'item name'
                    
            # Determine index of quantity in user input                
            qInd = 0;
            while command[qInd].isdigit() != True and qInd < len(command):
                qInd += 1
            
            # Get item name        
            j = 2
            itemName = command[j]   
            while j < qInd-1:
                j += 1
                itemName = itemName + ' ' + command[j]

            # Verify there is nothing after price and ensure price has the right format
            if (len(command[qInd:len(command)]) == 2 and \
                command[qInd+1][0] == '$' and isFloat(command[qInd+1][1:len(command[qInd+1])])):      
                # Add item to inventory
                invQ[itemName] = int(command[qInd])
                invP[itemName] = float(command[qInd+1][1:len(command[qInd+1])])     

                # Print inventory to screen
                printInv(invQ, invP)                       
            else:
                # Print error msg
                errorMsg('')
        case other:
            # Print error msg
            errorMsg('')
    return invQ, invP

# Calculate and return the currency value in cents
def calcCurr(bal):
    return int(bal['dollar'])*100 + int(bal['quarter'])*25 + \
           int(bal['dime'])*10 + int(bal['nickel'])*5 + \
           int(bal['penny'])

# Calculate whether change can be made and return in number of dollars,
# quarters, dimes, nickels, and pennies
def getDenom(changeC, bal):
    deNom = {}

    deNom['dollar'] = changeC // 100         # Calc number of dollars
    changeC = changeC % 100                  # Calc remaining change
    if deNom['dollar'] > bal['dollar']:
        changeC += (deNom['dollar'] - bal['dollar']) * 100
        deNom['dollar'] = bal['dollar']
            
    deNom['quarter'] = changeC // 25         # Calc number of quarters
    changeC = changeC % 25                   # Calc remaining change
    if deNom['quarter'] > bal['quarter']:
        changeC += (deNom['quarter'] - bal['quarter']) * 25
        deNom['quarter'] = bal['quarter']

    deNom['dime'] = changeC // 10            # Calc number of dimes
    changeC = changeC % 10                   # Calc remaining change
    if deNom['dime'] > bal['dime']:
        changeC += (deNom['dime'] - bal['dime']) * 10
        deNom['dime'] = bal['dime']
    
    deNom['nickel'] = changeC // 5           # Calc number of nickels
    changeC = changeC % 5                    # Calc remaining change
    if deNom['nickel'] > bal['nickel']:
        changeC += (deNom['nickel'] - bal['nickel']) * 5
        deNom['nickel'] = bal['nickel']

    deNom['penny'] = changeC                 # Calc number of pennies

    return deNom

def updateInv(itemName, invQ):
    # Remove purchased item from imnventory
    invQ[itemName] -= 1 
    return invQ

def updateBal(changeS, bal, inOut):
    # Update balance to reflect change given to customer
    match inOut:
        case 'in':    
            for x in bal.keys():
                bal[x] = bal[x] + changeS[x]
        case 'out':
            for x in bal.keys():
                bal[x] = bal[x] - changeS[x]
    return bal

# Print denomination to screen
def printDenom(bal):
    print('{:-^95s}'.format('-'))
    print('{: ^20s} | {: ^15s} | {: ^15s} | {: ^15s} | {: ^15s}'\
        .format('Dollar', 'Quarter', 'Dime', 'Nickel', 'Penny'))
    print('{:-^95s}'.format('-'))
    print('{: ^20} | {: ^15} | {: ^15} | {: ^15} | {: ^15}'\
        .format(bal['dollar'], bal['quarter'], bal['dime'], \
        bal['nickel'], bal['penny']))    
    print('{:-^95s}'.format('-'))
    print('')

# Print inventory to screen
def printInv(invQ, invP):
    print('{:-^85s}'.format('-'))
    print('{: ^25s} | {: ^25s} | {: ^25s}'.format('Item', 'Quantity', 'Price'))
    print('{:-^85s}'.format('-'))
    for x in invQ:
        print('{: ^25s} | {: ^25d} | {: ^25s}'.format(x, invQ[x], '$ '+str(invP[x])))

# Verify that 'buy item' command has correct syntax and execute if correct
# Returns updated balance and quantities (bal, invQ)
def verifyBuy(command, bal, invQ, invP):
    match command[1]:
        case 'item' if len(command) > 2 and command[2].isdigit() != True:    
            # Command has 'buy item' and specifies 'item name'
                                
            # Determine index of quantity in user input                
            qInd = 0;
            while command[qInd].isdigit() != True and qInd < len(command):
                qInd += 1
            
            # Get item name        
            j = 2
            itemName = command[j]   
            while j < qInd-1:
                j += 1
                itemName = itemName + ' ' + command[j]
        
            # Verify that the item exists 
            if itemName in invQ and invQ[itemName] > 0:            
                # Verify there is nothing after specification of pennies and verify 
                # that specified quantities are integers            
                if (len(command[qInd:len(command)]) == 5 and \
                    command[qInd+1].isdigit() and command[qInd+2].isdigit() and \
                    command[qInd+3].isdigit() and command[qInd+4].isdigit()):    

                    # Generate payment denomination dict and add to balance
                    paiD = {
                        'dollar': int(command[qInd]),
                        'quarter': int(command[qInd+1]), 
                        'dime': int(command[qInd+2]), 
                        'nickel': int(command[qInd+3]),
                        'penny': int(command[qInd+4]), 
                    }
                    bal = updateBal(paiD, bal, 'in')
                                        
                    # Calculate payment and cost of item in cents
                    payC = calcCurr(paiD)
                    costC = int(invP[itemName]*100)

                    # Verify that customer paid enough money
                    changeC = payC - costC      # Calculate change in cents
                    if changeC >= 0:                           
                        balC = calcCurr(bal)        # Current balance in machine

                        # If there is enough in the balance update inventory and balance to reflect purchase
                        if balC > changeC:
                            changeS = getDenom(changeC, bal)      # Calc denomination quantities
                            
                            invQ = updateInv(itemName, invQ)                            
                            bal = updateBal(changeS, bal, 'out')
                            
                            # Print output
                            print('{:-^40s}'.format('-'))
                            print(f'${payC/100} paid for {itemName} (cost = ${costC/100})')                  
                            print(f'Change given is:  ${changeC/100}')
                            printDenom(changeS)
                            print(f'Vending Machine balance is:  ${calcCurr(bal)/100}')
                            printDenom(bal)
                        else:
                            errorMsg('noMoney')
                    else:
                        # Print error msg and return money
                        errorMsg('notEnough')
                        bal = updateBal(paiD, bal, 'out')
                else:
                    # Print error msg
                    errorMsg('')
            else:
                # Print error msg
                errorMsg('noInv')
        case other:
            # Print error msg
            errorMsg('')

    return bal, invQ


##### Main program
# Initialize variables
uInput = 'run'
quant = dict()
price = dict()
hist = list()
balance = {         # Initial change balance in vending machine
    'dollar': 5,
    'quarter': 10, 
    'dime': 10, 
    'nickel': 10,
    'penny': 100 
}

print('{:-^40s}'.format('-'))
print('CSCE086 Vending Machine')
print('{:-^40s}'.format('-'))
print('')

while uInput[0] != 'exit' or len(uInput) != 1:
    # Read in user input and keep track of input history
    uInput = input('What do you want?: ')    
    hist.append(uInput)
    uInput = uInput.split(' ')
    uInput = rmEmpty(uInput)
    print('')

    match uInput[0]:
        case 'exit' if len(uInput) ==1:
            # Exit program
            print('{:-^40s}'.format('-'))
            print('Completing transaction...')
            print('{:-^40s}'.format('-'))
        case 'inventory' if len(uInput) ==1:
            # Print inventory
            printInv(quant, price)
        case 'balance' if len(uInput) ==1:
            # Print balance
            print(f'Vending Machine balance is:  ${calcCurr(balance)/100}')
            printDenom(balance)
        case 'history' if len(uInput) ==1:
            # Print history
            print('{:-^40s}'.format('-'))
            print('Input Log')
            print('{:-^40s}'.format('-'))
            for x in hist:
                print(x)
        case 'help' if len(uInput) ==1:
            # Print help msg
            print('{:-^115s}'.format('-'))
            print('{: <30s} | {: <25s} | {: <55s}'.format('', '', ''))
            print('{: <30s} | {: <25s} | {: <25s}'.format('Command Syntax', 'Example', 'Description'))
            print('{: <30s} | {: <25s} | {: <55s}'.format('', '', ''))
            print('{:-^115s}'.format('-'))
            print('{: <30s} | {: <25s} | {: <25s}'.format('balance', 'balance', 'Shows the balance'))
            print('{:-^115s}'.format('-'))
            print('{: <30s} | {: <25s} | {: <25s}'.format('history', 'history', 'Prints list of transactions'))
            print('{:-^115s}'.format('-'))
            print('{: <30s} | {: <25s} | {: <25s}'.format('inventory', 'inventory', 'Prints available items with name and ID'))
            print('{:-^115s}'.format('-'))
            print('{: <30s} | {: <25s} | {: <25s}'.format('add item <str> <int> <float>', \
                'add item chips 2 $1.00', 'Add an item name qty price'))
            print('{:-^115s}'.format('-'))
            print('{: <30s} | {: <25s} | {: <55s}'.format('buy item \{5\}', 'buy item chips 1 2 2 4 3', \
                'Buys an item with # dollars, quarters, dimes, nickles, ')) 
            print('{: <30s} | {: <25s} | {: <55s}'.format('', '', \
                'pennies. It also shows change given and the remaining '))
            print('{: <30s} | {: <25s} | {: <55s}'.format('', '', \
                'balance with currency distribution.  For change, the '))
            print('{: <30s} | {: <25s} | {: <55s}'.format('', '', \
                'machine  uses the largest denominator of curenncy that '))
            print('{: <30s} | {: <25s} | {: <55s}'.format('', '', \
                'is available.'))
            print('{:-^115s}'.format('-'))
            print('{: <30s} | {: <25s} | {: <25s}'.format('exit', 'exit', 'Exit the vending machine'))
            print('{:-^115s}'.format('-'))
        case 'add' if len(uInput) > 1 and hasNum(uInput):     # Verify that command includes numbers
            # Verify command format and execute
            quant, price = verifyAdd(uInput, quant, price)
        case 'buy' if len(uInput) > 1 and hasNum(uInput):     # Verify that command includes numbers
            # Verify command format and execute
            balance, quant = verifyBuy(uInput, balance, quant, price)
        case other:
            # Print error msg
            errorMsg('')
            
    for k in range(3):
        print('')
    

