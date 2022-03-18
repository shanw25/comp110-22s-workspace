"""Desmonstration of dictionary capabilities."""

# Declearing the type of a dictionary

school: dict[str, int]

# Initialize to an empty dictionary
school = dict()

# Set a key-value pairing in the dictionary
school["UNC"] = 19400
school["Duke"] = 6717
school["NCSU"] = 26150

# Print a dictionary literal representation
print(school)

# Access a value by it's key -- lookup
print(f"UNC has {school['UNC']} students")

# Remove a key-value pair from a dictionary
# by its key
school.pop("Duke")

# Test for existence of a key
is_duke_present: bool = "Duke" in school
print(f"Duke is present: {is_duke_present}")

# Updade/Reassign a key-value pair
school['UNC'] = 20000
school['NCSU'] += 200
print(school)

# Demonstration of dictrionary literals

# Empty dictionary literal
school = {}
print(school)

school = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(school)

print(school["UNCC"])