from modules.voice_recognition import escuchar_comando
from modules.nlp_processing import interpretar_comando
from modules.command_execution import ejecutar_orden
from modules.response_voice import responder

def ejecutar_asistente():
    while True:
        comando = escuchar_comando()
        if "salir" in comando:
            responder("Saliendo del asistente. ¡Hasta luego!")
            break
        interpretacion, detalles = interpretar_comando(comando)
        ejecutar_orden(interpretacion, detalles)
        responder("Comando ejecutado.")

if __name__ == "__main__":
    ejecutar_asistente()
