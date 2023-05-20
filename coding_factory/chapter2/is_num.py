strange_message = "32c4o23di42n3g "

decrypted_message = ""

for char in strange_message:
    if not char.isnumeric():
        decrypted_message += char

print(decrypted_message)
