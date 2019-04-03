names = ['Alex_', 'Mathew_', 'Har_ry']
cleaned_names = list(map(lambda x: x.replace('_', ''), names))
print(cleaned_names)

exp = lambda x, y: x**y
print(exp(2, 2))