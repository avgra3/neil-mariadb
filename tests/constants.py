from neil import NeilConfig

BASIC_CONFIG = NeilConfig(username="user", password="pw")

SAMPLE_SQL_ONE = "SELECT id, name FROM person WHERE active = 1;"
SAMPLE_SQL_TWO = "SELECT id, name FROM person WHERE active = 1 GROUP BY location;"
SAMPLE_MULTIPLE_SQL = SAMPLE_SQL_ONE + SAMPLE_SQL_TWO

SAMPLE_SQL_WITH_LINE_COMMENTS = """SELECT person
-- This should not appear in the output
FROM person_table;
"""
SAMPLE_SQL_WITH_MULTILINE_COMMENTS = """SELECT person
/*
This should not appear in the output
*/
FROM person_table;
"""
SAMPLE_SQL_WITHOUT_LINE_COMMENTS = """SELECT person

FROM person_table;
"""
SAMPLE_SQL_WITHOUT_MULTILINE_COMMENTS = """SELECT person

FROM person_table;
"""
