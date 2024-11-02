def test_function():        # 1
    def inner_function():   # 2
        print("Я в области видимости функции test_function")

    inner_function() #на терминале ничего не видим

inner_function()     #на терминале появляется ошибка