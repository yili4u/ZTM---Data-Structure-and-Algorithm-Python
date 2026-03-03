fishes = ["trout", "salmon", "tuna", "shark", "Nemo"]
fishes.extend(["Nemo"] * 100)

def findNemo(fishes: list) -> None:
   for fish in fishes:
      if fish == "Nemo":
         print("Found Nemo!")
print(fishes)
findNemo(fishes)