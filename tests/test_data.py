from neil.data import NeilResult, NeilResultMetaData, as_dict

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


def test_NeilResult_to_str():
    metadata = NeilResultMetaData(field=("field_name",))
    result = NeilResult(
        sqlStatement="SELECT 1 AS field_name",
        returnedData=[(1,)],
        updatedRows=1,
        metadata=metadata,
    )
    expected = (
        "SQL Ran: SELECT 1 AS field_name\nupdated/returned rows: 1\n|field_name|\n|1|\n"
        + str(metadata)
        + "\n"
    )
    actual = str(result)
    assert expected == actual
