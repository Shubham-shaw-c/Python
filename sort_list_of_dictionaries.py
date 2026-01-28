rows = [{"n": "A", "s": 70}, {"n": "B", "s": 95}, {"n": "C", "s": 82}]
print([r["n"] for r in sorted(rows, key=lambda r: r["s"], reverse=True)])
