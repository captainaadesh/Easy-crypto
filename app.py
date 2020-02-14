from flask import Flask,render_template,request
from cipher import EasyCrypto as ec


app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/decrypt")
def decrypt():
	return render_template("decrypt.html")


@app.route("/encrypted_data", methods=["POST"])
def encrypted_data():
	pt = request.form.get("textarea")
	seed = request.form.get("seed")
	n = request.form.get("n")
	cipher = ec(seed+"."+n).encrypt(pt)
	return render_template("encrypted_data.html",cipher=cipher)

@app.route("/decrypted_data", methods=["POST"])
def decrypted_data():
	ct = request.form.get("textarea")
	seed = request.form.get("seed")
	n = request.form.get("n")
	plaintext = ec(seed+"."+n).decrypt(ct)
	return render_template("decrypted_data.html",plaintext=plaintext)


if __name__ == '__main__':
	app.run(debug=True)