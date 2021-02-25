num_input = int(input("Enter a number: "))

"""            
check_even = (num_input % 2)

if check_even != 0:
    print("Not even")
else:
    print("Even")
"""

check_minutes = (num_input / 60)

print(check_minutes)

"""
when testing integers for minutes to seconds
test with int(#.9999) ex: int(4.899)
then assign this to a variable
result = (int(4.899))
or
result 4.899
then math.ceil(result) will show as a whole number

so if number of minutes is entered as 65
then it will divide by 60
result of 1 will have remainder as 0.08888833

to make this into seconds we have to multiply that by 60
and result in this case would give 4.9999
which we then take the math.ceil of it and give as full seconds of 5
"""
