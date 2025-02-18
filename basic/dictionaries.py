person = {
    "name": "rafa",
    "age": 15
}

print(person["name"])

person["height"] = "170cm"
del person["name"]

print(person)

print(person.get("name", "no name"))

for key, value in person.items():
    print(f"{key} - {value}")

for key in person:
    print(f"Key: {key}")

languages = {
    "rafa": "portguese",
    "mari": "portguese",
    "luca": "english"
}

for languages in set(languages.values()):
    print(languages)