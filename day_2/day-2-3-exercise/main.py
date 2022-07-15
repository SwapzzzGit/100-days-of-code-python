age = input("What is your current age?")
final_age = 90 - int(age)
days = 365 * final_age
week = 52 * final_age
months = 12 * final_age

print(f"You have {days} days, {week} weeks, and {months} months left.")