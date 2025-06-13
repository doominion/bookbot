import sys;
from stats import get_num_words, get_num_letters, letters_report

def get_book_text(file_path):
	with open(file_path) as f:
		return f.read()
		file_contents = f.read()

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}...")
	file_contents = get_book_text(sys.argv[1])
	print("----------- Word Count ----------")
	print(f"{get_num_words(file_contents)} words found in the document")
	letters_count = get_num_letters(file_contents)
	cnt = letters_report(letters_count)
	print("--------- Character Count -------")
	for d in cnt:
		print(f"{d['char']}: {d['num']}")
	# print(letters_report(letters_count))

main()
