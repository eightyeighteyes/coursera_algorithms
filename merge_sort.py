def merge_sort(unsorted):
    if len(unsorted) == 2:
        return [min(unsorted), max(unsorted)]
    elif len(unsorted) < 2:
        return unsorted
    else:
        return merge(unsorted)


def merge(unsorted):
    first = unsorted[:len(unsorted) / 2]
    last = unsorted[len(unsorted) / 2:]

    a = merge_sort(first)
    b = merge_sort(last)
    output = []
    i = 0
    j = 0
    for _ in range(len(unsorted)):
        if j > len(b) - 1:
            output.extend(a[i:])
            break
        elif i > len(a) - 1:
            output.extend(b[j:])
            break

        if a[i] < b[j]:
            output.append(a[i])
            i += 1
        else:
            output.append(b[j])
            j += 1
    return output
