from pi.pi2 import process_input

def test_process_input():
    for i in range(1,16):
        assert process_input(i) != False

    l = ["1.1", "&", "four", 17, "18"]
    for i in l:
        assert process_input(i) == False