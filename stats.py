def get_num_words(text):
	words = text.split(" ")
	#print(f"{len(words)} words found in the document")

	return len(words)

def get_num_letters(text):
	letters_cnt = {}
	for letter in text:
		l = letter.lower()
		if l not in letters_cnt:
			letters_cnt[l]=0
		letters_cnt[l] += 1
		
	return letters_cnt

def sort_on(dict):
	return dict["num"]

def letters_report(letters_cnt):
	arr = []
	for letter in letters_cnt:
		if letter.isalpha():
			arr.append({"char": letter, "num": letters_cnt[letter]})

	arr.sort(key=sort_on, reverse = True)
	return arr
