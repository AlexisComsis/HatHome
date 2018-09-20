

    def updater(self):
        Entity.timer1 += 1
        if Entity.timer1 < 65:
            self.state = 0
        elif Entity.timer1 < 90:
            self.state = 1
        else:
            Entity.timer1 = 0
