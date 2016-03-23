from django.core.paginator import Paginator


def group_list(obj_list, n):
    """
    Group lst by n elements.
    Example:
    lst = [1,2,3,4,5,6]
    group_list(lst,2) -> [[1,2],[3,4],[5,6]]
    """
    pager = Paginator(obj_list, n)
    return [pager.page(N).object_list for N in pager.page_range]


def grouplist(obj_lst, n, tail=False):
    """
    Group lst by n elements.
    Example:
    lst = [1,2,3,4,5,6]
    grouplist(lst,2) -> [[1,2],[3,4],[5,6]]
    """
    L = []
    c = 0
    while c+n <= len(obj_lst):
        L.append(obj_lst[c:c + n])
        c += n
    if tail and (obj_lst[c:] != []):
        L.append(obj_lst[c:])
    return L
