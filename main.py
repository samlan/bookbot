from stats import get_num_words,convert_dict_to_list,get_char_freq
import sys


def sort_on(item):
	return item["num"]

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		filepath = sys.argv[1] 
	#frank=get_book_text("./books/frankenstein.txt")
	frank_num = get_num_words(filepath)
	frank_char_dict = get_char_freq(filepath)
	list_of_dictionaries = convert_dict_to_list(frank_char_dict)
	lod = list_of_dictionaries.copy()
	lod.sort(key=lambda x: x["num"], reverse=True)	
	print("===========================BOOKBOT==================")
	print(f"Analyzing book found at {filepath}...")
	print("----------------- Word Count ---------------")
	print(f"Found {frank_num} total words")
	print("--------------- Character Count --------------")

	for item in lod:
		if item['char'].isalpha():
			print(f"{item['char']}: {item['num']}")
		else:
			continue
	print("============= END ===============")

main()
