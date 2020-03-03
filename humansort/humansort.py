import re

yesRegex = re.compile('y|Y|yes|YES|Yes|TRUE|true|t|T')

def human_sort(arr: list) -> None:
  if len(arr) < 2:
    return

  result = [arr[0]]

  for i in range(1, len(arr)):
    found = False
    for j in range(0, len(result)):
      yOrN = str(input('is {} less than {}? (y/n): '.format(arr[i], result[j])))
      if yesRegex.match(yOrN) is not None:
        found = True
        result.insert(j, arr[i])
        break
    if not found:
      result += arr[i]

  for i in range(0, len(arr)):
    arr[i] = result[i]

