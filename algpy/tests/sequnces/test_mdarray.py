from algpy import init_md_array

def test_init_md_array():
    a = init_md_array(2, 2, 1)
    assert a[0][0] == 1
    assert a[1][1] == 1