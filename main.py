age = input("\nWhat is your current age? ")
int_age=int(age)
left_years=90-int_age
days=left_years*365
weeks=left_years*52
months=left_years*12
print(f"You have {days} days, {weeks} weeks, and {months} months left")
