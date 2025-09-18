from typing import IO
from bg import remove
import onnxruntime as ort
from flask import Flask, send_from_directory, request
import base64
from u2net import U2netSession
import os

app = Flask(__name__)


@app.route("/process", methods=["POST"])
def handle():
    # print('h')
    payload = request.get_json(force=True)
    # print(payload)
    base64_str: str = payload["img"]
    # print(base64_str)
    img_bytes = base64.b64decode(base64_str)
    out = start("u2net", img_bytes)
    f = open("out.jpg", "wb+")
    f.write(out)
    fin = open("in.jpg", "wb+")
    fin.write(img_bytes)
    return base64.b64encode(out).decode("utf-8")


def start(model: str, input: bytes) -> None:
    """
    Click command line interface function to process an input file based on the provided options.

    This function is the entry point for the CLI program. It reads an input file, applies image processing operations based on the provided options, and writes the output to a file.

    Parameters:
        model (str): The name of the model to use for image processing.
        extras (str): Additional options in JSON format.
        input: The input file to process.
        output: The output file to write the processed image to.
        **kwargs: Additional keyword arguments corresponding to the command line options.

    Returns:
        None
    """
    sess_opts = ort.SessionOptions()

    if "OMP_NUM_THREADS" in os.environ:
        threads = int(os.environ["OMP_NUM_THREADS"])
        sess_opts.inter_op_num_threads = threads
        sess_opts.intra_op_num_threads = threads

    return remove(input, session=U2netSession(model, sess_opts))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
