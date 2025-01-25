def len_common_prefix(a, b):
    len_ = min(len(a), len(b))
    for i in range(len_):
        if a[i] != b[i]:
            return i
    return len_

def main():
    txt1 = input("1st text? ")
    txt2 = input("2nd text? ")

    print(len_common_prefix(txt1, txt2))
    
main()