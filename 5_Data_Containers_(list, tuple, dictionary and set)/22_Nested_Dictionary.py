# Nested Dictionary
books = {
    'U Maung': ['Python', 'C++', 'Java'],
    'Kyaw Aye': ['Bitcoin', 'C#']
}
print(books)
print(books['U Maung']) # ['Python', 'C++', 'Java']
print(books['Kyaw Aye']) # ['Bitcoin', 'C#']
print(books['U Maung'][0]) # Python
print(books['Kyaw Aye'][1]) # C#

# Dictionary Nested with Dictionary
books = {
    'MaungMaung': {
        # nested dictionary
                # nested list
        '2015': ['Python programming', 'C++ programming', 'Data Mining'],
        '2019': ['Web development', 'Java script']
    },
    'Thiha': {
        2020: 'Bitcoin Mining'
    }
}
print(books['MaungMaung']['2015'][1])
print(books['MaungMaung']['2019'][0])
print(books['Thiha'][2020])

# List Nested with Dictionary
book_shelf = [
    {
        # book shelf 0
        'book_amount': 10,
        'class': 'Maths',
        'keeper': True
    },
    {
        # book shelf 1
        'book_amount': 5,
        'class': 'English',
        'keeper': True
    },
    {
        # book shelf 2
        'book_amount': 3,
        'class': 'Geography',
        'keeper': False
    }
]
print(book_shelf[0])
print(book_shelf[0]['book_amount'])
print(book_shelf[1]['book_amount'])
print(book_shelf[2]['book_amount'])