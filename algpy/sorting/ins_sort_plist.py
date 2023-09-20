# insertion sor of positional list

def ins_sort_plist(pl) -> None:
    point = pl.tail()
    while point != pl.head():
        handle = pl.after(point) #assume silently that positional length is longer than one element
        elt = handle.elt()
        if elt > point.elt():
            point = handle
        else:
            move = point
            while move != pl.tail() and pl.before(move).elt() > elt:
                move = pl.before(move)
            pl.remove(handle)
            pl.insert_before(elt, move)