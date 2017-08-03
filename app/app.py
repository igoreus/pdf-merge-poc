from flask import Flask, request, jsonify, make_response
import pdf
import base64
import uuid
import json

app = Flask(__name__)

@app.route("/health-check")
def health_check():
    return "OK"

@app.route("/pdf-merger", methods=['POST'])
def merge():
    res = pdf.merge(request.get_json(force=True))
    return res

@app.route("/pdf-merger-stream", methods=['POST'])
def merge_stream():
    data = request.get_json(force=True)
    response = make_response(base64.urlsafe_b64decode(pdf.merge(data)))
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = \
        'inline; filename=%s.pdf' % str(uuid.uuid4())
    return response

if __name__ == "__main__":
    app.run()