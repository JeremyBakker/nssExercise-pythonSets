showroom = set()

showroom.add("Pilot")
showroom.add("Accord")
showroom.add("Civic")
showroom.add("Fit")
print(showroom)
print(len(showroom))
showroom.add("Pilot")
print(showroom)

new_showroom = set()
new_showroom.add("Highlander")
new_showroom.add("Camry")
print(new_showroom)

showroom.update(new_showroom)
print(showroom)
showroom.discard("Camry")
print(showroom)

junkyard = {"Ranger", "Bronco", "Highlander", "Civic", "Accord"}
print(showroom.intersection(junkyard))
combined_showroom = showroom.union(junkyard)
print(combined_showroom)

combined_showroom.discard("Bronco")
combined_showroom.discard("Ranger")
print(combined_showroom)