try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Background:
    def __init__(self, imgurl, speed, bg_width, bg_height, height,game_state):
        self.img = simplegui.load_image(imgurl)
        self.speed = speed
        self.bg_width = bg_width
        self.bg_height = bg_height
        self.height = height
        self.background_scroll = 0
    def update(self):
        self.background_scroll = (self.background_scroll + self.speed) % self.bg_width
    def draw(self, canvas):
        if game_state == "play": 
            global background_scroll
            canvas.draw_image(self.img,
                    (self.bg_width/ 2, self.bg_height / 2),
                    (self.bg_width, self.bg_height),
                    (self.bg_width / 2 - self.background_scroll, self.height / 2),
                    (self.bg_width, self.bg_height))

            # second copy to make it continuous
            canvas.draw_image(self.img,
                            (self.bg_width / 2, self.bg_height  / 2),
                            (self.bg_width, self.bg_height ),
                            (self.bg_width * 1.5 - self.background_scroll, self.height / 2),
                            (self.bg_width, self.bg_height ))
        elif game_state == "start":
            canvas.draw_image(self.img,
                    (self.bg_width/ 2, self.bg_height / 2),
                    (self.bg_width, self.bg_height),
                    (self.bg_width / 2, self.height / 2),
                    (self.bg_width, self.bg_height))
            canvas.draw_text("Flappy Chicken",(200,300),50,"Black")
        #here i will make the button for the start screen
        elif game_state == "over":
            canvas.draw_image(self.img,
                    (self.bg_width/ 2, self.bg_height / 2),
                    (self.bg_width, self.bg_height),
                    (self.bg_width / 2, self.height / 2),
                    (self.bg_width, self.bg_height))   
#the main idea in the class is that i will implement the background, 
#with the background i will implement the buttons on it and the text
#this keeps the background logic in one class and not merging it in 
#the interaction class

#i have one question, is it ok that the background stops for both the 
#start and over states but bc of the different text and buttons, i just
#repeated the code
