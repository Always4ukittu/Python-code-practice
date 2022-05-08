# Flask helps toconvert our application into rest API

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

    
    # in browser like /34/23
@app.route("/LCM/<int:a>/<int:b>")
def LCM(a,b):
    if(a>b):
        num = b
    else:
        num = a
    # finding highest common factor which divide both the number
    for i in range(1, num+1):
        if(a%i==0 and 10%i==0):
            hcf = i

    return jsonify({
        "first_numbre":a,
        "second_numbre": b,
        "HCF" : hcf,
        "IP" : "127.0.0.1:5500"
    })

if __name__ == '__main__':
    app.run(debug=True)