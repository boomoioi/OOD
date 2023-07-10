vote_count = int(input("*** Election ***\nEnter a number of voter(s) : "))
votes = [int(vote) for vote in input("").split()]
counter = {}
res = []
for vote in votes:
    if vote<1 or vote>20:
        continue
    if vote in counter.keys():
        counter[vote] += 1
    else:
        counter[vote] = 1
        
if not counter: 
    print("*** No Candidate Wins ***")
most_vote = max([val for val in counter.values()])

res = [key for key, val in counter.items() if val == most_vote]
res.sort()
for can in res:
    print(can, end=" ")