try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Button:
    def __init__(self,button_x,button_y,button_width,button_height,button_text):
        self.button_x = button_x
        self.button_y = button_y
        self.button_width = button_width
        self.button_height = button_height
        self.button_text = button_text
    def draw(self,canvas):
        canvas.draw_polygon([(self.button_x,self.button_y),
        (self.button_x + self.button_width, self.button_y), 
        (self.button_x + self.button_width, self.button_y + self.button_height),
        (self.button_x, self.button_y + self.button_height)], 2, "Black", "Yellow")
        canvas.draw_text(self.button_text,(self.button_x + 30, self.button_y + 25), 20,"Black")
    def is_clicked(self,pos):
        if self.button_x <= pos[0] <= self.button_x + self.button_width and self.button_y <= pos[1] <= self.button_y + self.button_height:
            return True
        return False