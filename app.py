from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def receber_mensagem():
    dados = request.json
    # print("Mensagem recebida:", dados)
    return {"status": "ok"}, 200

if __name__ == '__main__':
    app.run(port=5000)