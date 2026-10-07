def clasificar_imc(peso, altura):
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        categoria = "Bajo peso"
    elif imc < 25:
        categoria = "Normal"
    else:
        categoria = "Sobrepeso"
        
    return categoria