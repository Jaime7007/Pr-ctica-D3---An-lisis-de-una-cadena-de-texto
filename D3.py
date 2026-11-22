"""}==========O=========={
 Cabecera
 INFORME_CADENA DE TEXTO
 Autores: Jaime 
 Fecha: 22/11/2026 
 }==========O=========={"""

def contar_caracteres(frase):
    """Devuelve el número total de caracteres."""
    return len(frase)

def contar_vocales(frase):
    """Cuenta las vocales aplicando el patrón contador[cite: 33, 34]."""
    vocales = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"
    contador = 0
    for c in frase:
        if c in vocales:
            contador += 1
    return contador

def contar_consonantes(frase):
    """Cuenta las consonantes mediante un bucle y un acumulador de conteo."""
    consonantes = "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
    contador = 0
    for c in frase:
        if c in consonantes:
            contador += 1
    return contador

def contar_digitos(frase):
    """Cuenta los dígitos numéricos con el método isdigit()."""
    contador = 0
    for c in frase:
        if c.isdigit():
            contador += 1
    return contador

def contar_espacios(frase):
    """Cuenta los espacios en blanco."""
    contador = 0
    for c in frase:
        if c.isspace():
            contador += 1
    return contador

def letra_mas_repetida(frase):
    """Devuelve únicamente la letra alfabética que más se repite (en minúscula)."""
    frase_min = frase.lower()
    abecedario = "abcdefghijklmnopqrstuvwxyzáéíóúüñ"
    
    max_repes = 0
    mejor_letra = "Ninguna"
    
    for c in abecedario:
        repes = 0
        for letra in frase_min:
            if letra == c:
                repes += 1
        
        if repes > max_repes:
            max_repes = repes
            mejor_letra = c
            
    return mejor_letra

def es_palindromo(frase):
    """Comprueba si es palíndromo limpiando espacios e invirtiendo la cadena con un bucle."""
    limpia = ""
    for c in frase.lower():
        if not c.isspace():
            limpia += c
            
    if not limpia:
        return True
        
    inversa = ""
    for c in limpia:
        inversa = c + inversa
        
    return limpia == inversa

def invertir_frase(frase):
    """Devuelve la frase escrita al revés, recorrida con un bucle."""
    invertida = ""
    for c in frase:
        invertida = c + invertida
    return invertida

def generar_informe():
    """Programa principal que solicita la frase y muestra el informe formateado."""
    frase = input("Introduce una frase para analizar: ")
    
    print("\n" + "="*30)
    print("   INFORME DE LA CADENA DE TEXTO")
    print("="*30)
    print(f"• Frase original      : '{frase}'")
    print(f"• Nº de caracteres    : {contar_caracteres(frase)}")
    print(f"• Nº de vocales       : {contar_vocales(frase)}")
    print(f"• Nº de consonantes   : {contar_consonantes(frase)}")
    print(f"• Nº de dígitos       : {contar_digitos(frase)}")
    print(f"• Nº de espacios      : {contar_espacios(frase)}")
    print(f"• Letra más repetida  : {letra_mas_repetida(frase)}")
    print(f"• ¿Es palíndromo?     : {'Sí' if es_palindromo(frase) else 'No'}")
    print(f"• Frase al revés      : '{invertir_frase(frase)}'")
    print("="*30)

if __name__ == "__main__":
    generar_informe()