def some_func(a, b, opt = []):
    retval = a + b + sum(opt)
    opt.append(retval)
    return retval

print(some_func(1,2))  # ok
print(some_func(1,2))  # huh
print(some_func(1,2))  # wtf python...