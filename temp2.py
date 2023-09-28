n = int(input())
i = 0
lst = []

while i < n:
    m = input().split()

    lst.append(m)
    i += 1

board1 = []
board2 = []
f = lst[0]

for g in lst[1:]:
    if f[3] == g[3]:
        board1.append(g)
board1.append(f)

for g in lst:
    if g[3] != f[3]:
        board2.append(g)

a1 = []
s1 = []
c1 = []
a2 = []
s2 = []
c2 = []

for x in board1:
    if x[4] == "A":
        a1.append(x)
    elif x[4] == "S":
        s1.append(x)
    elif x[4] == "C":
        c1.append(x)
for x in board2:
    if x[4] == "A":
        a2.append(x)
    elif x[4] == "S":
        s2.append(x)
    elif x[4] == "C":
        c2.append(x)


def scenarios(a, s):
    h_a = int(a[1])
    h_s = int(s[1])
    m_a = int(a[2])
    m_s = int(s[2])
    if int(s[0]) > int(a[0]):
        d = int(s[0]) - int(a[0])
        if m_a != 0:
            m_s += 60
            h_s += 23 * d
            result = (60*(h_s - h_a)) + (m_s - m_a)
        else:
            h_s += 24 * d
            result = (60*(h_s - h_a)) + (m_s - m_a)
        return result
    else:
        if h_s != 0:
            m_s += 60
            h_s -= 1
            result = (60*(h_s - h_a)) + (m_s - m_a)
        else:
            result = m_s - m_a
        return result


def merge_two_list(a, b):

    c = []
    i = j = 0

    while i < len(a) and j < len(b):
        if int(a[i][0]) < int(b[j][0]):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]

    return c


def merge_sort(list):

    if len(list) == 1:
        return list

    mid = len(list) // 2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    return merge_two_list(left, right)


merge_sort(a1)
if len(s1) > 0:
    merge_sort(s1)
if len(c2) > 0:
    merge_sort(c1)
merge_sort(a2)
if len(s2) > 0:
    merge_sort(s2)
if len(c2) > 0:
    merge_sort(c2)

results = []
q = 0
if int(a1[0][3]) < int(a2[0][3]):
    if len(a1) > 1:
        sum = 0
        temp = []
        for j in a1:
            if len(s1) > 0:
                res1 = scenarios(j, s1[q])
                temp.append(res1)
                if len(c1) > 0:
                    res = scenarios(j, c1[q])
                    temp.append(res)
                q += 1
            else:
                res = scenarios(j, c1[q])
                temp.append(res)
                q += 1
        for l in temp:
            sum += l
        results.append(sum)
    else:
        res = scenarios(a1[0], s1[0])
        results.append(res)

    if len(a2) > 1:
        for j in a2:
            sum = 0
            temp = []
            if len(s1) > 0:
                res = scenarios(j, s2[q])
                temp.append(res)
                if len(c2) > 0:
                    res = scenarios(j, c2[q])
                    temp.append(res)
                q += 1
            else:
                res = scenarios(j, c2[q])
                temp.append(res)
                q += 1
        for l in temp:
            sum += l
            results.append(sum)
    else:
        res = scenarios(a2[0], s2[0])
        results.append(res)
else:
    if len(a2) > 1:
        for j in a2:
            sum = 0
            temp = []
            if len(s1) > 0:
                res = scenarios(j, s2[q])
                temp.append(res)
                if len(c2) > 0:
                    res = scenarios(j, c2[q])
                    temp.append(res)
                q += 1
            else:
                res = scenarios(j, c2[q])
                temp.append(res)
                q += 1
        for l in temp:
            sum += l
            results.append(sum)
    else:
        res = scenarios(a2[0], s2[0])
        results.append(res)

    if len(a1) > 1:
        sum = 0
        temp = []
        for j in a1:
            if len(s1) > 0:
                res1 = scenarios(j, s1[q])
                temp.append(res1)
                if len(c1) > 0:
                    res = scenarios(j, c1[q])
                    temp.append(res)
                q += 1
            else:
                res = scenarios(j, c1[q])
                temp.append(res)
                q += 1
        for l in temp:
            sum += l
        results.append(sum)
    else:
        res = scenarios(a1[0], s1[0])
        results.append(res)

for u in results:
    print(u, end=" ")
