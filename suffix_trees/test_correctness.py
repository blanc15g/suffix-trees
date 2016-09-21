from STree import STree

if __name__ == '__main__':
    st = STree("abcdefghab")
    assert st.find("abc") == 0
    assert st.find_all("ab") == [0,8]

    st_corner_case = STree("abcabd")
    assert st_corner_case.find("cab") == 2
    assert st_corner_case.find("ac") == -1
    assert st_corner_case.find_all("ac") == []

