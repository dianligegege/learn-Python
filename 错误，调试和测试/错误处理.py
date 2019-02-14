# try
def fun1():
    try:
        print('try...')
        r = 10 / 0
        print('result:',r)
    except ZeroDivisionError as e:
        print('except:',e)
    finally:
        print('finally...')
    print('end')

fun1()


# print(2/0)

# 记录错误 loading
import logging
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END') 


# 抛出错误
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')
