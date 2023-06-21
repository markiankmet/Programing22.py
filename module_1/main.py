from Collection_libraries import *
file = input_file(input('Enter a file: '))
collection_ = Collection(file)
collection_.read_from_file()
print(collection_)