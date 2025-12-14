import time
import math
from constants import Constants

class Drivetrain:
    def __init__(self, velocity, tolerance, time_update, robot):
        self.base_velocity = velocity
        self.drive_velocity = self.base_velocity
        self.turn_velocity = self.base_velocity
        self.turn_tolerance = tolerance # in degrees
        self.time_update = time_update
        self.robot = robot

    def set_drive_velocity(self, value, type=0):
        if type == 0: # 0 signifies PERCENT
            self.drive_velocity = (value / 100) * self.base_velocity
        elif type == 1: # 1 signifies VOLTS
            self.drive_velocity = (value / 12) * self.base_velocity
        elif type == 2: # 2 signifies RPM
            self.drive_velocity = (value / 300) * self.base_velocity

    def set_turn_velocity(self, value, type=0):
        if type == 0: # 0 signifies PERCENT
            self.turn_velocity = (value / 100) * self.base_velocity
        elif type == 1: # 1 signifies VOLTS
            self.turn_velocity = (value / 12) * self.base_velocity
        elif type == 2: # 2 signifies RPM
            self.turn_velocity = (value / 300) * self.base_velocity

    def drive_for(self, direction, value, units, wait=True):
        init_distance_traveled = 0
        while abs(init_distance_traveled) < (value * 0.1):
            left_drive_velocity = self.drive_velocity * direction
            right_drive_velocity = self.drive_velocity * direction

            v = (left_drive_velocity + right_drive_velocity) / 2
            w = (right_drive_velocity - left_drive_velocity) / Constants.DISTANCE_BETWEEN_WHEELS  # rad/s

            dt = self.time_update

            theta = self.robot.rotation

            dx = v * math.cos(theta) * dt
            dy = v * math.sin(theta) * dt
            dtheta = w * dt

            self.robot.shift(dx, dy, dtheta)

            init_distance_traveled += (self.drive_velocity * self.time_update)

            time.sleep(self.time_update)
            
    def turn_to_heading(self, angle, units, wait=True):
        init_angle = math.degrees(self.robot.rotation)
        init_angle %= 360
        angle = 360 - angle
        angle %= 360
        angle_difference = angle - init_angle
        shortest_angle_difference = angle_difference
        if angle_difference > 180:
            shortest_angle_difference -= 360
        elif angle_difference < -180:
            shortest_angle_difference += 360
        while abs(shortest_angle_difference) > self.turn_tolerance:
            direction = 1 # COUNTERCLOCKWISE
            if shortest_angle_difference < 0: # CLOCKWISE
                direction = -1


            left_drive_velocity = -1 * direction * self.turn_velocity
            right_drive_velocity = direction * self.turn_velocity

            v = (left_drive_velocity + right_drive_velocity) / 2
            w = (right_drive_velocity - left_drive_velocity) / Constants.DISTANCE_BETWEEN_WHEELS  # rad/s

            dt = self.time_update

            theta = self.robot.rotation

            dx = v * math.cos(theta) * dt
            dy = v * math.sin(theta) * dt
            dtheta = w * dt

            self.robot.shift(dx, dy, dtheta)

            init_angle = math.degrees(self.robot.rotation)
            init_angle %= 360
            
            angle_difference = angle - init_angle
            shortest_angle_difference = angle_difference
            if angle_difference > 180:
                shortest_angle_difference -= 360
            elif angle_difference < -180:
                shortest_angle_difference += 360
            time.sleep(self.time_update)