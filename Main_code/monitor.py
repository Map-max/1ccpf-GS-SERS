import os
import time
from colorama import init, Fore, Style
from simulador import simular_dados
from alertas import verificar_alertas

init()

def exibir_painel(dados, alertas):
    os.system("cls")

    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "   🚀 PAINEL DE CONTROLE - MISSÃO ESPACIAL")
    print(Fore.CYAN + "=" * 50 + Style.RESET_ALL)

    # 🌡️ Temperatura
    print(Fore.CYAN + "\n🌡️  TEMPERATURA" + Style.RESET_ALL)
    print(f"   Interna : {dados['temp_interna']}°C")
    print(f"   Externa : {dados['temp_externa']}°C")

    # ⚡ Energia
    print(Fore.CYAN + "\n⚡  ENERGIA" + Style.RESET_ALL)
    print(f"   Bateria       : {dados['bateria']}%")
    print(f"   Painéis Solares: {dados['paineis_solares']} kW")
    print(f"   Consumo        : {dados['consumo']} kW")

    # 📡 Comunicação
    print(Fore.CYAN + "\n📡  COMUNICAÇÃO" + Style.RESET_ALL)
    print(f"   Sinal   : {dados['sinal']}%")
    print(f"   Latência: {dados['latencia']} ms")

    # 🛸 Status geral
    print(Fore.CYAN + "\n🛸  STATUS GERAL" + Style.RESET_ALL)
    if dados["status_geral"] == "CRÍTICO":
        print(Fore.RED + f"   {dados['status_geral']}" + Style.RESET_ALL)
    elif dados["status_geral"] == "ALERTA":
        print(Fore.YELLOW + f"   {dados['status_geral']}" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + f"   {dados['status_geral']}" + Style.RESET_ALL)

    # 🔔 Alertas
    print(Fore.CYAN + "\n🔔  ALERTAS" + Style.RESET_ALL)
    for alerta in alertas:
        print(f"   {alerta}")

    print(Fore.CYAN + "\n" + "=" * 50 + Style.RESET_ALL)
    print("   Próxima leitura em 3 segundos...")