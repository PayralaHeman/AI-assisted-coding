# buggy_code_task2.py
def find_duplicates(nums):
	seen = set()
	duplicates = set()
	for num in nums:
		if num in seen:
			duplicates.add(num)
		else:
			seen.add(num)
	return list(duplicates)

# Get user input
user_input = input("Enter numbers separated by commas: ")
numbers = [int(x.strip()) for x in user_input.split(',') if x.strip()]
print(find_duplicates(numbers))
