from FlaskAPI import db

class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_name = db.Column(db.String(20), nullable=False)
    stored_name = db.Column(db.String(20), unique=True, nullable=False)
    original_image = db.Column(db.String(80), unique=True, nullable=False)
    colored_image = db.Column(db.String(80), unique=True, nullable=False)
    
    #For python3.6 string formatting is done using f-strings
    def __repr__(self):
        return f"Image('{self.original_name}','{self.stored_name}','{self.original_image}', '{self.colored_image}')"
    
    #For python<3.6 .format() is used
    #def __repr__(self):
     #   return "Image('{original_image}','{stored_name}','{original_image}','{colored_image}')".format(
      #      original_image=self.original_image,stored_name=self.stored_name,
       #     original_name=self.original_name,colored_image=self.colored_image)
