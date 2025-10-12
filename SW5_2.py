

results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2,
            35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

sorted_results = sorted(results)

best_three = sorted_results[:3]

worst_three = sorted_results[-3:]

from_ten = [r for r in results if r >= 10]

print("Три лучших результата:", best_three)
print("Три худших результата:", worst_three)
print("Все результаты от 10 и выше:", from_ten)
