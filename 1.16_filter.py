def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


values = ['1', '2', '-3', '-', '4', 'N/A', '5']
ivals = list(filter(is_int, values))
print(ivals)
