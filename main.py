def funkcija(sk1,sk2,sk3):
  maximums = sk1
  if sk1>sk2 and sk1>sk3:
    maximums = sk1
  elif sk2>sk1 and sk2>sk3:
    maximums = sk2
  else:
    maximums = sk3
  return maximums

sk1 = int(input("Ievadi 1.skaitli:"))
sk2 = int(input("Ievadi 2.skaitli"))
sk3 = int(input("Ievadi 3.skaitli:"))
print("Lielākais skaitlis =",funkcija(sk1,sk2,sk3))
