def _prompt(prompt: str, type: str) -> str:
    prompt = prompt.strip()

    if type == "Personalizado":
        return prompt
    if type == "Código de programación":
        return (
            f"Escribe un código de programación funcional y bien comentado que cumpla con esta solicitud del usuario: {prompt}. "
            f"Asegúrate de usar buenas prácticas y claridad en el código. Responde solo con el código bien identado."
        )
    if type == "Traducción":
        return (
            f"Traduce el siguiente texto al idioma más probable según lo indicado (si se especifica un idioma, tradúcelo a ese): {prompt}. "
            f"Si no se especifica idioma, tradúcelo al español. Mantén el formato del contenido original."
        )
    return (
        f"Actúa como un experto creando contenido de tipo '{type}'. "
        f"Genera un {type.lower()} atractivo, claro y adaptado al público objetivo "
        f"basado en esta descripción del usuario: {prompt}. "
        f"El contenido debe estar en español."
    )
