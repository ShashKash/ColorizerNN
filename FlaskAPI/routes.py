import os
from flask import render_template, request, send_from_directory
from FlaskAPI import app, original_target, colored_target
from FlaskAPI.models import Images
from FlaskAPI.colorize import colorize

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload",methods=['POST'])
def upload():
    file = request.files['file']
    print(file)
    ori_name,extension = os.path.splitext(file.filename)
    print(ori_name)
    print(extension)
    ori_storage_name = str(int(len([i for i in os.listdir(original_target)]))+1)+extension
    print(ori_storage_name)
    destination_bw = "/".join([original_target,ori_storage_name])
    print(destination_bw)
    col_storage_name = 'col_' + ori_storage_name
    file.save(destination_bw)
    destination_col = "/".join([colored_target,col_storage_name])
    print(destination_col)

    colorize(img_in=destination_bw,img_out=destination_col)

    return render_template("image_show.html", image_name=col_storage_name)

@app.route("/colored/<filename>")
def getColored(filename):
    return send_from_directory("colored_images", filename)
