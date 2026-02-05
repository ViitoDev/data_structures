text1 = set("The bright light flickered in the hallway".lower().split())
text2 = set("She carried a light bag for the long walk.".lower().split())

comuns = text1.intersection(text2)
print(f"Common words: {comuns}")