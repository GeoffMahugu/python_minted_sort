from question_1 import py3_sort_rejection_reasons

failure_reasons_1 = [{'type': 'TEXT', 'id': '4', 'reason': 'other'},
{'type': 'TEXT', 'id': '1', 'reason': 'spelling error'},
{'type': 'PHOTO', 'id': '2', 'reason': 'contrast'},
{'type': 'PHOTO', 'id': '3', 'reason': 'other'}];

failure_reasons_1_expected_result = [{'id': '1', 'reason': 'spelling error', 'type': 'TEXT'},
{'id': '2', 'reason': 'contrast', 'type': 'PHOTO'},
{'id': '4', 'reason': 'other', 'type': 'TEXT'},
{'id': '3', 'reason': 'other', 'type': 'PHOTO'}]

def test_py3_sort_rejection_reasons():
    assert py3_sort_rejection_reasons(failure_reasons_1) == failure_reasons_1_expected_result
def test_py3_sort_empty_rejection_reasons():
    assert py3_sort_rejection_reasons([]) == None
