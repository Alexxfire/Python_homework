import user
import findd
import write

def main():
    while True:
        deystvie = user.Privet()
        if deystvie == 1:
            data = findd.Poisk()        #поиск
        elif deystvie == 2:
            write.Add()                 #новый ученик
        elif deystvie == 3:
            exit()

if __name__ == "__main__":
	main()