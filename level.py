import constants


class Level:
    def __init__(self):
        self.value = 0
        self.hint_cnt = constants.HINTS_NR_LEVEL_0

    def change_to_next_level(self):
        self.value += 1
        if self.value == constants.MAX_LEVEL:
            self.value -= 1

        match self.value:
            case 0:
                self.hint_cnt = constants.HINTS_NR_LEVEL_0
            case 1:
                self.hint_cnt = constants.HINTS_NR_LEVEL_1
            case 2:
                self.hint_cnt = constants.HINTS_NR_LEVEL_2
