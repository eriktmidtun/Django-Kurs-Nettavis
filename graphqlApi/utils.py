
def get_offset(qs, offset, count):
    if count:
        return qs[offset:offset + count]
    else:
        return qs[offset:]