from random import randint

def stupid_search(target: any, arr: list) -> int:
  if len(arr) == 0:
    return None
  while True:
    idx = randint(0, len(arr) - 1)
    if target == arr[idx]:
      return idx
