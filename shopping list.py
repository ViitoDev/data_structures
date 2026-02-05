laura_list = set(["milk", "bread", "coffee", "sugar"])
ana_list = set(["bread", "coffee", "cookie", "chocolate"])

commons = laura_list.intersection(ana_list)
differents1 = laura_list.difference(ana_list)
differents2 = ana_list.difference(laura_list)

print(f"Commons: {', '.join(commons)}\nLaura's list exclusives: {', '.join(differents1)}\nAna's list exclusives: {','.join(differents2)}")