def calculate_weight_on_planets(earth_weight):
    """Calcula o peso em outros planetas com base no peso na Terra.

    Args:
        earth_weight (float): O peso (massa) da pessoa em kg na Terra.

    Returns:
        dict: Um dicionário com os planetas e o peso correspondente em cada um.
    """
    gravity_ratios = {
        "Mercúrio": 0.38,
        "Vênus": 0.91,
        "Marte": 0.38,
        "Júpiter": 2.34,
        "Saturno": 1.06,
        "Urano": 0.92,
        "Netuno": 1.19,
        "Plutão": 0.06,  # Incluí Plutão para curiosidade
        "Sol": 27.01
    }

    weights = {planet: earth_weight * gravity for planet, gravity in gravity_ratios.items()}
    return weights

def convert_weight_to_unit(weight_kg, unit):
    """Converte o peso de kg para outra unidade."""
    conversion_rates = {
        "kg": 1,
        "lb": 2.20462,
        "oz": 35.274
    }
    return weight_kg * conversion_rates.get(unit, 1)