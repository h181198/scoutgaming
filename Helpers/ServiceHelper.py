def secure_text(text):
    if isinstance(text, str):
        return text.replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;")

    return text
