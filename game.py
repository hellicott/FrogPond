from frog_pond import FrogPond
from visualise import Visualise
from config import Config


class Game(object):

    def __init__(self, config):
        self.frog_pond = FrogPond(config)
        self.vis = Visualise(self.frog_pond)

    def play(self):
        self.print_frogs()
        self.print_lilly_pads()
        win = False
        round_num = 1
        while not self._all_frogs_out() and not win:
            print("*"*100)
            print(f"Round {round_num}")
            print("*" * 100)
            round_num += 1
            win = self.frog_round(self.frog_pond.frogs)
        if self._all_frogs_out():
            print("All frogs are out :(")

    def _all_frogs_out(self):
        for frog in self.frog_pond.frogs:
            if frog.playing:
                return False
        return True

    def frog_round(self, frog_list):
        for frog in frog_list:
            result = frog.jump(self.frog_pond.lilly_pads)
            if result == "win":
                print(f"Frog {frog.frog_id} reached the centre lilly pad!")
                return True
            if result == "out":
                print(f"Frog {frog.frog_id} is stuck!")
            else:
                x = frog.get_range_circle().centre_point.x
                y = frog.get_range_circle().centre_point.y
                print(f"Frog {frog.frog_id} made a jump, it's new position is ({x}, {y})")
        return False

    def print_frogs(self):
        for frog in self.frog_pond.frogs:
            x = frog.get_range_circle().centre_point.x
            y = frog.get_range_circle().centre_point.y
            print(f"Frog {frog.frog_id}: at position ({x}, {y}) with max jump {frog.max_jump}")

    def print_lilly_pads(self):
        for pad in self.frog_pond.lilly_pads:
            x = pad.circle.centre_point.x
            y = pad.circle.centre_point.y
            print(f"LillyPad at position ({x}, {y}) with radius {pad.circle.radius}. Centre_pad? {pad.centre_pad}")


def main():
    config = Config()
    game = Game(config)
    game.play()


main()
