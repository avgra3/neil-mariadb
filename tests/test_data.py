from .constants import BASIC_CONFIG


def test_NeilConfig_dictionary():
    expected = {
        "user": BASIC_CONFIG.username,
        "password": BASIC_CONFIG.password,
        "host": BASIC_CONFIG.hostname,
        "database": BASIC_CONFIG.database,
        "port": BASIC_CONFIG.port,
    }
    actual = BASIC_CONFIG.as_dict()
    assert expected == actual
