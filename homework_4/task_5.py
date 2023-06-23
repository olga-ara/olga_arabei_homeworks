# программа проверки здоровья персонажа
import random
health = random.randrange(0, 100)
print(health)
if health <= 0:
    print('False')
else:
    print('True')

