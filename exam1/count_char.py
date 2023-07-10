inp = input(" *** String count ***\nEnter message : ")
low = []
up = []
sum_up = 0
sum_low = 0 
for ch in inp: 
    if ch.islower():
        sum_low += 1
        if ch not in low:
            low.append(ch)
    elif ch.isupper():
        sum_up += 1
        if ch not in up:
            up.append(ch)
up.sort()
low.sort()

print(f"No. of Upper case characters : {sum_up}")
print("Unique Upper case characters : " + "  ".join(up))
print(f"No. of Lower case Characters : {sum_low}")
print("Unique Lower case characters : " + "  ".join(low))