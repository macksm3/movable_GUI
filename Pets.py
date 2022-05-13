class Pets:

    def __init__(self, canvas, x, y, xVelocity, yVelocity, image):
        self.canvas = canvas
        # self.name = name
        self.image = canvas.create_image(x, y, image=image)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.image_width = image.width()
        self.image_height = image.height()

    def move(self):
        coordinates = self.canvas.coords(self.image)
        # print(coordinates)
        if (coordinates[0] >= (self.canvas.winfo_width()-self.image_width/2) or coordinates[0] < self.image_width/2):
            self.xVelocity = -self.xVelocity
        if (coordinates[1] >= (self.canvas.winfo_height()-self.image_height/2) or coordinates[1] < self.image_height/2):
            self.yVelocity = -self.yVelocity

        self.canvas.move(self.image, self.xVelocity, self.yVelocity)

    def stop(self):
        self.xVelocity = 0
        self.yVelocity = 0

