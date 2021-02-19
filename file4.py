'''
a=input ("Имя:")
b=input ("Возраст:")
c=input ("Любимый фильм:")
print(f'Меня зовут, {a.title()}, мне {b.upper()} лет.\n Ваш фильм {c.title()} меня заинтересовал.')

a="Google создаст специальную команду для поиска багов в особо важных приложениях."
print(len(a.split()))

b="У вас есть строка 'Запуск Ethereum 2.0 состоится 1 декабря. На депозиный контракт внесено более 524 288 ЕТН"
d= b.split()
for y in d:
	print(y,type(y))

a="Хакеры слили в сеть данные пакистанской энергетической компании k-Electric"
print(a.title())

a=input ("Символ:")
print(f'Git{a.title()}Hub')

a="Самые важные события в мире инфосека за сентябрь"
print(a.replace("е","3"))
'''
s="Ботент IPStorm, в который ранее входили лишь Windows-машины" 
s1=len(s)
lower_case=s.lower()
upper_case=s.upper()
cut_len=s1-(s1 // 2)
printlen=lower_case[: cut_len] +upper_case[cut_len :]
print(printlen)

'''
d=e.split()
r=len(d)
for g in range(r // 2):
	print(d[g].lower(), end='')
s= r-r//2
while s < r:
	print(d[s].upper())
	s += 1
	print()
'''
a=str(True)
print(a, type(a))



