# INF360 - Programming in Python
# Clifford Anderson
# Final Project

'''This program is intended to help people better understand their financial health (or lack thereof), identify areas in which they might be able to improve their finances,
   and provide concrete suggestions as to how to do so. I envision it is a financial diagnostic tool. As the program progresses, the user is asked detailed questions
   about their income, expenses, discretionary spending, et cetera; areas identified as problematic are flagged and added to a list which is reviewed immediately prior to
   termination of the program. If no areas are flagged, the program provides the user with a clean bill of financial health. (Note: I do not represent myself as an accountant
   or a financial wizard; this kind of thing interests me and I wanted to see if I could implement my idea in code.) Thus far, the code *mostly* works as intended; I plan
   to keep refining the existing code (e.g., detailed questions regarding the breakdown of discretionary spending) and I also plan to add further diagnostic sections (e.g.,
   mortgage payments, amount put into savings, et cetera).'''

import logging
import sys
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

from pathlib import Path ##this enables us to open and write to a text file

try:
    import functions as fn
except:
    logging.critical('Missing functions.py')
    print('Missing functions.py! Program is closing.')
    sys.exit()

try:
    import FinancialHealth as f
except:
    logging.critical('Missing Financialhealth.py')
    print('Missing FinancialHealth.py! Program is closing.')
    sys.exit()

print('This program will help you review your financial health, identify potentially problematic areas, and take corrective action if needed.')
print('Please respond to yes or no questions asked with either "yes" or "no." This program will not recognize "y" or "n". \nAnswers are not case sensitive.')
print('Be advised that inputting more than two decimal places for numeric values will result in the values being rounded to the appropriate figure.')
logging.disable(logging.CRITICAL)

while True: ##this while loop enables us to run the program multiple times if the user desires
    print('What is your monthly income?')
    value = fn.requestNumericInput()
    income = fn.validateNumericInput(value)
    income = fn.confirmUserInput(income) ##this line of code utilizes the assignment operator to create a new float object for income, as float is an immutable class
    (logging.info('So far, so good'))
    print('What are your total monthly expenses for bills (including mortgage or rent).')
    value = fn.requestNumericInput()
    expenses = fn.validateNumericInput(value)
    expenses = fn.confirmUserInput(expenses)
    (logging.info('So far, so good'))
    info = f.FinancialHealth(income, expenses) ##this line of code calls the FinancialHealth class constructor, initializes its values, creates a FinancialHealth object and 'fills in' the bulk of the rest of the program
    (logging.info('So far, so good'))
    print('Would you like to save your financial health report to a text file? Please enter yes or no.')
    answer = input()
    answer = fn.validateYesOrNo(answer)

    if (answer.casefold() == 'yes'):
        newFile = open('financialHealth.txt', 'w') #this opens a file and enables us to write the contents of our financial health report to it
        newFile.write(info.text)
        logging.critical('Module not found error')
        newFile.close() #this closes the new file

    print('Would you like to run the program again? Please enter yes or no.')
    answer = input()
    answer = fn.validateYesOrNo(answer)

    if (answer.casefold() == 'yes'):
        continue
    elif (answer.casefold() == 'no'):
        print('Thank you for using this program! Goodbye.')
        break

    (logging.info("Aaaaaand we're clear!"))
