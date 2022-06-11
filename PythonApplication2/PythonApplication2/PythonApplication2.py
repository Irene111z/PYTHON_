
text = "I learn Python DAY"
day = 1
print(text, day)
print(text + str(day)) #convert day to string
del day

day = "1"
print(7+int(day)) #convert day to int
print(text + str(7+int(day)))
del day

alldays = int(input("\nEnter all count of days: "))
skipped = int(input("Enter count of days you skipped: "))
day=alldays-skipped
print(text, day)
# or
day = int(input("\nEnter all count of days: "))
skipped = int(input("Enter count of days you skipped: "))
day -= skipped
print(text, day)

name = "Irina"
print(name*3)