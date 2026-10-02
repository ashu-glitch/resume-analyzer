from src.parser import extract_text_from_pdf, clean_text

raw = extract_text_from_pdf("resume.pdf")
print(raw[:500])
print("-----")
print(clean_text(raw)[:500])