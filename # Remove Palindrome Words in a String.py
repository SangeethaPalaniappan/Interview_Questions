# Remove palindrome words in a given string

string = "He did a great job"
string = "Malayalam is her mother tongue"
string = "Text contains malayalam and level words"
start = 0
end = 0
last = end
res = ""
while end < len(string):
    while end < len(string) and string[end] != " ":
        end += 1
    last = end + 1
    end -= 1
    while start <= end:
        s_string_ord = ord(string[start])
        e_string_ord = ord(string[end])
        if ord(string[start]) >= 65 and ord(string[start]) <= 90:
            s_string_ord = ord(string[start]) + 32
        elif ord(string[end]) >= 65 and ord(string[end]) <= 90:
            e_string_ord = ord(string[end]) + 32

        if s_string_ord != e_string_ord:
            if last > len(string):
                res += string[start : last - 1] 
                break
            res += string[start : last - 1] + " "
            break
        start += 1
        end -= 1
    start = last
    end = start + 1
    
print(res)        