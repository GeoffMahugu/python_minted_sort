from functools import cmp_to_key
from operator import itemgetter

def py3_sort_multilevel_rejections(failure_reasons):

    if failure_reasons:
     
        def primary_sort(a,b):
            if a.get('primary_reason').lower() == "other":
                return 1
            elif b.get('primary_reason').lower() == "other":
                return -1
            return -1

        sorted_primary = sorted(failure_reasons, key=cmp_to_key(primary_sort))

        def _other_sort(a, b):
            if a.get('reason').lower() == "other":
                return 1
            elif b.get('reason').lower() == "other":
                return -1
            return 0

        for index,item in enumerate(sorted_primary):
            if item.get('second_levels'):
                second_sort = sorted(item['second_levels'], key=cmp_to_key(_other_sort))
                sorted_primary[index]['second_levels'] = second_sort

        return sorted_primary

    else: 
        return None
