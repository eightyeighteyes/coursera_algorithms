def sort_and_count_inversions(unsorted):
    inversions = 0
    if len(unsorted) < 2:
        return inversions, unsorted
    elif len(unsorted) == 2:
        sort = [min(unsorted), max(unsorted)]
        if unsorted != sort:
            inversions += 1
    else:
        inversions, sort = sort_and_count_split_inversions(unsorted)

    return inversions, sort


def sort_and_count_split_inversions(unsorted):
    first = unsorted[:len(unsorted) / 2]
    last = unsorted[len(unsorted) / 2:]

    a_count, a = sort_and_count_inversions(first)
    b_count, b = sort_and_count_inversions(last)

    output = []
    i = 0
    j = 0
    inversions = a_count + b_count

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
            inversions += len(a) - i

    return inversions, output


def count_inversions(container):
    return sort_and_count_inversions(container)[0]
