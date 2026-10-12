# Programa 1: Cálculo de descuento con if-else anidados
def calcular_descuento(es_vip, monto_compra):
    descuento = 0.0
    
    # Estructura if-else anidada (Obligatoria para la práctica)
    if es_vip == True:
        if monto_compra >= 500:
            descuento = 0.20  # 20% de descuento
        else:
            descuento = 0.10  # 10% de descuento
    else:
        if monto_compra >= 300:
            descuento = 0.05  # 5% de descuento
        else:
            descuento = 0.00  # Sin descuento
            
    total_pagar = monto_compra - (monto_compra * descuento)
    return total_pagar

# Pruebas rápidas para verificar que funciona
print("Caso 1 (VIP, compra 600):", calcular_descuento(True, 600))
print("Caso 2 (VIP, compra 200):", calcular_descuento(True, 200))
print("Caso 3 (No VIP, compra 150):", calcular_descuento(False, 150))
