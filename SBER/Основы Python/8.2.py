text = 'a1 2b  3   abc d3e r2D2'
newText = ''
lenText = len(text)

for i in range(1, lenText + 1):
    s = text[i - 1]
    if (i - 1) == 0:
        s = s.upper()
    if text[i - 2] == ' ':
        if not s.isdigit():
            s = s.upper()
    newText += s
print(newText)
