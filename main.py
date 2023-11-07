from basic_word import BasicWord
from players import Player
from utils import load_random_word

# Загрузка случайного слова
word_url = "https://jsonkeeper.com/b/G4YO"
random_word = load_random_word(word_url)



if random_word:
    # Приветствие игрока и начало игры
    player_name = input("Введите имя игрока: ")
    player = Player(player_name)
    print(f"Привет, {player}!")
    print(f"Составьте {random_word.count_subwords()} слов из слова {random_word}.")

    while True:
        user_input = input("Поехали, ваше слово (или 'стоп' для завершения): ").lower()

        if user_input == 'стоп':
            break

        if len(user_input) < 3:
            print("Слово слишком короткое. Попробуйте снова.")
            continue

        if not random_word.is_valid_subword(user_input):
            print("Неверно. Попробуйте снова.")
            continue

        if player.has_used_word(user_input):
            print("Слово уже использовано. Попробуйте другое.")
            continue

        player.add_used_word(user_input)
        print("Верно!")

    print(f"Игра завершена, вы угадали {player.get_used_words_count()} слов!")


