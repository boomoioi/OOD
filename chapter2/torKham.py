class TorKham:
    def __init__(self):
        self.words = []

    def restart(self):
        self.words = []
        return "game restarted"

    def play(self, word):
        
        if not self.words:
            self.words.append(word)
        else:
            if(self.words[-1][-2:].lower() == word[:2].lower()):
                self.words.append(word)
            else:
               return f"\'{word}\' -> game over" 
        return f"\'{word}\' -> [\'" + "\', \'".join(self.words) + "\']"


torkham = TorKham()
S = input("*** TorKham HanSaa ***\nEnter Input : ").split(',')
for play in S:
    mode = play.split()[0]
    if mode == 'P':
        print(torkham.play(play.split()[1]))
    elif mode == 'R':
        print(torkham.restart())
    elif mode == 'X':
        break
    else:
        print(f"\'{play}\' is Invalid Input !!!")
        break