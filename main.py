path_to_file = 'books/frankenstein.txt'

def main(path):
    with open(path) as f:
        file_contents = f.read()
        print(file_contents)
# main(path_to_file)

def count_words(path):
    with open(path) as f:
        file_contents=f.read()
        words_list = file_contents.split()
    return len(words_list)
# print(count_words(path_to_file))

def count_characters(path):
    with open(path) as f:
        file_contents = f.read()
        contents_lowered = file_contents.lower()
        char_dict = {}
        for character in contents_lowered:
            if character.isalpha():
                if character not in char_dict:
                    char_dict[character]=1
                else:
                    char_dict[character]+=1
    return char_dict

def print_characters_count(path):
    words_count=count_words(path)
    chars_count=count_characters(path)
    chars_list = [{'char':char,'count':count} for char,count in chars_count.items()]
    chars_list.sort(key=lambda item: item['char'])
    print(f'--- Begin report of {path_to_file} ---')
    print(f'{words_count} words found in the document')
    for char in chars_list:
        print(f"The '{char['char']}' character was found {char['count']} times")
    print('--- End report ---')
print_characters_count(path_to_file)