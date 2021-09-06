class BrincandoComOQueAprendi:
    def __init__(self, fruta_1, fruta_2, fruta_3):
        self.f1 = fruta_1
        self.f2 = fruta_2
        self.f3 = fruta_3
        print(self.f1)

    def __len__(self):
        return len(self.f1)

    def __enter__(self):
        print('Se estou aparecendo é pq algo deu certo!')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Se eu apareci também... MARAVILHOSO!! Deu tudo certo!')


salada_de_fruta = {'fruta_1': 'Banana',
                   'fruta_2': 'Maça',
                   'fruta_3': 'Pera'}

brinquedo = BrincandoComOQueAprendi(**salada_de_fruta)

with brinquedo:
    print(len(brinquedo))
