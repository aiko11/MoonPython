# --------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------


def partial(func, *a_args):

    def wrapper(*b_args):
        args = list(a_args)
        args.extend(b_args)

        return func(*args)

    return wrapper

def logging(year, month, day, title, content):
    print("%s-%s-%s %s:%s" % (year,month, day, title, content))

def main():
    print("------------------ use logging function")
    logging("2019","03","09","python2", "End of support in 2020")
    logging("2019","03","09","python3", "Updateing")

    print("------------------ use partial function")
    f = partial(logging, "2019","03", "10")
    f("python2", "End of support in 2020")
    f("python3", "Updateing")

if __name__ == "__main__":
    main()
