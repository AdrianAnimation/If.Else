lista = [18.5, 24.9, 29.9]

w = int(input("Enter your weight: "))
h = float(input("Enter your height: "))

bmi = w/(h**2)

peso = 'Underweight Normal Overweight Obesse'

for i in lista:
    if i > bmi:
        lista.remove(i)
print(round(bmi),2)
print(peso.split()[len(lista)])






