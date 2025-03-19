try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Button import Button

class Background:
    def __init__(self, imgurl, speed, bg_width, bg_height, height):
        self.img = simplegui.load_image(imgurl)
        self.speed = speed
        self.bg_width = bg_width
        self.bg_height = bg_height
        self.height = height
        self.background_scroll = 0
        self.start_button = Button(290,335,100,40)
        self.restart_button = Button(290,335,100,40)
        self.final_score = 0

    def set_final_score(self,score):
        self.final_score = score
    def update(self):
        self.background_scroll = (self.background_scroll + self.speed) % self.bg_width
    def draw(self, canvas, game_state):
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
            self.start_button.draw(canvas)
            canvas.draw_text("Start",(320, 360), 20,"Black")
            canvas.draw_text("Flappy Chicken",(200,250),50,"Black")
        elif game_state == "over":
            canvas.draw_image(self.img,
                    (self.bg_width/ 2, self.bg_height / 2),
                    (self.bg_width, self.bg_height),
                    (self.bg_width / 2, self.height / 2),
                    (self.bg_width, self.bg_height))
            self.restart_button.draw(canvas)
            canvas.draw_text("Restart",(310, 360), 20,"Black")
            canvas.draw_text("Game Over",(220,200),50,"Black")
            canvas.draw_text("Score",(250, 250), 25,"Black")
            canvas.draw_text("High Score",(250, 290), 25,"Black")
            score = str(self.final_score)
            canvas.draw_text(score,(380,250),25,"Black")
        
#the main idea in the class is that i will implement the background, 
#with the background i will implement the buttons on it and the text
#this keeps the background logic in one class and not merging it in 
#the interaction class