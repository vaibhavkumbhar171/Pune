from random import randint

lower_limit = 1
higher_limit = 10
step_size = 1

for i in range(lower_limit, higher_limit, step_size):
    # do something
    

    higher_limit = higher_limit + randint(0, 5)
    i += 5
    print(i)


#sprint(i)
