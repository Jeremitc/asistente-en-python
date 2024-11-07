import webbrowser
import os

# Diccionario de respuestas y acciones por categorías
conversacion = {
    "saludo": ["¡Hola! ¿En qué puedo ayudarte hoy?", "¡Hola! ¿Qué necesitas?", "Hola, ¿cómo puedo asistirte en temas de informática hoy?"],
    
    # Soporte Técnico
    "soporte": [
        "¿Tienes problemas con tu computadora o algún software en particular? Puedo ayudarte a resolver problemas comunes.",
        "Para problemas de red, prueba a reiniciar tu router. ¿Necesitas ayuda con algo más específico?",
        "Si tienes problemas de rendimiento, verifica el Administrador de Tareas. ¿Quieres que te guíe en eso?"
    ],
    
    # Apertura de aplicaciones
    "abrir": {
        "youtube": lambda: webbrowser.open("https://www.youtube.com"),
        "calculadora": lambda: os.system("calc"),
        "navegador": lambda: webbrowser.open("https://www.google.com"),
        "editor de código": lambda: os.system("code"),  # Para Visual Studio Code
        "spotify": lambda: webbrowser.open("https://www.spotify.com")
    },
    
    # Interacciones para Gamers
    "gamers": [
        "¿Buscas recomendaciones de hardware para juegos?",
        "Para mejorar el rendimiento en juegos, asegúrate de cerrar aplicaciones en segundo plano y optimizar la configuración gráfica.",
        "¿Quieres saber los últimos lanzamientos de videojuegos? Puedo abrir páginas de noticias de juegos si lo necesitas."
    ],
    
    # Ingenieros de Software
    "ingenieria": [
        "¿Necesitas ayuda con algún lenguaje de programación en específico?",
        "Para desarrollo web, te recomiendo explorar React, Django, o Flask. ¿Te interesa alguno?",
        "¿Quieres abrir el entorno de desarrollo Visual Studio Code o necesitas documentación sobre algún tema?"
    ],
    
    # Agradecimiento y Despedida
    "agradecimiento": ["¡De nada! ¿Hay algo más en lo que pueda ayudarte?", "Estoy aquí para ayudarte, no dudes en preguntar."],
    "despedida": ["¡Hasta luego! Que tengas un buen día.", "Adiós, ¡espero haberte ayudado!"]
}

# Función que devuelve una respuesta o realiza una acción
def responder_conversacion(mensaje):
    mensaje = mensaje.lower()

    # Saludos
    if "hola" in mensaje:
        return conversacion["saludo"][0]
    
    # Soporte Técnico
    elif "problema" in mensaje or "ayuda" in mensaje or "soporte" in mensaje:
        return conversacion["soporte"][0]
    
    # Apertura de Aplicaciones
    elif "abre" in mensaje:
        if "youtube" in mensaje:
            conversacion["abrir"]["youtube"]()
            return "He abierto YouTube para ti."
        elif "calculadora" in mensaje:
            conversacion["abrir"]["calculadora"]()
            return "He abierto la calculadora."
        elif "navegador" in mensaje:
            conversacion["abrir"]["navegador"]()
            return "He abierto el navegador."
        elif "editor de código" in mensaje:
            conversacion["abrir"]["editor de código"]()
            return "He abierto el editor de código (VS Code)."
        elif "spotify" in mensaje:
            conversacion["abrir"]["spotify"]()
            return "He abierto Spotify en el navegador."
        else:
            return "Lo siento, no tengo configurada esa aplicación para abrirla."
    
    # Interacciones para Gamers
    elif "juego" in mensaje or "gamer" in mensaje:
        return conversacion["gamers"][0]
    
    # Ingenieros de Software
    elif "programación" in mensaje or "ingeniero" in mensaje or "software" in mensaje:
        return conversacion["ingenieria"][0]
    
    # Agradecimientos y Despedidas
    elif "gracias" in mensaje:
        return conversacion["agradecimiento"][0]
    elif "adiós" in mensaje or "hasta luego" in mensaje:
        return conversacion["despedida"][0]
    
    # Respuesta predeterminada
    return "No estoy seguro de cómo responder a eso, ¿puedes preguntar algo diferente?"
