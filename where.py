where = input("Go left or right? ").strip().lower()

while where not in ("left", "right"):
    print("Please type left or right.")
    where = input("Go left or right? ").strip().lower()

print("You got this!")