class Robot:
    def __init__(self):
        self.direction = 0  # initial direction in degrees

    def turn_full_circle(self):
        """ completes a full turn. """
        self.direction = (self.direction + 360) % 360

    def get_direction(self):
        return self.direction

# Usage
robot = Robot()
print(robot.get_direction())  # Output: 0
robot.turn_full_circle()
print(robot.get_direction())  # Output: 0 (since a full turn brings it back to the same direction)
