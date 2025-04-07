from collections import defaultdict

n = int(input())
students = []
languages = defaultdict(int)

for i in range(n):
    count = int(input())
    students.append(count)
    for j in range(count):
        lang = input()
        languages[lang] += 1

everybody_knows = []
for language in languages:
    if languages[language] == n:
        everybody_knows.append(language)

print(len(everybody_knows))
for lang in everybody_knows:
    print(lang)

print(len(languages))
for lang in languages.keys():
    print(lang)
