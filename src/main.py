from calculations import calculate_weight_on_planets, convert_weight_to_unit

def main():
    print("Calculadora de peso em outros planetas!")
    try:
        earth_weight = float(input("Digite seu peso (massa) em kg na Terra: "))
        if earth_weight <= 0:
            print("Por favor, insira um peso positivo.")
            return

        unit = input("Escolha a unidade de saída (kg, lb, oz): ").strip().lower()
        if unit not in ["kg", "lb", "oz"]:
            print("Unidade inválida. Usando kg por padrão.")
            unit = "kg"

        weights = calculate_weight_on_planets(earth_weight)
        print(f"\nSeu peso nos outros planetas do sistema solar em {unit}:")
        for planet, weight in weights.items():
            converted_weight = convert_weight_to_unit(weight, unit)
            print(f"{planet}: {converted_weight:.2f} {unit}")

    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")

