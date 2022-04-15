import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

class Box:
    def __init__(self):
        self.x = 50
        self.y = 50
        
        self.dx = 1
        self.dy = 2
        
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, 50, 20, arcade.color.BLUE)
        
    def advance(self):
        if self.x > SCREEN_WIDTH:
            self.dx = -1
        elif self.x < 0:
            self.dx = 1
        
        if self.y > SCREEN_HEIGHT:
            self.dy = -2
        elif self.y < 0:
            self.dy = 2
            
        
            
        self.x += self.dx
        self.y += self.dy
        
class DemoApp(arcade.Window):
    '''
    This class defines the demo application.
    It produces a rectangle on the screen.
    '''
    
    def __init__(self, width, height):
        super().__init__(width, height)
        
        arcade.set_background_color(arcade.color.WHITE)
        
        self.box = Box()
        
    def on_draw(self):
        '''
        Called ever time we need to draw the window
        :return:
        '''
        arcade.start_render()
        
        self.box.draw()
        
    def update(self, delta_time: float):
        '''
        The purpose of this method is to move everthing forward.
        :param delta_time:
        '''
        self.box.advance()
    
window = DemoApp(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()