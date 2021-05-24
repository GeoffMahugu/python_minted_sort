from functools import cmp_to_key

def py3_sort_rejection_reasons(failure_reasons):
    if failure_reasons:
        def _other_sort(a, b):
            """ return similar to cmp

            If the a > b, cmp returns -1.
            If b > a cmp returns 1, 
            If a == b, cmp returns 0
            """
            if a.get('reason').lower() == "other":
                return 1
            elif b.get('reason').lower() == "other":
                return -1
            return 0
        return sorted(failure_reasons, key=cmp_to_key(_other_sort))
    else: 
        return None