#reading word count in a file
with open(r'C:\Users\Ahad\Documents\text_file.txt', 'r') as file:
    data = file.read().replace(".", "")
    w = data.split()
    no_words = len(w)

    print(f"total number words in the given file: {no_words}")