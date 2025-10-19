import logging

logging.basicConfig(
    level=logging.INFO,  # Solo los mensajes importantes, no de depuración
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

def dividir(a, b):
    try:
        resultado = a / b
        logging.info(f"Resultado de dividir: {a} / {b} = {resultado}")
        return resultado
    except ZeroDivisionError:
        logging.error(f"Error: División por cero. a={a}, b={b}")
        raise
    except Exception as e:
        logging.error(f"Error inesperado en dividir: {e}")
        raise

def promedio(lista_numeros):
    if not lista_numeros:
        logging.warning("Advertencia: Lista vacía recibida para calcular el promedio")
        return None
    try:
        resultado = sum(lista_numeros) / len(lista_numeros)
        logging.info(f"Promedio calculado: {resultado}")
        return resultado
    except Exception as e:
        logging.error(f"Error al calcular el promedio: {e}")
        raise

def obtener_elemento(lista, indice):
    if indice >= len(lista) or indice < -len(lista):
        logging.warning(f"Advertencia: Índice fuera de rango: {indice} para una lista de tamaño {len(lista)}")
        return None
    try:
        elemento = lista[indice]
        logging.info(f"Elemento obtenido en índice {indice}: {elemento}")
        return elemento
    except IndexError as e:
        logging.error(f"Error: Índice fuera de rango al intentar acceder a {indice}")
        raise
    except Exception as e:
        logging.error(f"Error inesperado en obtener_elemento: {e}")
        raise

def calcular_total(precios):
    try:
        total = sum(precios)
        logging.info(f"Total calculado: {total}")
        return total
    except TypeError:
        logging.error(f"Error: Lista de precios contiene tipos de datos no válidos")
        raise
    except Exception as e:
        logging.error(f"Error inesperado en calcular_total: {e}")
        raise

def main():
    logging.info("="*60)
    logging.info("Inicio del programa")
    logging.info("="*60)

    logging.info("Prueba 1: División")
    try:
        dividir(10, 2)
    except Exception:
        logging.error("Prueba 1 falló")

    logging.info("Prueba 2: Promedio de lista vacía")
    try:
        promedio([10,20,30])
    except Exception:
        logging.error("Prueba 2 falló")

    logging.info("Prueba 3: Obtener elemento con índice fuera de rango")
    try:
        obtener_elemento([1, 2, 3],2)
    except Exception:
        logging.error("Prueba 3 falló")

    logging.info("Prueba 4: Calcular total con tipos mezclados")
    try:
        calcular_total([10, 20, 30, 40])
    except Exception:
        logging.error("Prueba 4 falló")

    logging.info("="*60)
    logging.info("Fin del programa")
    logging.info("="*60)

if __name__ == "__main__":
    main()
