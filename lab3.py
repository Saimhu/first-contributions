dice_options = list(range(1, 7))
print("Dice options:", dice_options)

weapons = ["Sword", "Axe", "Bow", "Dagger", "Spear"]
print("Weapons:")
for weapon in weapons:
    print(weapon)

def get_combat_strength(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 6:
                return value
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

combat_strength = get_combat_strength("Enter combat strength (1-6): ")
m_combat_strength = get_combat_strength("Enter mCombat strength (1-6): ")
print(f"Your combat strength: {combat_strength}, mCombat strength: {m_combat_strength}")

print("Fight sequence:")
for j in range(1, 20, 2):
    print(f"Round {j}")
    if j == 11:
        print("Breaking loop at j = 11")
        break
