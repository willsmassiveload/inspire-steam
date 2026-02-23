class FighterCharacter:

    def __init__(self, role, health, damage, speed):   # FIX 1
        self.character_role = role
        self.character_health = health
        self.character_damage = damage
        self.character_speed = speed

    def run(self, direction):
        print(f"Game log: {self.character_role} runs {direction} at speed {self.character_speed}")

    def report_status(self):
        print(f"\nCharacter Log:")
        print(f"Role: {self.character_role}")
        print(f"Health: {self.character_health}")
        print(f"Damage: {self.character_damage}")
        print(f"Speed: {self.character_speed}")   # FIX 2
        print("__________")

    def kick(self, opponent):
        damage = self.character_damage
        opponent.character_health -= damage      # FIX 3 (subtract, not divide)
        print(f"Game Log: {self.character_role} deals {damage} damage to {opponent.character_role}.")

    def takle(self, opponent):
        damage = self.character_damage
        opponent.character_speed -= damage       # FIX 4
        print(f"Game Log: {self.character_role} tackles {opponent.character_role} reducing speed by {damage}.")


# Create characters
ninja_character = FighterCharacter("Ninja", 100, 40, 120)
warrior_character = FighterCharacter("Warrior", 160, 80, 80)


# Initial Status
ninja_character.report_status()
warrior_character.report_status()

# PROBLEM 1
ninja_character.run("Up")
ninja_character.kick(warrior_character)

print("\nAfter Kick:")
ninja_character.report_status()
warrior_character.report_status()

# PROBLEM 2
warrior_character.takle(ninja_character)

print("\nAfter Tackle:")
ninja_character.report_status()
warrior_character.report_status()


class FighterCharacter:

    def __init__(self, role, health, damage, speed):
        self.character_role = role
        self.character_health = health
        self.character_damage = damage
        self.character_speed = speed

    def run(self, direction):
        print(f"Game log: {self.character_role} runs {direction} at speed {self.character_speed}")

    def report_status(self):
        print(f"\nCharacter Log:")
        print(f"Role: {self.character_role}")
        print(f"Health: {self.character_health}")
        print(f"Damage: {self.character_damage}")
        print(f"Speed: {self.character_speed}")
        print("__________")

    def kick(self, opponent):
        damage = self.character_damage
        opponent.character_health -= damage
        print(f"Game Log: {self.character_role} deals {damage} damage to {opponent.character_role}.")

    def takle(self, opponent):
        damage = self.character_damage
        opponent.character_speed -= damage
        print(f"Game Log: {self.character_role} tackles {opponent.character_role} reducing speed by {damage}.")


# Create characters
ninja_character = FighterCharacter("Ninja", 100, 40, 120)
warrior_character = FighterCharacter("Warrior", 160, 80, 80)


# Initial Status
ninja_character.report_status()
warrior_character.report_status()

# Test kick (Problem 1)
ninja_character.run("Up")
ninja_character.kick(warrior_character)

print("\nAfter Kick:")
ninja_character.report_status()
warrior_character.report_status()


# ✅ Added lines to test takle (Problem 2)
warrior_character.takle(ninja_character)
ninja_character.report_status()
warrior_character.report_status()