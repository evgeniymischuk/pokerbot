class ActionState:
    bank = None
    all_in = False
    folded = False
    combination_str = None
    total_point = 0

    def __init__(self):
        self.total_point = 0
        self.bank = 0
        self.all_in = False
        self.folded = False
        self.combination_str = None
