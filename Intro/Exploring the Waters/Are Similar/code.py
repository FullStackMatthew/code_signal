from operator import is_not
from functools import partial

def areSimilar(a, b):
    s = [i if a[i] != b[i] else None for i in range(len(a))]
    s = list(filter(partial(is_not, None), s))
    print(s)
    return len(s) == 0 or len(s) == 2 and a[s[0]] == b[s[1]] and b[s[0]] == a[s[1]]