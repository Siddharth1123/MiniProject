from flask import Flask, request, jsonify

app = Flask(_name_)


@app.route("/extract-urls", methods=["POST"])
def extract_urls():
    data = request.form.get("text")
    if data:
        urls = re.findall(r"\bhttps?:\/\/\S+", data)
        return jsonify({"urls": urls}), 200
    else:
        return jsonify({"error": "No text provided."}), 400


if _name_ == "_main_":
    app.run(debug=True)