from flask import *
from datetime import datetime
from multiprocessing import Process, Value
import functionality

app = Flask(__name__)

@app.route('/')
def main_app():
    return render_template('main.html')

@app.route('/success', methods=['GET', 'POST'])
def messages():
    messages = request.form.getlist("dropdown")

    if (request.form.get("contact") == "email"):
        functionality.add_mailing_list(request.form.get("contact"), "none", request.form.get("input"), messages)
    
    elif (request.form.get("contact") == "phone"):
        functionality.add_mailing_list(request.form.get("contact"), request.form.get("input_carrier"), request.form.get("input"), messages)

    return render_template('data.html')

@app.route('/report', methods=['GET', 'POST'])
def request_quotes():
    return render_template('request_quotes.html')

def record_loop(loop_on):
    while True:
        time = datetime.now()
        if (time.hour == 6 and time.minute == 30):
            functionality.send_message()

if __name__ == "__main__":
    recording_on = Value('b', True)
    p = Process(target=record_loop, args=(recording_on,))
    p.start()
    app.run(host='127.0.0.1', debug=True, use_reloader=False)
    p.join()