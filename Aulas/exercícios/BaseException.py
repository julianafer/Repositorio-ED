a = 'Hello world!'

try:
    a + 10
except Exception:
    msg = "You can't add int to string"

print(msg)