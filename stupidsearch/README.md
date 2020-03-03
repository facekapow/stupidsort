# StupidSearch
Like StupidSort, but for searching.

This algorithm just picks random index until one of them matches the search parameter.

## Performance
Worst case: O(&infin;). This is especially the case if the item to search for is not present in the array. In that case, you're screwed.

Best case: O(1). It's possible that we just *happen* to land on the right element with our first guess.
