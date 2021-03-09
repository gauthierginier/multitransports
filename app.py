import os
from flask import Flask
from flask_cors import CORS
from back import route
from back.main import main
from apscheduler.schedulers.background import BackgroundScheduler
sched = BackgroundScheduler(daemon=True)
sched.add_job(main,'interval',seconds=59)
sched.start()

template_dir = os.path.abspath('./front/templates')
app = Flask(__name__, template_folder=template_dir)
CORS(app)
main()

app.static_url_path = "http://127.0.0.1:5000/static/"
app.static_folder = "./front/static"

app.add_url_rule('/', view_func=route.entry_point)
app.add_url_rule('/hello_world', view_func=route.hello_world)
app.add_url_rule('/<ville>/stations/<station>', view_func=route.nexttram)
app.add_url_rule('/<ville>/stations/', view_func=route.citystations)
app.add_url_rule('/<ville>/ligne/<ligne>', view_func=route.line_station)
app.add_url_rule('/<ville>/<station>/<ligne>/<direction>', view_func=route.next_to_direction)
app.add_url_rule('/<ville>/stationslike/<station>', view_func=route.station_like)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
