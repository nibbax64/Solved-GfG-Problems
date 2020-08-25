def reverse_words_in_a_given_string(string, size):
    arr = []
    front = 0
    for i in range(size):
        if string[i] == ".":
            arr.insert(0, string[front:i])
            front += 2
    return ".".join(arr)


if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        string = input()+"."
        print(":: ", reverse_words_in_a_given_string(string, len(string)))

'''
2
i.like.this.program.very.much
pqr.mno

'''
