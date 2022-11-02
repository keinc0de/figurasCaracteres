class Operaciones:
    def __init__(self, caracter="*"):
        self.caracter = caracter

    def figura(self, w, sep=' ', pre=''):
        txt = ""
        for c in range(w):
            _ = self.caracter * (w-c)
            txt += (pre*c) + sep.join(_) + '\n'
        return txt

if __name__=="__main__":
    op = Operaciones()
    a = op.figura(4, ' '*1, ' '*4)
    print(a)

            