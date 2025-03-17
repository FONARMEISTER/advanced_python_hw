from fonarmeister_latex_helper import generate_latex_image, generate_latex_table, generate_pdf_from_latex, make_document_from_latex

data = [
    ["Test", "kek", 12313214],
    ["er242342342", 25, "kek"],
    ["fsdfdsf", 111, "sffk"]
]

latex_code = generate_latex_table(data)
latex_code += generate_latex_image("pic.png")
with open("artifacts/output_table.tex", "w") as file:
    file.write(latex_code)
latex_code = make_document_from_latex(latex_code)
generate_pdf_from_latex(latex_code, "artifacts/generated_document")