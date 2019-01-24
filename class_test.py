class Hehe:
    def __init__(self, *args, hehe, haha):
        print(args)
        print(hehe)

if __name__ =="__main__":
    a = ("nihao","ni")
    b = {
        "hehe":"hehev",
        "haha":"hahav"
    }
    hehe = Hehe("nihao", "nimei", hehe="hehev", haha="haha")