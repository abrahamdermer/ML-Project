def print_tabel(tabel:dict , distance  = 0)-> None:
    for k in tabel.keys():
        print(f'{'    '*distance }{k}:')
        if isinstance(tabel[k], dict):
            print_tabel(tabel[k] , distance + 1)
        else:
            print(f"{'    '*(distance+1)}{tabel[k]}")
