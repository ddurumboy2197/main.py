texts = ["PYTHON", "MAP FUNCTION", "HELLO WORLD", "LAMBDA", "EXAMPLES"]
lower = list(map(str.lower, texts))
print(lower)

ages = [15, 18, 22, 16, 30]
status = list(map(lambda a: "Voyaga yetgan" if a >= 18 else "Voyaga yetmagan", ages))
print(status)
