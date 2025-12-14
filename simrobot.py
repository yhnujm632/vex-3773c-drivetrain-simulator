import math
import turtle
from constants import Constants

class SimRobot:
    def __init__(self, screen, width, height, starting_position=(0,0), starting_rotation=0):
        self.screen = screen
        self.player = turtle.Turtle()

        self.width = width
        self.height = height
        self.STARTING_POSITION = starting_position
        self.position = list(self.STARTING_POSITION)
        self.STARTING_ROTATION = starting_rotation
        self.rotation = self.STARTING_ROTATION

        self.player.penup()
        self.player.goto(self.position[0], self.position[1])
        self.player.pendown()
        self.player.shape("classic")
        self.player.hideturtle()
        self.player.color("#0f0")

        self.player.speed(0)
        self.screen.tracer(0)
        
    def set_drivetrain(self, drivetrain):
        self.drivetrain = drivetrain

    def get_drivetrain(self):
        return self.drivetrain

    def draw_rectangle(self, x_coord, y_coord, width, height, rotation_angle=0):
        center_x = x_coord
        center_y = y_coord

        self.player.penup()
        self.player.goto(center_x, center_y)

        self.player.setheading(rotation_angle)

        self.player.forward(height / 2)
        self.player.right(90)
        self.player.forward(width / 2)
        self.player.right(180)

        self.player.pendown()

        self.player.begin_fill()
        self.player.forward(width)
        self.player.right(90)
        self.player.forward(height)
        self.player.right(90)
        self.player.forward(width)
        self.player.right(90)
        self.player.forward(height)
        self.player.right(90)
        self.player.end_fill()

        self.player.penup()
        self.player.goto(center_x, center_y)
        self.player.pendown()

        self.player.setheading(0)

    def draw_robot(self, x, y, rotation_angle):
        self.player.clear()
        self.player.color("#0f0")
        self.player.penup()

        theta = math.radians(rotation_angle)

        self.player.goto((x + ((self.width / 2) * math.cos(theta) - (self.height / 2) * math.sin(theta)), y + ((self.width / 2) * math.sin(theta) + (self.height / 2) * math.cos(theta))))
        self.player.pendown()
        self.player.begin_fill()
        self.player.goto((x + (-1 * (self.width / 2) * math.cos(theta) - (self.height / 2) * math.sin(theta)), y + (-1 * (self.width / 2) * math.sin(theta) + (self.height / 2) * math.cos(theta))))
        self.player.goto((x + (-1 * (self.width / 2) * math.cos(theta) + (self.height / 2) * math.sin(theta)), y + (-1 * (self.width / 2) * math.sin(theta) - (self.height / 2) * math.cos(theta))))
        self.player.goto((x + ((self.width / 2) * math.cos(theta) + (self.height / 2) * math.sin(theta)), y + ((self.width / 2) * math.sin(theta) - (self.height / 2) * math.cos(theta))))
        self.player.goto((x + ((self.width / 2) * math.cos(theta) - (self.height / 2) * math.sin(theta)), y + ((self.width / 2) * math.sin(theta) + (self.height / 2) * math.cos(theta))))
        self.player.end_fill()
        self.player.penup()
        
        self.player.color("#000")
        
        self.player.goto((x + (-1 * (self.width / 2) * math.cos(theta) - (self.height / 2) * math.sin(theta)), y + (-1 * (self.width / 2) * math.sin(theta) + (self.height / 2) * math.cos(theta))))
        self.player.pendown()
        self.player.begin_fill()
        self.player.goto((x, y))
        self.player.goto((x + (-1 * (self.width / 2) * math.cos(theta) + (self.height / 2) * math.sin(theta)), y + (-1 * (self.width / 2) * math.sin(theta) - (self.height / 2) * math.cos(theta))))
        self.player.end_fill()
        self.player.penup()

        self.screen.update()

    def shift(self, change_x, change_y, change_theta):
        self.position[0] += change_x
        self.position[1] += change_y
        self.rotation += change_theta

        heading_degrees = math.degrees(self.rotation)

        self.draw_robot(self.position[0], self.position[1], heading_degrees)
        

    def move(self, magnitude, direction_angle=0):
        self.position[0] += magnitude * math.cos(math.radians(direction_angle))
        self.position[1] += magnitude * math.sin(math.radians(direction_angle))
        self.draw_robot(self.position[0], self.position[1], direction_angle)
