@client.command("b64encode")
def b64enc(s, command):
            import base64
            text = ""
            
            for i in command.args:
                text += i

            encoded = base64.b64encode(text.encode()).decode()
            template = f'''
```ansi
[2;31m[1;31mEncrypted text: [1;34m[1;34m{encoded}[0m[1;34m[0m[1;31m[0m[2;31m[0m[2;31m[0m
```'''
            s.edit_message(template, command.id, CHANNEL)