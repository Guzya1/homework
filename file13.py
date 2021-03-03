
def is_even(num):
	if num%2 == 0:
		return True
	else:
		return False
def test_is_even():
	assert is_even(2) == True
	assert is_even(3) == False
	assert is_even(8) == True
	assert is_even(100) == True
	assert is_even(101) == False
	print("YOUR CODE IS CORRECT!")
test_is_even()

def square_number(num):
	return num**2
	
def test_square_number():
	assert square_number(2) == 4
	assert square_number(8) == 64
	assert square_number(10) == 100
	print("YOUR CODE IS CORRECT!")
test_square_number()

def is_odd(num):
	if num%2 == 0:
		return False
	else:
		return True
def test_is_odd():
	assert is_odd(2) == False
	assert is_odd(3) == True
	assert is_odd(8) == False
	assert is_odd(100) == False
	assert is_odd(101) == True
	print("YOUR CODE IS CORRECT!")
test_is_odd()

def last_letter(word):
	return word[-1]
def test_last_letter():
	assert last_letter('hello!') == '!'
	assert last_letter('banana') == 'a'
	assert last_letter('8') == '8'
	assert last_letter('funnyguys') == 's'
	assert last_letter('101') == '1'
	print("YOUR CODE IS CORRECT!")
test_last_letter()

def string_lenght(word):
	return len(word)
def test_string_lenght():
	assert string_lenght('hello!') == 6
	assert string_lenght('banana') == 6
	assert string_lenght('8') == 1
	assert string_lenght('funnyguys') == 9
	assert string_lenght('101') == 3
	print("YOUR CODE IS CORRECT!")
test_string_lenght()
