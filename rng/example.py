seed_number = int(input("Please enter a four digit number:\n[####] "))
number = seed_number
already_seen = set()
counter = 0

while number not in already_seen:
    counter += 1
    already_seen.add(number)
    a_number = int(str(number * number).zfill(8))
    number = int(str(number * number).zfill(8)[2:6])
    print(f"#{counter}: {number}")

print("We began with {}, and"
      " have repeated ourselves after {} steps"
      " with {}.".format(seed_number, counter, number))
