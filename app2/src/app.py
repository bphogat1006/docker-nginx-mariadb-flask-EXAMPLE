from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def index():
    headers = ''
    for k,v in request.headers.items():
        headers += f'<br>{k}: {v}'
    return Response('hi this is app2<br>'+headers)