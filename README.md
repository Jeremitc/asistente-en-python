
# Siri o Alexa in Python

**Descripción:**  
Este proyecto es un asistente virtual básico desarrollado en Python, diseñado para ejecutar comandos en la PC, responder a preguntas generales y mantener conversaciones simples mediante un árbol de decisiones. Inspirado en asistentes como Siri y Alexa, proporciona una base funcional para la interacción con el sistema y para responder a preguntas comunes.

## Tecnologías Utilizadas

- **Python**: Lenguaje principal del proyecto.
- **Bibliotecas de IA y Procesamiento de Lenguaje Natural**:
  - `SpeechRecognition`: Para reconocer y transcribir la voz del usuario.
  - `Transformers` y `Torch`: Para cargar y ejecutar modelos de lenguaje.
  - `spaCy`: Para procesar texto y clasificar intenciones.
- **Control del Sistema**:
  - `os`, `subprocess`, y `pyautogui`: Para ejecutar comandos y controlar aplicaciones en la PC.
- **Soporte de Audio**:
  - `pyttsx3`: Para generar respuestas en voz y simular un asistente conversacional.

## Estructura del Proyecto

```plaintext
Siri o Alexa in Python/
├── main.py                   # Script principal de ejecución
├── modules/                  # Módulos para tareas específicas
│   ├── conversation.py       # Árbol de decisiones y generación de respuestas
│   ├── voice_recognition.py  # Módulo de reconocimiento de voz
│   ├── command_execution.py  # Ejecución de comandos en el sistema
│   └── nlp_processing.py     # Clasificación de intenciones
└── requirements.txt          # Dependencias del proyecto
```

## Funcionalidades

1. **Reconocimiento de Voz**  
   El módulo `voice_recognition.py` utiliza `SpeechRecognition` para captar la voz del usuario, transcribirla y enviarla a otros módulos para su procesamiento.

2. **Clasificación de Intenciones**  
   En `nlp_processing.py`, el asistente utiliza `spaCy` para identificar la intención del usuario: abrir una aplicación, responder preguntas o iniciar una conversación.

3. **Árbol de Decisiones para Conversación**  
   En `conversation.py`, el árbol de decisiones permite al asistente dar respuestas preprogramadas a preguntas comunes como “¿Cómo estás?” o “¿Qué puedes hacer?”.

4. **Ejecución de Comandos en el Sistema**  
   En `command_execution.py`, el asistente abre aplicaciones, navega a sitios web y controla aplicaciones del sistema según los comandos específicos.

5. **Respuesta por Voz**  
   Con `pyttsx3`, el asistente responde en voz alta para mejorar la experiencia conversacional del usuario.

## Dependencias

Listado de dependencias en `requirements.txt`:

```plaintext
SpeechRecognition
transformers
torch
spacy
pyttsx3
pyautogui
pyaudio
```

## Uso del Proyecto

1. **Configuración**
   - Instalar las dependencias:
     ```bash
     pip install -r requirements.txt
     ```

2. **Ejecución**
   - Para iniciar el asistente, ejecutar:
     ```bash
     python main.py
     ```

3. **Ejemplo de Comandos**
   - “Abre YouTube”
   - “Calculadora”
   - “Hola, ¿cómo estás?”

## Limitaciones del Proyecto

1. **Interacciones Limitadas**  
   Responde a un número limitado de preguntas y comandos específicos.

2. **Sin Autoaprendizaje**  
   No mejora ni aprende de las interacciones pasadas.

3. **Modelo Conversacional Simple**  
   Usa un árbol de decisiones y respuestas preprogramadas, limitando su flexibilidad y realismo en la conversación.

## Mejoras Futuras (Plan para el Nuevo Proyecto)

Para superar estas limitaciones, el siguiente proyecto incluirá:

- Un modelo de lenguaje avanzado y autoaprendizaje.
- Interfaz de supervisión para ajustar y mejorar las respuestas.
- Ampliación de comandos y acciones en el sistema.

---

Este README proporciona una guía completa sobre el propósito, uso y estructura del proyecto **"Siri o Alexa in Python"**, dejando una base sólida documentada para futuras mejoras y referencias.
