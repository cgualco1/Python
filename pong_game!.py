"""
File: pong.py
Original Author: Br. Burton
Designed to be completed by others
This program implements a simplistic version of the
classic Pong arcade game.
"""
import arcade
import random
import sys

# These are Global constants to use throughout the game
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BALL_RADIUS = 10

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 80
MOVE_AMOUNT = 7

SCORE_HIT = 1
SCORE_MISS = 5

class Point:
    def __init__(self):
        self.x = random.uniform(0,10)
        self.y = random.uniform(0,800)

class Velocity:
    def __init__(self):
        self.dx = 4.00
        self.dy = 4.00
        
class Ball():
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, BALL_RADIUS, arcade.color.WHITE)
        
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
    
    def bounce_horizontal(self):
        self.velocity.dx *= -1
        
    def bounce_vertical(self):
        if self.center.y > SCREEN_HEIGHT:
            self.velocity.dy *= -1
        elif self.center.y < 0:
            self.velocity.dy *= -1
    
    def restart(self):
        self.center = Point()
        self.velocity = Velocity()
    #Finished playing function    
    def finish(self):
        sys.exit()
    
class Paddle:
    def __init__(self):
        self.center = Point()
        self.center.x = SCREEN_WIDTH -40
        self.center.y = 400
        
    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.WHITE)
    #when paddle reaches the top or bottom it loops to the bottom or top
    def move_up(self):
        self.center.y += MOVE_AMOUNT
        if (self.center.y > SCREEN_HEIGHT):
            self.center.y = 0
    
    def move_down(self):
        self.center.y -= MOVE_AMOUNT
        if (self.center.y < 0):
            self.center.y = SCREEN_HEIGHT
        
class Pong(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Point
        Velocity
        Ball
        Paddle
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class,
    but should not have to if you don't want to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.ball = Ball()
        self.paddle = Paddle()
        self.score = 0
        self.end = ""
        
        # These are used to see if the user is
        # holding down the arrow keys
        self.holding_left = False
        self.holding_right = False

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsiblity of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.ball.draw()
        self.paddle.draw()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        end_text = "To End Press 'X'".format(self.end)
        start_x = 10
        start_y = SCREEN_HEIGHT - 60
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=40, color=arcade.color.WHITE)
        arcade.draw_text(end_text, start_x=start_x, start_y=start_y - 30, font_size=20, color=arcade.color.WHITE)
    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """

        # Move the ball forward one element in time
        self.ball.advance()

        # Check to see if keys are being held, and then
        # take appropriate action
        self.check_keys()

        # check for ball at important places
        self.check_miss()
        self.check_hit()
        self.check_bounce()

    def check_hit(self):
        """
        Checks to see if the ball has hit the paddle
        and if so, calls its bounce method.
        :return:
        """
        too_close_x = (PADDLE_WIDTH / 2) + BALL_RADIUS
        too_close_y = (PADDLE_HEIGHT / 2) + BALL_RADIUS

        if (abs(self.ball.center.x - self.paddle.center.x) < too_close_x and
                    abs(self.ball.center.y - self.paddle.center.y) < too_close_y and
                    self.ball.velocity.dx > 0):
            # we are too close and moving right, this is a hit!
            self.ball.bounce_horizontal()
            self.ball.velocity.dx *= 1.2
            self.ball.velocity.dy *= 1.2
            self.score += SCORE_HIT

    def check_miss(self):
        """
        Checks to see if the ball went past the paddle
        and if so, restarts it.
        """
        if self.ball.center.x > SCREEN_WIDTH:
            # We missed!
            self.score -= SCORE_MISS
            self.ball.restart()

    def check_bounce(self):
        """
        Checks to see if the ball has hit the borders
        of the screen and if so, calls its bounce methods.
        """
        if self.ball.center.x < 0 and self.ball.velocity.dx < 0:
            self.ball.bounce_horizontal()

        if self.ball.center.y < 0 and self.ball.velocity.dy < 0:
            self.ball.bounce_vertical()

        if self.ball.center.y > SCREEN_HEIGHT and self.ball.velocity.dy > 0:
            self.ball.bounce_vertical()

    def check_keys(self):
        """
        Checks to see if the user is holding down an
        arrow key, and if so, takes appropriate action.
        """
        if self.holding_left:
            self.paddle.move_down()

        if self.holding_right:
            self.paddle.move_up()
            

    def on_key_press(self, key, key_modifiers):
        """
        Called when a key is pressed. Sets the state of
        holding an arrow key.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT or key == arcade.key.DOWN:
            self.holding_left = True

        if key == arcade.key.RIGHT or key == arcade.key.UP:
            self.holding_right = True
        #If key is 'X' game will quit    
        if key == arcade.key.X:
            self.ball.finish()

    def on_key_release(self, key, key_modifiers):
        """
        Called when a key is released. Sets the state of
        the arrow key as being not held anymore.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT or key == arcade.key.DOWN:
            self.holding_left = False

        if key == arcade.key.RIGHT or key == arcade.key.UP:
            self.holding_right = False

# Creates the game and starts it going
window = Pong(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
