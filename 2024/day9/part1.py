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

    done = False
    checksum = 0
    for top_index, top_item in enumerate(memory):
        if top_item == -1:
            item = -1
            while (item := memory.pop()) == -1:
                if len(memory) <= top_index:
                    done = True
                    break
        else:
            item = top_item
        if not done:
            checksum += top_index * item

    print(checksum)

if __name__ == "__main__":
    main()
    # 6342014655338 too low
    # 6249861460223 (too low)
    # 9029345352181 too high
    # 6366928626680 too high
    # 6366665108136