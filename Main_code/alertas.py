def verificar_alertas(dados):
    alertas = []

    # ⚡ Energia
    if dados["bateria"] < 20:
        alertas.append("🔴 CRÍTICO: Bateria abaixo de 20%!")
    elif dados["bateria"] < 40:
        alertas.append("🟡 ALERTA: Bateria abaixo de 40%.")

    # 📡 Comunicação
    if dados["sinal"] < 30:
        alertas.append("🔴 CRÍTICO: Sinal de comunicação muito fraco!")
    elif dados["sinal"] < 50:
        alertas.append("🟡 ALERTA: Sinal de comunicação fraco.")

    # 🌡️ Temperatura interna
    if dados["temp_interna"] > 75 or dados["temp_interna"] < -15:
        alertas.append("🔴 CRÍTICO: Temperatura interna fora dos limites!")
    elif dados["temp_interna"] > 60 or dados["temp_interna"] < 0:
        alertas.append("🟡 ALERTA: Temperatura interna em zona de atenção.")

    # ⚡ Balanço energético
    if dados["consumo"] > dados["paineis_solares"]:
        alertas.append("🟡 ALERTA: Consumo maior que geração dos painéis solares.")

    # 📶 Latência
    if dados["latencia"] > 4000:
        alertas.append("🔴 CRÍTICO: Latência de comunicação extremamente alta!")
    elif dados["latencia"] > 2500:
        alertas.append("🟡 ALERTA: Latência de comunicação elevada.")

    if not alertas:
        alertas.append("🟢 Todos os sistemas operando normalmente.")

    return alertas