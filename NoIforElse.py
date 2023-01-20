lista = [18.5, 25, 30]

w = int(input("Enter your weight: "))
h = float(input("Enter your height: "))

bmi = w/(h**2)

peso = 'Underweight Normal Overweight Obesity'

for i in list(lista):
    if i > bmi:
        lista.remove(i)
print(round(bmi,2))
print(peso.split()[len(lista)])








