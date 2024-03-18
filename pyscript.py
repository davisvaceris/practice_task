import random
import time

def russian_roulette():
    print("Welcome to Russian Roulette!")
    players = int(input("Enter the number of players: "))
    bullets = random.randint(1, 6)  # Randomly place the bullet in one of the 6 chambers
    print("Spin the chamber...")
    time.sleep(2)  # Simulate spinning the chamber
    print("Pull the trigger and hope for the best...")

    for i in range(1, players + 1):
        input(f"Player {i}, press Enter to pull the trigger...")
        if bullets == i:
            print(f"Player {i} has been shot! Game over!")
            break
        else:
            print(f"Player {i} survives!")

    print("Game over.")

if __name__ == "__main__":
    russian_roulette()
