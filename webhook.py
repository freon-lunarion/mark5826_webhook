from flask import Flask, request, abort
import json
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    response = {
        "fulfillmentText": "This is a text response",
        "fulfillmentMessages": [
        {
        "card": {
            "title": "card title",
            "subtitle": "card text",
            "imageUri": "https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png",
            "buttons": [
            {
                "text": "button text",
                "postback": "https://assistant.google.com/"
            }
            ]
        }
        }
    ]

    }

    if request.method == 'POST':
        print(request.json)
        return json.dumps(response), 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run(debug=True)