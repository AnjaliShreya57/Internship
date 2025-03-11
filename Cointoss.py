import random

def coin_toss():
    return random.choice(["Heads", "Tails"])

def multiple_tosses():
    while True:
        try:
            num_flips = int(input("Enter the number of times you want to flip the coin: "))
            if num_flips <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        heads_count = 0
        tails_count = 0

        for _ in range(num_flips):
            result = coin_toss()
            print(result)
            if result == "Heads":
                heads_count += 1
            else:
                tails_count += 1

        total_flips = heads_count + tails_count
        heads_percentage = (heads_count / total_flips) * 100
        tails_percentage = (tails_count / total_flips) * 100

        print(f"\nResults:")
        print(f"Heads: {heads_count} ({heads_percentage:.2f}%)")
        print(f"Tails: {tails_count} ({tails_percentage:.2f}%)\n")

        again = input("Do you want to flip again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing!")
            break
        
multiple_tosses()
