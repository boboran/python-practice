s = "2018 Amazon Jeff Bezos 1120"

s1 = s[5:]
print(s1)

s2 = ""
for c in s:
    if c.isdigit():
        s2 += c
print(s2)

s3 = ""
l, r = 0, 0
while l < len(s):
    # find left
    while l < len(s) and not s[l].isdigit():
        s3 += s[l]
        l += 1
    if l == len(s):
        break
    # find right
    r = l + 1
    while r < len(s) and s[r].isdigit():
        r += 1
    s3 += "["+s[l:r]+"]"
    l = r
print(s3)

s4 = ""
for c in s:
    if c != " ":
        s4 += c
print(s4)

counter = {}
for c in s:
    if c in counter:
        counter[c] += 1
    else:
        counter[c] = 1
print(counter["1"])
