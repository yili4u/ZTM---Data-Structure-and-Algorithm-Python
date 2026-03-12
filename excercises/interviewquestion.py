def containsCommonItemBrute(arr1, arr2):
  for item in arr1: #O(n)
    if item in arr2: #O(n)
      return True
  return False

def containsCommonItem(arr1, arr2):
  set2 = set(arr2)
  # or use dict: dict2 = {item:True for item in arr2}
  # or dict2 = dict.fromkeys(arr2)
  for item in arr1: #O(n)
    if item in set2: #O(1)
      return True
  return False


if __name__ == "__main__":
  array1 = ['a', 'b', 'c', 'x']
  array2 = ['z', 'y', 'i']
  #should return false
  print(containsCommonItem(array1, array2))

  array2 = ['z', 'y', 'x']
  #should return true
  print(containsCommonItem(array1, array2))
