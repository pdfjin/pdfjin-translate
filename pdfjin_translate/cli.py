import sys, argparse
try:
    from .core import translate_pdf_text
    from . import __version__
except (ImportError, ValueError):
    from pdfjin_translate.core import translate_pdf_text
    from pdfjin_translate import __version__


def main():
    p = argparse.ArgumentParser(prog="pdfjin-translate", description="Translate PDF text.")
    p.add_argument("input", help="Input PDF file")
    p.add_argument("-l", "--lang", default="es", help="Target language code (e.g. 'es', 'fr', 'de')")
    p.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    args = p.parse_args()
    try:
        res = translate_pdf_text(args.input, target_lang=args.lang)
        print(res)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr); sys.exit(1)


if __name__ == "__main__":
    main()
