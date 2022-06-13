a_var = range(2)


def locals_test():
    b_var = 3
    c_var = "hi"
    d_var = locals()
    print(d_var)


locals_test()

e_var = globals()
print(e_var)

numbers = (1, 2, 3, 4, 5)  # 패킹
numbers[3]  # 4

a, _, _, d, e = numbers
<!-- wp:codemirror-blocks/code-block {"mode":"python","mime":"text/x-python"} -->
<div class="wp-block-codemirror-blocks-code-block code-block"><pre>&gt;&gt;&gt; a, b, *rest = numbers     # 1, 2를 제외한 나머지를 rest에 대입
&gt;&gt;&gt; print(a, b, rest)
1 2 [3, 4, 5]


a, b, *rest = numbers

print(10,20,30)
print(*[10,20,30])  # *는 시퀀스를 언패킹하여 전달

a = [10,20,30]

print(a)

print(*a)  # *는 시퀀스를 언패킹하여 전달


def print_numbers(*args):
    for arg in args:
        print(arg)

print_numbers(10, 20, 30)

print_numbers(*a)