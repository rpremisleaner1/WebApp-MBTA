"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request 

from mbta_helper import find_stop_near

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/nearest-station/', methods =["GET","POST"])
def get_nearest():
    if request.method == "POST":
        place_name = (request.form["place_name"])
        roots = find_stop_near(place_name)

        if roots: 
            return render_template('nearest_station_result.html',
            place_name = place_name,
            root1 = roots[0],
            root2 = roots[1] )

        else: 
            return render_template('nearest_station_form.html')
    return render_template('nearest_station_form.html')




if __name__ == '__main__':
    app.run(debug=True)
