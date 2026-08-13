import random

attempts_by_level = {
    "1": 10,
    "2": 5,
    "3": 3,
}

print('Приветствую вас в игре "Угадай число"!')
print("Я загадываю число от 1 до 100.")
print("Количество попыток зависит от уровня сложности.")

playing = True

while playing:
    print("\nПожалуйста, выберите уровень сложности:")
    print("1. Легкий(10 попыток)")
    print("2. Средний(5 попыток)")
    print("3. Трудный(3 попытки)")

    while True:
        level = input("Введите уровень сложности: ")

        if level in attempts_by_level:
            break

        print("Доступны 3 уровня сложности.")

    attempts = attempts_by_level[level]

    print(f"Выбран уровень сложности: {level}")
    print(f"Количество попыток: {attempts}")

    random_digit = random.randint(1, 100)
    count = 0

    while attempts > 0:
        try:
            specified_digit = int(input("Введите число: "))
        except ValueError:
            print("Нужно ввести число.")
            continue

        count += 1

        if random_digit == specified_digit:
            print(f"Поздравляем! Вы угадали верное число за {count} попыток.")
            break
        elif random_digit > specified_digit:
            print(f"Неверно! Это число больше, чем {specified_digit}.")
        else:
            print(f"Неверно! Это число меньше, чем {specified_digit}.")

        attempts -= 1

    while True:
        play_again = input("\nХотите сыграть ещё раз? (да/нет): ").strip().lower()

        if play_again in ("да", "д", "yes", "y"):
            break
        elif play_again in ("нет", "н", "no", "n"):
            print("Спасибо за игру!")
            playing = False
            break

        print('Пожалуйста, введите "да" или "нет".')