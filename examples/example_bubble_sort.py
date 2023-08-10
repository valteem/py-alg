# https://stackoverflow.com/a/58751479
# set PYTHONPATH to project folder

from algpy.sorting.bubble_sort import bubble_sort

def main():
    a = list("421543")
    bubble_sort(a)
    print(a)

if __name__ == "__main__":
    main()
