import requests
from datetime import datetime

def get_quote(currency):
    currency = currency.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{currency}-BRL"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        key = f"{currency}BRL"
        if key not in data:
            print("❌ Moeda não encontrada ou inválida.")
            return

        quote = data[key]

        print(f"\n✅ Cotação {currency} para BRL:")
        print(f"Valor Atual: R$ {float(quote['bid']):.2f}")
        print(f"Valor Máximo do dia: R$ {float(quote['high']):.2f}")
        print(f"Valor Mínimo do dia: R$ {float(quote['low']):.2f}")
        date_time = datetime.fromtimestamp(int(quote['timestamp']))
        print(f"Última atualização: {date_time.strftime('%d/%m/%Y %H:%M:%S')}\n")
    
    except requests.RequestException as e:
        print("❌ Erro ao consultar a API:", e)

def main():
    currency = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").strip()
    
    if not currency.isalpha() or len(currency) != 3:
        print("❌ Código de moeda inválido.")
        return
    get_quote(currency)

if __name__ == "__main__":
    main()
