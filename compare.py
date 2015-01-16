import os.path 


def get_the_directory(the_string):
	directory = ''
	while not os.path.isdir(directory):
		directory = raw_input('Enter the {0} directory: '.format(the_string))
	return directory


def list_the_files(the_string):
	the_list = []
	directory = get_the_directory(the_string)
	for subdir, dirs, files in os.walk(directory):
		for afile in files:
			whole_directory = os.path.join(subdir, afile)
			important_part = whole_directory.replace(directory,'')
			important_part = important_part.lower()
			the_list.append(important_part)
	return the_list


original_list = list_the_files('original')
copy_list = list_the_files('copy')

print('\n\nNumber of items in each directory:')
print('=================================')
print('Original directory: {0}'.format(str(len(original_list))))
print('Copy directory: {0}\n\n'.format(str(len(copy_list))))

print('Items in the copy but not in the original:')
print('=========================================')
for item in copy_list:
	if item not in original_list:
		print(item)

print('\n\nItems in the original but not in the copy:')
print('=========================================')
for item in original_list:
	if item not in copy_list:
		print(item)