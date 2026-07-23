from neil.data import as_dict

from .constants import BASIC_CONFIG


def test_NeilConfig_dictionary():
    expected = {
        "user": BASIC_CONFIG.user,
        "password": BASIC_CONFIG.password,
        "host": BASIC_CONFIG.host,
        "database": BASIC_CONFIG.database,
        "port": BASIC_CONFIG.port,
        "autocommit": BASIC_CONFIG.autocommit,
        "compress": BASIC_CONFIG.compress,
        "local_infile": BASIC_CONFIG.local_infile,
        "init_command": BASIC_CONFIG.init_command,
        "converter": BASIC_CONFIG.converter,
    }
    actual = as_dict(obj=BASIC_CONFIG)
    assert expected == actual
