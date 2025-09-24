string = str(input())

print("Длина предложения ", len(string))
print("Предложение в нижнем регистре ", string.lower())
count = 0
for i in ['a','e', 'i','o','u']:
    count += string.count(i)
print("Колличество гласных", count)
print("Измененное предложение",string.replace("ugly", "beauty"))

if "The" in string.split()[0]:
    print("Предложение начинается на The")
else:
    print("Предложение не начинается на The")
if "end" in string.split()[-1]:
    print("Предложение заканчивается на end")
else:
    print("Предложение не заканчивается на end")
if string.startswith("The"):
    print("Предложение начинается на The")
else:
    print("Предложение не начинается на The")
if string.endswith("end"):
    print("Предложение заканчивается на end")
else:
    print("Предложение не заканчивается на end")