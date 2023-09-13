from main import Add, Multiply

def Test():
    assert Add(2, 3) == 5
    print("Add Function works correctly")

    assert Multiply(2, 3) == 6
    print("Multiply Function works correctly")

if __name__ == '__main__':
    Test()