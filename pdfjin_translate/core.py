import io
from pathlib import Path
from typing import Union
from deep_translator import GoogleTranslator
import pdfplumber


def translate_pdf_text(input_pdf: Union[str, Path, bytes], target_lang: str = "es") -> str:
    stream = open(input_pdf, "rb") if isinstance(input_pdf, (str, Path)) else io.BytesIO(input_pdf)
    translator = GoogleTranslator(source="auto", target=target_lang)
    extracted = []

    with pdfplumber.open(stream) as pdf:
        for p in pdf.pages:
            t = p.extract_text()
            if t:
                extracted.append(translator.translate(t))
    return "\n\n".join(extracted)
