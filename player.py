from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(STARTING_POSITION)
        self.go_to_start()
        self.setheading(90)
        self.lvl = 0

    def move(self):
        """Docstring"""
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def finish(self) -> bool:
        """Docstring"""
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        """Docstring"""
        self.goto(STARTING_POSITION)

