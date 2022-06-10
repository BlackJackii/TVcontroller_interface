class TVController:
    def __init__(self, channel):
        self.chan = channel
        self.N = 0  # позиция соответствует позиции во внутреннем списке

    def first_channel(self):
        self.N = 0
        return self.chan[self.N]

    def last_channel(self):
        self.N = len(self.chan) - 1
        return self.chan[self.N]

    def turn_channel(self, new):
        self.N = new - 1
        return self.chan[self.N]

    def next_channel(self):
        if self.N == len(self.chan) - 1:
            self.N = 0
        else:
            self.N += 1

        return self.chan[self.N]

    def previous_channel(self):
        if self.N == 0:
            self.N = len(self.chan) - 1
        else:
            self.N -= 1

        return self.chan[self.N]

    def current_channel(self):
        return self.chan[self.N]

    def is_exist(self, ex):
        if type(ex) == str:
            if ex in self.chan:
                return 'Yes'
            else:
                return 'No'
        elif type(ex) == int:
            if 0 < ex <= len(self.chan):
                return 'Yes'
            else:
                return 'No'
        else:
            raise ValueError('Не тот тип ввода!')

        return self.chan[self.N]


CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

assert controller.first_channel() == "BBC"
assert controller.last_channel() == "TV1000"
assert controller.turn_channel(1) == "BBC"
assert controller.next_channel() == "Discovery"
assert controller.previous_channel() == "BBC"
assert controller.current_channel() == "BBC"
assert controller.is_exist(4) == "No"
assert controller.is_exist("BBC") == "Yes"
