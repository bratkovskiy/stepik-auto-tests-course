def test_input_text(expected_result, actual_result):
    stdin = expected_result
    stdout = actual_result
    assert stdin == stdout, \
        f"expected {stdin}, got {stdout}"

test_input_text(8,11)
