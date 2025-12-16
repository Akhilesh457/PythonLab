def split_into_chunks(lst, n):
    chunks_list = []                  # empty list to store sublists

    for i in range(0, len(lst), n):
        small_list = lst[i:i+n]  # create a sublist of size n
        chunks_list.append(small_list)

    return chunks_list
# -------- Main Program --------
def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8]  # given list
    n = 3                        # size of each chunk

    result = split_into_chunks(a, n)

    print("Original list:", a)
    print("Chunk size:", n)
    print("The list after splitting into chunks is:",n)
    print("Chunks:", result)

# calling main function
main()
