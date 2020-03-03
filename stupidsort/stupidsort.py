from typing import List
from random import shuffle

def is_sorted(arr: List[any]) -> bool:
  if len(arr) < 2:
    return True

  for i in range(1, len(arr)):
    if arr[i] < arr[i - 1]:
      return False

  return True

def stupid_sort(arr: List[any]) -> None:
  while not is_sorted(arr):
    shuffle(arr)
