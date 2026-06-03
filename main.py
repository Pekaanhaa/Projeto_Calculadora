# Importa as funções necessárias do Flask
from flask import Flask, render_template, request

# Cria a aplicação Flask
app = Flask(__name__)

# Define a rota principal "/"
# Aceita requisições GET (abrir a página)
# e POST (enviar o formulário)
@app.route("/", methods=["GET", "POST"])
def calculadora():

    # Variável que armazenará o resultado
    resultado = None

    # Verifica se o usuário enviou o formulário
    if request.method == "POST":

        # Obtém o valor digitado no primeiro campo
        valor1 = float(request.form["valor1"])

        # Obtém o valor digitado no segundo campo
        valor2 = float(request.form["valor2"])

        # Obtém a operação escolhida
        operacao = request.form["operacao"]

        # Se a operação for soma
        if operacao == "soma":
            resultado = valor1 + valor2

        # Se a operação for subtração
        elif operacao == "subtracao":
            resultado = valor1 - valor2

        # Se a operação for multiplicação
        elif operacao == "multiplicacao":
            resultado = valor1 * valor2

        # Se a operação for divisão
        elif operacao == "divisao":

            # Verifica se o divisor é diferente de zero
            if valor2 != 0:
                resultado = valor1 / valor2
            else:
                resultado = "Erro: divisão por zero."

    # Envia o resultado para a página HTML
    return render_template("calculadora.html", resultado=resultado)

# Executa o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)