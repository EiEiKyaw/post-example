from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/convert", methods=["POST"]) 
def convert():
    myinput = request.form['myinput']
    output = "It works " + myinput
    if myinput:
        return jsonify({'output': output})
    return jsonify({'output': "An error occured"})
    
if __name__ == "__main__":
    app.run(debug=True)
