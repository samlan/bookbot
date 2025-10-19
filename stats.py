def get_book_text(filepath):
        with open(filepath) as f:
                file_contents = f.read()
        return file_contents
def get_num_words(filepath):
        with open(filepath) as f:
                file_contents=f.read()
        return len(file_contents.split())
def get_char_freq(filepath):
	char_nums = {}
	with open(filepath) as f:
		file_contents = f.read().lower()
	characters = list(file_contents)
	for character in characters:
		if character in char_nums:
			char_nums[character] += 1
		else:
			char_nums[character] = 1
	return char_nums

def get_word_freq(filepath):
	word_nums = {}
	with open(filepath) as f:
		file_contents=f.read().lower()
	words = file_contents.split()
	
	for word in words:
		if word in word_nums:
			word_nums[word] += 1
		else:
			word_nums[word]=1
	return word_nums



def convert_dict_to_list(mydict):
	mylist = []
	for key in mydict:
		mylist.append({"char": key, "num": mydict[key]})
	return mylist