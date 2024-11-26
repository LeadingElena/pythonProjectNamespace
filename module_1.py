def test_function():
    print('Я не inner_function')
    def inner_function():
        print('Я в области видимости функции test_function')
        def inner_inner_function():
            print('А я inner_inner_function')
        return inner_inner_function
    return inner_function

def test_function_1():
    print('Я test_function_1')
    def inner_function_1():
        print('Я в области видимости функции test_function_1')
        def inner_inner_function_1():
            print('А я inner_inner_function_1')
        inner_inner_function_1()
    inner_function_1()

test_function()
print('')
test_function()()
print('')
test_function()()()
print('')
test_function_1()