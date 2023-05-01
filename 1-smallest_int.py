def get_smallest_integer(my_list):
    """
    ereet
    """
    smallest = my_list[0]
    for n in my_list:
        if n < smallest:
            smallest = n
    return smallest


if __name__ == "__main__":
    my_list = [30, 58, 12, 59, 67, 20, 70]
    smallest = get_smallest_integer(my_list)
    print(f"The smallest integer in the list is: {smallest}")
