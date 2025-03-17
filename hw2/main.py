from latex_helper import generate_latex_table, generate_latex_image


data = [
    ["Test", "kek", 12313214],
    ["er242342342", 25, "kek"],
    ["fsdfdsf", 111, "sffk"]
]

latex_code = generate_latex_table(data)
latex_code += generate_latex_image("pic.png")
with open("artifcats/output_table.tex", "w") as file:
    file.write(latex_code)