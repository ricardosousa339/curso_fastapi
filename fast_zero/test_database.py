from fast_zero.database import get_session


def test_get_session():
    session_generator = get_session()
    session = next(session_generator)
    assert session is not None
    session_generator.close()
