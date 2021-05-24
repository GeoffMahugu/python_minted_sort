
from question_2 import py3_sort_multilevel_rejections

failure_reasons_1 = [{'primary_reason': 'zeta',
  'second_levels': [{'id': '1', 'reason': 'zed', 'type': 'zed'}]},
 {'primary_reason': 'other',
  'second_levels': [{'id': '1', 'reason': 'other', 'type': 'bar'},
                    {'id': '1', 'reason': 'sec2', 'type': 'foo'}]},
 {'primary_reason': 'first1',
  'second_levels': [{'id': '3', 'reason': 'zebra', 'type': 'foo'},
                    {'id': '45', 'reason': 'other', 'type': 'foo'},
                    {'id': '7', 'reason': 'alpha', 'type': 'foo'}]}]

failure_reasons_1_expected_result = [{'primary_reason': 'first1',
  'second_levels': [{'id': '3', 'reason': 'zebra', 'type': 'foo'},
                    {'id': '7', 'reason': 'alpha', 'type': 'foo'},
                    {'id': '45', 'reason': 'other', 'type': 'foo'}]},
 {'primary_reason': 'zeta',
  'second_levels': [{'id': '1', 'reason': 'zed', 'type': 'zed'}]},
 {'primary_reason': 'other',
  'second_levels': [{'id': '1', 'reason': 'sec2', 'type': 'foo'},
                    {'id': '1', 'reason': 'other', 'type': 'bar'}]}]

def test_2_py3_sort_multilevel_rejections():
    assert py3_sort_multilevel_rejections(failure_reasons_1) == failure_reasons_1_expected_result

def test_2_py3_sort_empty_rejection_reasons():
    assert py3_sort_multilevel_rejections([]) == None
