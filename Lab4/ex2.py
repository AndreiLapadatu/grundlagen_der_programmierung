def replace_word(filename, old_word, new_word):
    with open(filename, 'r') as file:
        data = file.read()
    replaced_data = data.replace(old_word, new_word)
    count = data.count(old_word)

    with open(filename, 'w') as file:
        file.write(replaced_data)

    print(f'Cuvantul "{old_word}" a fost inlocuit cu cuvantul "{new_word}" de {count} ori.')


def main():
    replace_word('meine_datei.txt', 'katze', 'Hund')


main()
