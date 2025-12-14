import turtle
from simrobot import SimRobot
from constants import Constants
from drivetrain import Drivetrain
from fake_vex import *
from controller import Controller
import math
import time


class TurtleApp:
    def __init__(self, is_driver):
        self.screen = turtle.Screen()
        self.screen.setup(450, 450)
        self.screen.onkey(self.exit_game, "Escape")
        self.driver = is_driver
        try:
            if self.driver:
                self.controller_1 = Controller()
        except Exception as e:
            print("Controller not detected. By default, defaulting to autonomous.")
            self.driver = False
        self.brain = Brain()
        self.intake_motor = Motor()
        self.hood_motor = Motor()
        self.triangle_piston = Piston()
        self.slider_piston = Piston()
        self.robot = SimRobot(self.screen, Constants.WIDTH, Constants.HEIGHT, Constants.STARTING_POSITION, Constants.STARTING_ROTATION)
        self.drivetrain = Drivetrain(Constants.VELOCITY, 3, Constants.TIME_UPDATE, self.robot)
        self.robot.set_drivetrain(self.drivetrain)
        try:
            self.screen.bgpic('real_topdown_map.png')
        except Exception:
            print("Warning: real_topdown_map.png not found. Using a plain white background.")

    def autonomous_func(self):
        brain, intake_motor, hood_motor, triangle_piston, slider_piston, drivetrain = self.brain, self.intake_motor, self.hood_motor, self.triangle_piston, self.slider_piston, self.drivetrain

        drivetrain.set_turn_velocity(150, RPM) # TO TEST!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        debug = Debug(brain.screen, FontType.MONO20)
        drivetrain.set_drive_velocity(200, RPM)
        intake_motor.set_velocity(100, PERCENT)
        hood_motor.set_velocity(100, PERCENT)
        intake_motor.spin(FORWARD)
        drivetrain.drive_for(FORWARD, 800, MM, wait=True)
        wait(1, SECONDS)
        intake_motor.stop()
        drivetrain.turn_to_heading(-120, DEGREES, wait=True)
        drivetrain.drive_for(FORWARD, 825, MM)
        drivetrain.turn_to_heading(-180, DEGREES, wait=True)
        triangle_piston.set(True)
        drivetrain.drive_for(REVERSE, 350, MM)
        intake_motor.spin(FORWARD)
        hood_motor.spin(FORWARD)
        wait(2,SECONDS)
        intake_motor.stop()
        hood_motor.stop()
        drivetrain.drive_for(FORWARD, 400, MM)
        triangle_piston.set(False)
        slider_piston.set(True)
        intake_motor.spin(FORWARD)
        drivetrain.drive_for(FORWARD, 400, MM)
        wait(0.8,SECONDS)
        intake_motor.stop()
        drivetrain.drive_for(REVERSE, 400, MM)
        slider_piston.set(False)
        wait(0.3, SECONDS)
        triangle_piston.set(True)
        drivetrain.drive_for(REVERSE, 400, MM)
        intake_motor.spin(FORWARD)
        hood_motor.spin(FORWARD)

    def exit_game(self):
        self.screen.bye()

    def main_loop(self):
        if self.driver == True:
            left_drive_velocity = self.controller_1.axis3.position() + self.controller_1.axis1.position()
            right_drive_velocity = self.controller_1.axis3.position() - self.controller_1.axis1.position()

            scale = max(100, abs(left_drive_velocity), abs(right_drive_velocity))
            left_drive_velocity = (left_drive_velocity / scale) * Constants.VELOCITY
            right_drive_velocity = (right_drive_velocity / scale) * Constants.VELOCITY

            v = (left_drive_velocity + right_drive_velocity) / 2
            w = (right_drive_velocity - left_drive_velocity) / Constants.DISTANCE_BETWEEN_WHEELS  # rad/s

            dt = Constants.TIME_UPDATE

            theta = self.robot.rotation

            dx = v * math.cos(theta) * dt
            dy = v * math.sin(theta) * dt
            dtheta = w * dt

            self.robot.shift(dx, dy, dtheta)

            self.screen.ontimer(self.main_loop, 50)
        else:
            self.autonomous_func()

    def cycle(self):
        self.main_loop()
        turtle.done()




