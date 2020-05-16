import textwrap

def wrap(string, max_width):
    object = textwrap.TextWrapper(width=max_width, break_long_words=True)
    result = '\n'.join(object.wrap(string))
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)