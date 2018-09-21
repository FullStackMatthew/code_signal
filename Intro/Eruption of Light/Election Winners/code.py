def electionsWinners(votes, k):
    m = max(votes)
    n = 0
    if k == 0:
        return 1 if votes.count(m)  == 1 else 0;
    for v in votes:
        if(v + k > m):
            n += 1
    return n