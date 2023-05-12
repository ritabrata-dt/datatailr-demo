from flask import Flask
import sys

application = Flask(__name__)
application.debug = True

@application.route('/', methods=['GET'])
def hello():
    return 'Hello World!'

def __app_main__( ):
    return application

if __name__ == '__main__':
    application.run('0.0.0.0', port=int(sys.argv[1]), debug=True)
