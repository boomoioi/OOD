class Queue():
    def __init__(self):
        self.items_size = 0
        self.items = []
    
    @property
    def size(self):
        return self.items_size

    def deQueue(self):
        if self.items:
            self.items_size -= 1
            return self.items.pop(0)
        return "Empty"
    
    def enQueue(self, val):
        self.items.append(val)
        self.items_size += 1
    
    def isEmpty(self):
        return not self.items

    def __str__(self):
        return ", ".join(self.items)
    
    def aclo(self):
        activitys = {
            "0" : "Eat",
            "1" : "Game",
            "2" : "Learn",
            "3" : "Movie"
        }
        location = {
            "0" : "Res.",
            "1" : "ClassR.",
            "2" : "SuperM.",
            "3" : "Home"
        }

        res = ""
        for al in self.items:
            al.split(":")
            res += activitys[al.split(":")[0]]+":"+location[al.split(":")[1]]+", "
        return res[:-2]


activitys = input("Enter Input : ").split(",")
q1 = Queue()
q2 = Queue()
score = 0
for activity in activitys:
    i = activity.split()[0]
    u = activity.split()[1]
    ia = i.split(":")[0]
    il = i.split(":")[1]
    ua = u.split(":")[0]
    ul = u.split(":")[1]
    if ia==ua and il==ul:
        score += 4
    elif ia==ua:
        score += 1
    elif il==ul:
        score += 2
    else:
        score -= 5
    q1.enQueue(i)
    q2.enQueue(u)

print(f"My   Queue = {q1}")
print(f"Your Queue = {q2}")
print(f"My   Activity:Location = {q1.aclo()}")
print(f"Your Activity:Location = {q2.aclo()}")
if score >= 7:
    print(f"Yes! You're my love! : Score is {score}.")
elif score > 0:
    print(f"Umm.. It's complicated relationship! : Score is {score}.")
else:
    print(f"No! We're just friends. : Score is {score}.")