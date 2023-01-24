import user
import find
import export
import write

while True:
    deystvie = user.Privet()
    if deystvie == 1:
        data = find.Poisk()
    elif deystvie == 2:
        write.Add()
    elif deystvie == 3:
        export.All()
    elif deystvie == 4:
        exit()