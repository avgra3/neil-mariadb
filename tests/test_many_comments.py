from neil.neil import NeilPool

MULTI_STATEMENT_MULTI_COMMENT = """
/* This is the first comment
-- This should also be removed
SELECT -1 FROM nonexistant;
*/

/* This should also not exist -- Especially this */
SELECT 1 FROM existing;

/*This should not exist*/
"""

EXPECTED_MULTI_STATEMENT_MULTI_COMMENT = "SELECT 1 FROM existing;"


def test_weird_query_data():
    assert (
        NeilPool._remove_comments(sql_script=MULTI_STATEMENT_MULTI_COMMENT)
        == EXPECTED_MULTI_STATEMENT_MULTI_COMMENT
    )
