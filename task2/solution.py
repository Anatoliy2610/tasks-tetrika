import requests
from bs4 import BeautifulSoup
import csv


def get_animals_count():
    base_url = "https://ru.wikipedia.org"
    letter_url = f"{base_url}/wiki/Категория:Животные_по_алфавиту"
    counts = {}
    while letter_url:
        response = requests.get(letter_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        alphabet_groups = soup.select('.mw-category-group')
        for letter_group in alphabet_groups:
            letter = letter_group.find('h3').get_text(strip=True)
            animals = letter_group.select('ul li a')
            counts[letter] = counts.get(letter, 0) + len(animals)
        next_link = soup.find('a', text='Следующая страница')
        if next_link:
            letter_url = f"{base_url}{next_link['href']}"
        else:
            letter_url = None
    return counts


def write_to_csv(counts, filename='beasts.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Буква', 'Количество животных'])
        russian_alphabet = [
            'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И',
            'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т',
            'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я'
        ]
        for letter in russian_alphabet:
            writer.writerow([letter, counts.get(letter, 0)])


if __name__ == '__main__':
    animals_count = get_animals_count()
    write_to_csv(animals_count)
    print("Данные записаны в файл beasts.csv.")
