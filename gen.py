def print_pyramid(n: int):
    """打印 n 层星号金字塔"""
    for i in range(1, n + 1):
        stars = "*" * (2 * i - 1)      # 每层 2i-1 个星号
        print(stars.center(2 * n - 1))  # 居中，宽度为最底层星号数


if __name__ == "__main__":
    print_pyramid(5)

    