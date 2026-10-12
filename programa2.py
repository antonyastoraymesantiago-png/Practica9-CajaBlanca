# Programa 2: Cálculo de envío usando selección múltiple
def calcular_envio(zona):
    costo_envio = 0.0
    
    # Estructura de selección múltiple (Equivalente a switch-case)
    match zona:
        case "Norte":
            costo_envio = 15.0
        case "Sur":
            costo_envio = 20.0
        case "Centro":
            costo_envio = 10.0
        case _:
            costo_envio = 25.0  # Zona por defecto o remota
            
    return costo_envio

# Pruebas rápidas para verificar que funciona
print("Costo Zona Norte:", calcular_envio("Norte"))
print("Costo Zona Sur:", calcular_envio("Sur"))
print("Costo Zona Centro:", calcular_envio("Centro"))
print("Costo Zona Otras:", calcular_envio("Oeste"))
