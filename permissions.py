main_permissions = set(input("Main permissions: ").strip().lower().split(','))
secondary_permissions = set(input("Secondary permissions: ").strip().lower().split(','))

for i in range(len(main_permissions)):
    main_permissions[i] = main_permissions[i].strip()

for i in range(len(secondary_permissions)):
    secondary_permissions[i] = secondary_permissions[i].strip()

conjunct = secondary_permissions.issubset(main_permissions)

if conjunct:
    print("The permisions are main")
else:
    print("The permision is secondary")