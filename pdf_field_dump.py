from pypdf import PdfReader

reader = PdfReader("/Users/walker/Downloads/PA_EO_WSC_Signed.pdf")
fields = reader.get_fields() or {}

for name, field in fields.items():
    print(f"{name}: {field.get('/FT')}")