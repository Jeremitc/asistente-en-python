import spacy

nlp = spacy.load("es_core_news_sm")  # Modelo en español

def interpretar_comando(comando):
    doc = nlp(comando)
    
    # Determinamos si el usuario necesita ayuda o conversación
    if any(palabra in comando.lower() for palabra in ["ayuda", "me podrías", "dime algo", "quisiera"]):
        return "conversacion_general", comando
    elif "abre" in comando and "youtube" in comando:
        return "abrir_youtube", None
    elif "abre" in comando and "calculadora" in comando:
        return "abrir_calculadora", None
    elif "abre" in comando and "navegador" in comando:
        return "abrir_navegador", None
    elif "busca" in comando:
        detalles = comando.split("busca")[-1].strip()
        return "realizar_busqueda", detalles
    elif "escribe" in comando:
        texto = comando.split("escribe")[-1].strip()
        return "escribir_texto", texto
    elif "apágate" in comando or "cerrar asistente" in comando:
        return "cerrar_asistente", None
    else:
        return "conversacion_general", comando
