
from flask import Flask
# from markupsafe import escape
appy=Flask(__name__)

@appy.route('/')
def Helloworld():
    return "<h1>Hello world</h1>"

@appy.route('/hi')
def hi_world():
    return "<h1>Hi ! world , this Sandip</h1>"

# @app.route('/user/<username>')
# def user(username):
#     return "Welcome used : %s"%escape(username)




if __name__=="__main__":
    appy.run(host="0.0.0.0",debug=True)

