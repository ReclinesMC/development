import turtle


class Ball:

    def __init__(self, color, size):
        self.ball = turtle.Turtle()
        self.screen = turtle.Screen()
        self.color = color
        self.size = size
        self.x = 0
        self.y = 0

        self.changeColor(color)
        self.ball.dot(self.size)
        self.ball.hideturtle()
        self.ball.penup()

    def __str__(self):
        out = self.color + " ball - radius of " + str(self.size)
        return out

    def changeColor(self, color):
        self.color = color
        self.ball.pencolor(self.color)
        self.ball.fillcolor(self.color)
        self.move(self.x, self.y)

    def changeSize(self, size):
        self.size = size

    def move(self, x, y):
        self.ball.clear()
        self.ball.goto(x, y)
        self.ball.dot(self.size)
        self.x = x
        self.y = y

    def bounce(self):
        ogy = self.y

        while self.y < 100:
            self.y += 1
            self.move(self.x, self.y)

        while self.y > ogy:
            self.y -= 1
            self.move(self.x, self.y)


ball1 = Ball("red", 30)
print(ball1)
ball1.bounce()
ball1.changeColor("green")
ball1.changeSize(50)
print(ball1)
ball1.bounce()
