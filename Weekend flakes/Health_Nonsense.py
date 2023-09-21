
age = int(input("Please enter your age: "))

max_heart_rate = 220 - age

min_target_rate = 0.5 * max_heart_rate  # 50% of max heart rate
max_target_rate = 0.85 * max_heart_rate  # 85% of max heart rate

print("Your maximum heart rate is:", max_heart_rate, "beats per minute")
print("Your target heart rate range is between", min_target_rate, "and", max_target_rate, "beats per minute")


