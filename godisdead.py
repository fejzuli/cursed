def satan_incarnate():
    sum = 0

    def function_with_state(summand):
        nonlocal sum
        sum += summand
        return sum

    return function_with_state

do_evil = satan_incarnate()

do_evil(600)
do_evil(60)
what_have_i_done = do_evil(6)

print(what_have_i_done)
# 666
