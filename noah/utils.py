import os

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def cleanup_temp_files(file_paths):
    """
    Method to remove files from given file_paths
    :param file_paths: Array containing local file paths
    """
    for path in file_paths:
        try:
            os.remove(path)
        except OSError:
            pass


# get paginated response
def get_paginated_response(objects, page_no, offset):
    # create paginator
    paginator = Paginator(objects, offset)

    # get objects of the page
    try:
        objects = paginator.page(page_no)
    except PageNotAnInteger:
        # If page is invalid then return first page data
        objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999),
        # deliver last page of results.
        objects = paginator.page(paginator.num_pages)

    data = {
        'results': objects.object_list,
        'count': paginator.count,
        'previous': objects.previous_page_number() if objects.has_previous() else None,
        'next': objects.next_page_number() if objects.has_next() else None
    }

    # return objects
    return data
