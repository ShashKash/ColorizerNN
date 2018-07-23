import os
from flask import render_template, request, send_from_directory
from FlaskAPI import app, db, original_target, colored_target
from FlaskAPI.models import Images
from FlaskAPI.colorize import colorize

@app.route("/")
def index():
    ##return render_template("upload.html")
    return "Hello"

@app.route("/upload",methods=['POST'])
def upload():
    print(request)
    file = request.files['photo']
    print(file)
    ori_name,extension = os.path.splitext(file.filename)
    #print(ori_name)
    #print(extension)

## Saving the b/w image in original_target##
    imageId = str(Images.query.count()+1)
    ori_storage_name = imageId+extension
    destination_bw = "/".join([original_target,ori_storage_name])
    print(destination_bw)
    col_storage_name = 'col_' + imageId + '.png'
    file.save(destination_bw)
    destination_col = "/".join([colored_target,col_storage_name])
    print(destination_col)

## Storing the info about image in database##
    image = Images(original_name=file.filename, stored_name=col_storage_name, original_image=destination_bw, colored_image=destination_col)
    db.session.add(image)
    db.session.commit()

## Using the DL model to colorize the image ##
## and save it in colored_target ##
    colorize(img_in=image.original_image,img_out=image.colored_image)

## Returning the required fetch info ##
## to user for the next step ##
    return imageId
    #return render_template("image_show.html", image_name=image.stored_name)

@app.route("/colored/<filename>")
def getColored(filename):
    return send_from_directory("colored_images", filename)

@app.route("/original/<filename>")
def getOriginal(filename):
    return send_from_directory("images", filename)
