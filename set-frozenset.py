# Sets are mutable containers
sett = set({"a", "b"})
print(sett)

sett_lit = {1, 2, 3, 4, 5, 6}
print(sett_lit)
sett_lit.add(7) # Adding elements
sett_lit.remove(1) # Removing elements
print(sett_lit)

# Frozen sets are not mutable
frozen_set = frozenset({"Python", "JS", "C", "C#"})
print(frozen_set)
print("JS" in frozen_set)
for i in frozen_set: # Also Sets are iterable
  print(i)
