from flask import Flask, jsonify, request
app = Flask (__name__)
def calculate_gross_price(net_price:float, vat_rate: float = 0.27) -> float:
    if net_price < 0:
        raise ValueError ("A netto ar nem lehet negativ.")
    return round(net_price * (1+vat_rate), 2)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "DevOps Mini App - AFA kalkulator",
        "status": "running",
        "endpoints": ["/health", "/calculate?net=1000"]
    })

@app.route("/health",methods=["GET"])
def health():
    return jsonify({"status":"UP"}),200

@app.route("/calculate",methods=["GET"])
def calculate():
    try:
        net=float(request.args.get("net",0))
        gross = calculate_gross_price(net)
        return jsonify({
            "net_price":net,
            "vat_rate":"27%",
            "gross_price":gross
        }), 200
    except ValueError as e:
        return jsonify({"error": str(e)}),400

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)