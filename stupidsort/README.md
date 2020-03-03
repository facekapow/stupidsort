# StupidSort
The original stupid algorithm

This algorithm is probably the tamest of them all. It goes by many names: bogosort, permutation sort, stupid sort, slow sort, shotgun sort, monkey sort, and probably many more, those are just the ones I found on Wikipedia.

The way it works is pretty simple: it contually shuffles an array until it's sorted.

## Performance
Worst case: O(&infin;). No, really. O(&infin;). There's a possibility (albeit an incredibly small one) that it is never shuffled into order, because shuffling is assumed to be completely random.

Best case: O(n). It needs to at least iterate through the entire array (minus one element) to check if the elements are in order.
