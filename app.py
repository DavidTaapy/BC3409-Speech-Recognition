# Import Libraries
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import speech_recognition as sr

# Setup Flask App
app = Flask(__name__)

# Routes
@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["File"]
        filename = secure_filename(file.filename)
        print(filename + " processed!")
        file.save("static/" + filename)
        audio = sr.AudioFile("static/" + filename)
        with audio as source:
            audio = sr.Recognizer().record(audio)
        speech = sr.Recognizer().recognize_google(audio)
        return render_template("index.html", result = speech)
    else:
        return render_template("index.html", result = "Please upload speech file!")

# Run Application
if __name__ == "__main__":
    app.run()