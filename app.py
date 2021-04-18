from project import app
from flask import Flask, render_template
from project import route


# @app.route("/test")
# def test1():
# 	return render_template("test.html")

@app.route("/")
def index():
    return render_template("index.html")
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)

