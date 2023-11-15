def test_version():
    import fastapicrud

    assert type(fastapicrud.__version__) is str


def test_version_file():
    from fastapicrud import _version

    assert type(_version.__version__) is str
