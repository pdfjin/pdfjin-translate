from pdfjin_translate.core import translate_pdf_text


def test_import():
    assert callable(translate_pdf_text)
