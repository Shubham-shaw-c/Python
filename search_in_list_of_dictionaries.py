students = [{"id": 1, "name": "Ira"}, {"id": 2, "name": "Jay"}, {"id": 3, "name": "Kia"}]
match = next((s for s in students if s["id"] == 2), None)
print(match)
