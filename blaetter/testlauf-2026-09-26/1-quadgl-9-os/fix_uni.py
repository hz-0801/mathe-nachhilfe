# Ersetzt in Lösungsquelltexten Unicode-Zeichen, die der Textfont nicht führt, durch Mathematik (idempotent).
import sys
ERS = [("x₁,₂", "$x_{1,2}$"), ("x₁", "$x_1$"), ("x₂", "$x_2$"), ("≈", "$\\approx$"), ("≠", "$\\neq$"),
       ("π", "$\\pi$"), ("±", "$\\pm$"), ("→", "$\\rightarrow$"), ("√", "$\\surd$"), ("₁", "$_1$"), ("₂", "$_2$")]
for f in sys.argv[1:]:
    s = open(f, encoding="utf-8").read()
    for a, b in ERS:
        s = s.replace(a, b)
    open(f, "w", encoding="utf-8", newline="").write(s)
    print("ok", f)
