# 🚀 Sistema de Monitoramento de Missão Espacial

Projeto desenvolvido para a **Global Solution 2026/1** da FIAP — Turma 1CCPF  
Disciplina: **Soluções em Energias Renováveis e Sustentáveis**

---

## 👨‍💻 Desenvolvedor

| Nome | RM | Turma |
|---|---|---|
| Matheus | 567261 | 1CCPF |

---

## 📋 Descrição

Sistema inteligente de monitoramento de dados simulados de uma missão espacial experimental. A solução interpreta e exibe em tempo real informações sobre temperatura, energia, comunicação e status geral dos módulos operacionais, gerando alertas automáticos diante de condições críticas.

---

## ⚙️ Funcionalidades

- 🌡️ **Monitoramento de Temperatura** — interna e externa da nave
- ⚡ **Monitoramento de Energia** — bateria, geração de painéis solares e consumo
- 📡 **Monitoramento de Comunicação** — força do sinal e latência
- 🛸 **Status Geral** — calculado automaticamente com base nos dados dos módulos
- 🔔 **Alertas Automáticos** — geração de alertas em níveis ALERTA e CRÍTICO
- 🔄 **Atualização em tempo real** — leituras a cada 3 segundos

---

## 🗂️ Estrutura do Projeto

```
missao_espacial/
│
├── main.py          # Ponto de entrada — roda o sistema em loop
├── simulador.py     # Gera os dados simulados dos módulos
├── alertas.py       # Analisa os dados e gera alertas automáticos
└── monitor.py       # Exibe o painel de controle no terminal
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- `random` — simulação de dados dos sensores
- `os` — limpeza do terminal para atualização do painel
- `time` — controle de intervalo entre leituras
- `colorama` — cores no terminal para melhor visualização

---

## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/Map-max/1ccpf-GS-SERS.git
cd 1ccpf-GS-SERS
```

### 2. Instale a dependência

```bash
python -m pip install colorama
```

### 3. Execute o sistema

```bash
python main.py
```

> Para encerrar o monitoramento, pressione `Ctrl + C`

---

## 📊 Faixas de Monitoramento

| Módulo | Normal | Alerta | Crítico |
|---|---|---|---|
| 🌡️ Temp. Interna | 0°C a 60°C | 0°C a -15°C ou 60°C a 75°C | Abaixo de -15°C ou acima de 75°C |
| ⚡ Bateria | Acima de 40% | 20% a 40% | Abaixo de 20% |
| 📡 Sinal | Acima de 50% | 30% a 50% | Abaixo de 30% |
| 📶 Latência | Abaixo de 2500ms | 2500ms a 4000ms | Acima de 4000ms |

---

## 🎥 Demonstração

[Link do vídeo no YouTube](#https://youtu.be/-XW0erARgRs)

---

## 📄 Licença

Projeto acadêmico — FIAP 2026
