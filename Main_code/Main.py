import time
from monitor import exibir_painel
from simulador import simular_dados
from alertas import verificar_alertas

def main():
    print("🚀 Iniciando sistema de monitoramento...")
    time.sleep(2)

    while True:
        dados = simular_dados()
        alertas = verificar_alertas(dados)
        exibir_painel(dados, alertas)
        time.sleep(3)

main()