import os
#Python has a built-in hash() function, which returns a 64bit int
#hashlib provides a wide range of secured hashing functions and the hash
#value can be updated with new feedins 
import hashlib

def duplicate_files(root):
	appeared_files= {}
	duplicates = []

	# do a depth-first traversal to visit all the files
	stack = [root]
	while stack:
		current_path = stack.pop()

		# os.path.isdir(), os.path.getmtime(), os.path.getsize(), os.path.join(parent, child)
		# os.listdir()
		if os.path.isdir(current_path):
			for path in os.listdir(current_path):
				full_path = os.path.join(current_path, path)
				stack.append(full_path)

		else:
			hash_value = hash_file(current_path)
			last_edit_time = os.path.getmtime(current_path)

			if hash_value in appeared_files:
				appeared_name, appeared_time = appeared_files[hash_value]
				if last_edit_time > appeared_time:
					duplicates.append((appeared_name, current_path))
				else:
					duplicates.append((current_path, appeared_name))

			else:
				appeared_files[hash_value] = (current_path, last_edit_time)

	return duplicates


def hash_file(full_name):

	hash_sample_size = 4000
	hasher = hashlib.sha256()

	file_size = os.path.getsize(full_name)

	with open(full_name, 'rb') as file:

		if file_size <= hash_sample_size * 3:
			hasher.update(file.read())

		else:
			read_offset = 0
			skip_block = (file_size - 3 * hash_sample_size) // 2
			for i in range(0, 3):
				file.seek(read_offset)
				hasher.update(file.read(hash_sample_size))
				read_offset += hash_sample_size + skip_block


	return hasher.hexdigest()


print duplicate_files("C:\Users\\alpha\Udacity\LeetCode\Leet\IC")


