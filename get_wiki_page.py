import wikipedia

page_title = "Line_(geometry)"

# auto_suggest=False because https://stackoverflow.com/a/69886635
page = wikipedia.page(title=page_title, auto_suggest=False)

print(page.content)
