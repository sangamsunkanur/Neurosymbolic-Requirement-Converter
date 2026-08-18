from flask import Flask, render_template, request
from converter import process_requirement, process_temporal_logic

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    conversion_mode = "forward"

    if request.method == "POST":

        conversion_mode = request.form.get("conversion_mode", "forward")
        text = request.form.get("requirement", "").strip()

        if text:

            if conversion_mode == "forward":
                result = process_requirement(text)

            elif conversion_mode == "reverse":
                result = process_temporal_logic(text)

    return render_template(
        "index.html",
        result=result,
        conversion_mode=conversion_mode
    )


if __name__ == "__main__":
    app.run(debug=True)