from flask import Flask, request, jsonify, make_response
import pdf
import base64
import uuid
import logging
import tempfile

app = Flask(__name__)
logging.basicConfig(filename=tempfile.gettempdir() + '/app.log', level=logging.ERROR)


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


@app.errorhandler(500)
def internal_server_error(error):
    logging.error('Server Error: %s', error)
    return 'Error 500', 500


@app.errorhandler(Exception)
def unhandled_exception(e):
    logging.error('Unhandled Exception: %s', e)
    return 'Error 500', 500

if __name__ == "__main__":
    app.run()
