n = int(input())
i = 0
lst = []

while i < n:
    m = input().split()

    lst.append(m)
    i += 1


def merge_two_list(a, b, h):

    c = []
    i = j = 0

    while i < len(a) and j < len(b):
        if int(a[i][h]) < int(b[j][h]):
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


def merge_sort(list, h):

    if len(list) == 1:
        return list

    mid = len(list) // 2
    left = merge_sort(list[:mid], h)
    right = merge_sort(list[mid:], h)

    return merge_two_list(left, right, h)


list = merge_sort(lst, 3)


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


results = []
bl_list = []
temp = []


def search(lst, t):
    for i in lst:
        if i not in bl_list:
            if i[4] == "A":
                if t == i[3]:
                    bl_list.append(i)
                    for j in lst:
                        if j not in bl_list:
                            if i[3] == j[3]:
                                if j[4] == "C":
                                    res = scenarios(i, j)
                                    if res <= 0:
                                        res = 0
                                    else:
                                        bl_list.append(j)
                                        temp.append(res)
                                        search(lst, i[3])
                                        num = 0
                                        for k in temp:
                                            num += k
                                        if num != 0:
                                            results.append(num)
                                        temp.clear()
                                elif j[4] == "S":
                                    res = scenarios(i, j)
                                    if res <= 0:
                                        res = 0
                                    else:
                                        bl_list.append(j)
                                        temp.append(res)
                                        search(lst, i[3])
                                        num = 0
                                        for k in temp:
                                            num += k
                                        if num != 0:
                                            results.append(num)
                                        temp.clear()
        else:
            next


l = []


def sr(list):
    for d in list:
        search(list, d[3])


def fl():
    l.append(list[0])
    for i in list:
        if i[3] == l[0][3]:
            if i not in l:
                l.append(i)
        else:
            sort_date = merge_sort(l, 0)
            sr(sort_date)
            l.clear()
            l.append(i)
    sort_date = merge_sort(l, 0)
    sr(sort_date)


fl()


for e in results:
    print(e, end=" ")
