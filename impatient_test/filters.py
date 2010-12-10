


def filter_by_case_fn_attr(prop, tds):
    ret_tds = []
    for td in tds:
        if getattr(td.case_fn, prop, False):
            ret_tds.append(td)
    return ret_tds
