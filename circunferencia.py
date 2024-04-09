from pyscript import document
import math

def calcBtn(e):
    #leitura do valor do raio
    inputRaio = document.querySelector("#raio")
    raio = float(inputRaio.value or "0")

    #leitrua do valor do diâmetro
    inputDiametro = document.querySelector("#diametro")
    diametro = float(inputDiametro.value or "0")

    #leitura do valor do perímetro
    inputPerimetro = document.querySelector("#perimetro")
    perimetro = float(inputPerimetro.value or "0")

    #leitura do valor da área
    inputArea = document.querySelector("#area")
    area = float(inputArea.value or "0")

    if raio > 0 or diametro > 0 or perimetro > 0 or area > 0:
        #obter o raio a partir dos outros inputs
        if diametro != 0:
            raio = diametro / 2
        elif perimetro != 0:
            raio = perimetro / (2 * math.pi)
        elif area != 0:
            raio = math.sqrt(area / math.pi)

        #gerar o cálculo dos demais em função do raio
        diametro = 2 * raio
        area = math.pi * raio ** 2
        perimetro = 2 * math.pi * raio

        #injetar texto no input
        inputRaio.value = round(raio,2)
        inputDiametro.value = round(diametro,2)
        inputPerimetro.value = round(perimetro,2)
        inputArea.value = round(area,2)

    else:
       mensagemErro = document.querySelector("#logErro")
       mensagemErro.innerText = "Insira um valor maior que 0."

def limpBtn(e):
    document.querySelector("#raio").value = ""
    document.querySelector("#diametro").value = ""
    document.querySelector("#perimetro").value = ""
    document.querySelector("#area").value = ""
    document.querySelector("#logErro").innerText = ""