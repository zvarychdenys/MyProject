def to_jaden_case(string):
    ans = []
    sp = string.split()
    for words in sp:
        ans.append(words.capitalize())

    answer = " ".join(ans)
    return answer


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
