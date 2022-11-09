import time
import concurrent.futures



def foo(name):
    print(name, " befor")
    time.sleep(1)
    print(name, "after")
    return "aila"



with concurrent.futures.ThreadPoolExecutor() as executor:
    print("Hello1")
    f1 = executor.submit(foo,"clemens")
    print(f1.result())
    print("Hello2")


