fishes = {"trout", "salmon", "tuna", "shark", "Nemo"}

def findNemo(fishes: set) -> None:
   for fish in fishes:
      if fish == "Nemo":
         print("Found Nemo!")
         return
   print("Cannot find Nemo!")

seasons = ["Spring", "Summer", "Autumn", "Winter"]
print(list(enumerate(seasons, -1)))