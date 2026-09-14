from calculator import square


def main():
    test_square()


def test_square():
    try:
        assert square(-2) == 4
        assert square(-3) == 9
        assert square(0) == 0
        print("All tests passed!")
    except AssertionError:
        print("Test failed.")


if __name__ == "__main__":
    main()
