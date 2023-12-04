def cnt(input):
    return {
        "digits": sum(char.isdigit() for char in input),
        "alphabets": sum(char.isalpha() for char in input),
        "spaces": sum(char.isspace() for char in input),
        "special_characters": sum(not char.isalnum() and not char.isspace() for char in input)
    }

input = "Hello 123, world!"
result = cnt(input)
print(result)
