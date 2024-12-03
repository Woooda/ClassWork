text = 'Georgy '

reserv_text = ''

for i in range (len(text)):
    reserv_text += text[len(text) - i - 1]

print(reserv_text)