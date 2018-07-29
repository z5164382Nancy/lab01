strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''


for i in strings[:-1]:
	sentence = sentence + i + ' '

sentence += strings[-1]

print(sentence)



print(' '.join(strings))
