#ealmonte32

print("==================================================")
print("\nMonthly loan payment calculator.\n")

"""
We only want integers as input so we make the type int.
For the interest rate we should use a float because interest rates
are sometimes given in decimal format such as 3.5 or 8.2, etc.
For the monthly interest rate variable we should make it easier for the user
to enter the interest rate just like they see on a paper or document, which is
usually given in the APR format (annual percentage rate), so if we allow the
rate to be entered this way, we simply need to convert the entered number
into a percent so we have to divide by 100, ex: 8% interest rate is 0.08 in decimal,
then we divide that by 12 to get a monthly rate.
"""
loanAmount = int(input(" Enter the total loan amount: $"))
monthlyInterestRate = ((float(input(" Enter the interest rate of the loan: ")) / 100) / 12)
numberOfYears = int(input(" Enter the number of years for the loan: "))
monthlyPayment = ((loanAmount*monthlyInterestRate)/(1-(1/((1+monthlyInterestRate)**(numberOfYears*12)))))

"""
After we calculate above, we print out the monthly payment to user.
I also format the floating decimal to only show two decimal points.
The only reason i convert the monthlyPayment(format_payment) to a string
is to display the dollar sign right next to it because when concatenating
with a +, you cannot simply mix strings and integers
"""

format_payment = "{:.2f}".format(monthlyPayment)
print(" Using the above information, your monthly payment would be: $" + str(format_payment), "\n")

"""
One alternative way to create the formula without making a big long line
is to either use multiline continuation which is using the backslash before new line,
or you can break down the formula into different variables such as:

top = (loanAmount * monthlyInterestRate)
bottom = ( (1+monthlyInterestRate)**(numberOfYears*12) )
monthlyPayment = (top / (1 - (1 / bottom)))

As you can see, this looks much cleaner.
"""

