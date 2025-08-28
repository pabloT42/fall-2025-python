from pyfiglet import figlet_format
print("what font do you want to use")
font_int = input(" ")
print("what do you want to say")
word = input(" ")

print(figlet_format(word , font=font_int, width=100, justify="right"))
