import sys
from modules.conversation import responder_conversacion

def ejecutar_orden(interpretacion, detalles=None):
    if interpretacion == "conversacion_general":
        respuesta = responder_conversacion(detalles)
        print("Asistente:", respuesta)
    elif interpretacion == "cerrar_asistente":
        print("Cerrando el asistente. ¡Hasta luego!")
        sys.exit()
    else:
        print("Comando no reconocido o en desarrollo")
