#Wilson Xu, 2/25/23, section 03, Assignment 04 part 2

import random

dice_sizes = [4, 6, 8, 10, 12, 20]

# Prompt user for the dice size
while True:
    size = int(input("How many sides on your dice (4, 6, 8, 10, 12 or 20)? "))
    if size in dice_sizes:
        break
    else:
        print("Invalid size, try again.")

print("Thanks, here we go!\n")

# Setup start from 0
high_count = 0
high_low_count = 0
even_count = 0
odd_count = 0
mixed_count = 0
sum_value_count = 0
neighbor_count = 0
middle_count = 0
doubles_count = 0
snake_eyes_count = 0


total_rolls = 0
total_score_1 = 0
total_score_2 = 0

# Start rolling the dice till user get snake eyes and stop
roll_number = 1
while True:
    roll_1 = random.randint(1, size)
    roll_2 = random.randint(1, size)
    print(f"{roll_number}. die roll is *{roll_1}* and *{roll_2}*", end=" ")

    if roll_1 == roll_2:
        if roll_1 == 1:
            print("Odd! Doubles! Snake Eyes!")
            snake_eyes_count += 1
            doubles_count += 1
            break
        else:
            print("Even! Doubles!")
            doubles_count += 1
    else:
        roll_sum = roll_1 + roll_2
        roll_min = min(roll_1, roll_2)
        roll_max = max(roll_1, roll_2)
        labels = []
        if roll_sum == size:
            labels.append("Sum Value")
        if roll_max == size:
            labels.append("High")
        if roll_min == 1 and roll_max == size:
            labels.append("High / Low")
        if roll_1 % 2 == roll_2 % 2:
            if roll_1 % 2 == 0:
                labels.append("Even")
            else:
                labels.append("Odd")
        else:
            labels.append("Mixed")
        if abs(roll_1 - roll_2) == 1:
            labels.append("Neighbor")
        if roll_min + 1 == roll_max - 1 == size // 2:
            labels.append("Middle")
        print(" ".join(labels) + "!")

        # Update the counters for the different roll types
        for label in labels:
            if label == "High":
                high_count += 1
            elif label == "High / Low":
                high_low_count += 1
            elif label == "Even":
                even_count += 1
            elif label == "Odd":
                odd_count += 1
            elif label == "Mixed":
                mixed_count += 1
            elif label == "Sum Value":
                sum_value_count += 1
            elif label == "Neighbor":
                neighbor_count += 1
            elif label == "Middle":
                middle_count += 1

    # Update total roll count and score totals
    total_rolls += 1
    total_score_1 += roll_1
    total_score_2 += roll_2
    roll_number += 1

# Calculate the average roll for each die
avg_roll_1 = total_score_1 / total_rolls
avg_roll_2 = total_score_2 / total_rolls

# Print out results
print(f"\nYou finally got snake eyes on roll #{roll_number-1}")
print(f"Along the way you rolled HIGH {high_count} time(s). ({100 * high_count / total_rolls:.2f}% of all rolls)")
print(f"Along the way you rolled HIGH / LOW {high_low_count} time(s). ({100 * high_low_count / total_rolls:.2f}% of all rolls)")
print(f"Along the way you rolled EVEN {even_count} time(s). ({100 * even_count / total_rolls:.2f}% of all rolls)")
print(f"Along the way you rolled ODD {odd_count} time(s). ({100 * odd_count / total_rolls:.2f}% of all rolls)")
print(f"Along the way you rolled MIXED {mixed_count} time(s). ({100 * mixed_count / total_rolls:.2f}% of all rolls)")
print(f"Along the way you rolled SUM VALUE {sum_value_count} time(s). ({100 * sum_value_count / total_rolls:.2f}% of all rolls)")
print(f"Along the way you rolled NEIGHBOR {neighbor_count} time(s). ({100 * neighbor_count / total_rolls:.2f}% of all rolls)")
print(f"Along the way you rolled MIDDLE {middle_count} time(s). ({100 * middle_count / total_rolls:.2f}% of all rolls)")
print(f"Along the way you rolled DOUBLE {doubles_count} time(s). ({100 * doubles_count / total_rolls:.2f}% of all rolls)")
print(f"Along the way you rolled SNAKE EYES {snake_eyes_count} time(s). ({100 * snake_eyes_count / total_rolls:.2f}% of all rolls)")
print(f"Average roll for die #1: {avg_roll_1:.2f}")
print(f"Average roll for die #2: {avg_roll_2:.2f}")
