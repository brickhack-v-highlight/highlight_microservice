from flask import Flask, jsonify

app = Flask(__name__)
app.debug = False

ghetto_database = 'static/active.txt'
local = False


@app.route('/ping')
def ping():
    return "Ping!"


@app.route('/set_active/<stream_name>')
def set_active(stream_name):
    if local:
        open(ghetto_database, 'w').write(stream_name)

    return "Made " + stream_name + " active"


@app.route('/set_all_streams_inactive')
def set_all_streams_inactive():
    if local:
        open(ghetto_database, 'w').write("")
    return "Stopped all streams"


@app.route('/is_active/<stream_name>')
def is_active(stream_name):
    if local:
        active_stream = open(ghetto_database, 'r').read()
    return jsonify({
        'is_active': stream_name == active_stream
    })


if __name__ == '__main__':
    app.run()
