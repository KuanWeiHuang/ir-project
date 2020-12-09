class Music:
    def __init__(self, composer, composerlink, title, titlelink):
        self.composer = composer
        self.composerlink = composerlink
        self.title = title
        self.titlelink = titlelink

    def __str__(self):
        return " ; ".join([self.composer, self.composerlink, self.title, self.titlelink])