from flask import Flask, jsonify

app = Flask(__name__)
app.debug = False


@app.route('/ping')
def ping():
    return "Ping!"


@app.route('/set_active/<stream_name>')
def set_active(stream_name):
    open("active.txt", 'w').write(stream_name)
    return "Made " + stream_name + " active"


@app.route('/set_all_streams_inactive')
def set_all_streams_inactive():
    open("active.txt", 'w').write("")
    return "Stopped all streams"


@app.route('/is_active/<stream_name>')
def is_active(stream_name):
    return jsonify({
        'is_active': stream_name == open("active.txt", 'r').read()
    })


if __name__ == '__main__':
    app.run()