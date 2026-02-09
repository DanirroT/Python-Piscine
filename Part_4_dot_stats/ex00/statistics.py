
def ft_statistics(*args: any, **kwargs: any) -> None:
    for val in args:
        if isinstance(val, (int, float)) is not True:
            print("Error: All arguments must be numbers.")
            return
    count = len(args)
    if count == 0:
        print("ERROR")
        return
    sum_all = sum(args)
    args_sorted = sorted(args)
    mean = sum_all / count
    if count % 2 == 0:
        median = float((args_sorted[count//2 - 1] + args_sorted[count//2]) / 2)
        lower_half = args_sorted[:count//2]
        upper_half = args_sorted[count//2:]
    else:
        median = float(args_sorted[count//2])
        lower_half = args_sorted[:count//2+1]
        upper_half = args_sorted[count//2:]

    if len(upper_half) % 2 == 0:
        q3 = float((upper_half[len(upper_half)//2 - 1] + upper_half[len(upper_half)//2]) / 2)
    else:
        q3 = float(upper_half[len(upper_half)//2])

    if len(lower_half) % 2 == 0:
        q1 = float((lower_half[len(lower_half)//2 - 1] + lower_half[len(lower_half)//2]) / 2)
    else:
        q1 = float(lower_half[len(lower_half)//2])

    quartile = [q1, q3]
    std_var = sum((x - mean) ** 2 for x in args) / count
    std_dev = std_var ** 0.5
    for key, to_print in kwargs.items():
        if to_print == "mean":
            print(f"mean: {mean}")
        elif to_print == "median":
            print(f"median: {median}")
        elif to_print == "quartile":
            print(f"quartile: {quartile}")
        elif to_print == "std":
            print(f"std: {std_dev}")
        elif to_print == "var":
            print(f"var: {std_var}")
        else:
            print("ERROR")

#ft_statistics(1, 42, 360, 11, 64, 3, toto="median", tata="quartile")
#print("-----")
ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")


"""print(args_sorted)
    print(int(int(count/2)/2))
    print("q1", args_sorted[int(int(count/2)/2)], args_sorted[-((int(int(count/2)/2) * 3) + 1)])
    print(int(count/2))
    print("q2", args_sorted[int(count/2)], args_sorted[-(int(count/2) + 1)])
    print(int(int(count/2)/2) * 3)
    print("q3", args_sorted[int(int(count/2)/2) * 3], args_sorted[-(int(int(count/2)/2) + 1)])
    print(count)
    median = (args_sorted[int(count/2)] + args_sorted[-(int(count/2) + 1)]) / 2
    q1 = (args_sorted[int(int(count/2)/2)] + args_sorted[-((int(int(count/2)/2) * 3) + 1)]) / 2
    q3 = (args_sorted[(int(int(count/2)/2) * 3 - 1)] + args_sorted[-(int(int(count/2)/2))]) / 2"""