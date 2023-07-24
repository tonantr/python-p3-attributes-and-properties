class Human:
    # class attributes
    species = 'Homo sapiens'

    def __init__(self, name):
        # instance attributes
        self.name = name
    
    def get_age(self):
        print("Retrieving age.")
        return self._age

    def set_age(self, age):
        if (type(age) in (int, float)) and (0 <= age <= 120):
            print(f"Setting age to { age }.")
            self._age = age

        else:
            print("Age must be a number between 0 and 120.")

    age = property(get_age, set_age,)

guido = Human("Guido")

guido.species
# => Homo sapiens
guido.name
# => Guido

# Changing species and name using dot notation
guido.species = "Python programmer"
guido.name = "Guido van Rossum"

guido.species
# => Python programmer
guido.name
# => Guido van Rossum

# Adding new attributes using dot notation
guido.nationality = "Dutch"
guido.nationality
# => Dutch

# Getting
guido.name
# => Guido van Rossum
getattr(guido, "name")
# => Guido van Rossum

#Setting
guido.nationality = "Dutch"
setattr(guido, "nationality", "Dutch")

my_attr = "is_a_friend"
getattr(guido, my_attr, False)
# => False

# Oh no! Let's try again.
setattr(guido, my_attr, True)
getattr(guido, my_attr, False)
# => True


guido.age = 0
# => Setting age to 0.
guido.age = False
# => Age must be a number between 0 and 120
guido.age = 66
# => Setting age to 66.
guido.age
# => Retrieving age.
# => 66
