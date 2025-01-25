text = "Python is a *multi-paradigm* *programming language*, meant to be highly *readable*."
inside = False

for c in text:
    if c == "*":
        inside = not inside
    else:
        if inside:
            c = c.upper()
        print(c, end="")
