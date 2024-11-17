cat = {}
info = {"status": "vaccinated", "breed": True}

cat ={
    "nick": "Simon",
    "age": 7,
    "characteristics": ["sweet", "biting"]
}

age = cat.get("age")
cat.update(info)

print("Updated cat dictionary:", cat)
