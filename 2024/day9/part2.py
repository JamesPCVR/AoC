def find_len(element:int, _list:list) -> int:
    """find the number of neighbours from a starting index."""
    count = 0
    for i in range(len(_list)-1, 0, -1):
        li = _list[i]
        if li != element:
            continue
        if li != element and count != 0:
            break
        count += 1
    return count

def find_space(_list:list, _len:int, _max:int) -> int:
    """check if element of certain size exists and return index"""
    count = 0
    for i, n in enumerate(_list):
        if i >= _max:
            return -1
        if n == -1:
            count += 1
            if count >= _len:
                return i - count + 1
        else:
            count = 0
    return -1

def main():
    memory = []
    full_empty = True
    index = 0
    with open("in.txt", "r", encoding="utf-8") as f:
        while (c := f.read(1)) != "":
            if full_empty:
                # append data
                if c == "0":
                    index -= 1
                else:
                    memory.extend([index] * int(c))
            else:
                # append empty
                if c != "0":
                    memory.extend([-1] * int(c))
                index += 1
            full_empty = not full_empty

    bottom_id = memory[-1]
    for test_id in range(bottom_id, 0, -1):
        right = memory.index(test_id)
        block_size = find_len(test_id, memory)
        space = find_space(memory, block_size, right)

        if space == -1:
            continue
        for i in range(block_size):
            memory[space + i] = test_id
            memory[right + i] = -1

    checksum = 0
    for i, n in enumerate(memory):
        if n != -1:
            checksum += i * n

    print(checksum)

if __name__ == "__main__":
    main()
    # 6398065450842
    