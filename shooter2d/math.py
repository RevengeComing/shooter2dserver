def nearly_equal(a, b, sig_fig=4):
    return (
        a == b or
        int(a*10**sig_fig) == int(b*10**sig_fig)
    )
