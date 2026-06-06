import random

def simular_dados():
    # 🌡️ Temperatura
    temp_interna = round(random.uniform(-20, 80), 1)
    temp_externa = round(random.uniform(-270, -180), 1)

    # ⚡ Energia
    bateria = random.randint(0, 100)
    paineis_solares = round(random.uniform(0, 5.0), 2)
    consumo = round(random.uniform(0.5, 3.0), 2)

    # 📡 Comunicação
    sinal = random.randint(0, 100)
    latencia = random.randint(100, 5000)

    # 🛸 Status geral (calculado automaticamente)
    if bateria < 20 or sinal < 30 or temp_interna > 75 or temp_interna < -15:
        status_geral = "CRÍTICO"
    elif bateria < 40 or sinal < 50 or temp_interna > 60 or temp_interna < 0:
        status_geral = "ALERTA"
    else:
        status_geral = "NORMAL"

    return {
        "temp_interna": temp_interna,
        "temp_externa": temp_externa,
        "bateria": bateria,
        "paineis_solares": paineis_solares,
        "consumo": consumo,
        "sinal": sinal,
        "latencia": latencia,
        "status_geral": status_geral
    }