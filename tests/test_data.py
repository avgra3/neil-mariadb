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
        "read_only": BASIC_CONFIG.read_only,
        "compress": BASIC_CONFIG.compress,
        "local_infile": BASIC_CONFIG.local_infile,
        "init_command": BASIC_CONFIG.init_command,
        "binary": BASIC_CONFIG.binary,
        "max_allowed_packet": BASIC_CONFIG.max_allowed_packet,
        "cache_prep_stmts": BASIC_CONFIG.cache_prep_stmts,
        "prep_stmt_cache_size": BASIC_CONFIG.prep_stmt_cache_size,
        "pipeline": BASIC_CONFIG.pipeline,
        "client_flag": BASIC_CONFIG.client_flag,
        "converter": BASIC_CONFIG.converter,
    }
    actual = as_dict(obj=BASIC_CONFIG)
    assert expected == actual
