# JOGO DA FORCA   RESPOSTA   =   banana

def jogar():
    print('**********************************')
    print('****Bem vindo ao Jogo da Forca****')
    print('**********************************')

    palavra_secreta = "banana"
    enforcou = False
    acertou = False
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    tentativas = 10

    print(letras_acertadas)

    while not enforcou and not acertou:
        index = 0
        print(f"\nVocê tem {tentativas} tentativas para acertar a palavra secreta.")

        if tentativas > 0:
            chute = input("\nChute uma letra que possa fazer parte da palavra secreta: ")
            chute = chute.strip().lower()
            if chute in palavra_secreta:
                tentativas -= 1
                print(f"\nVocê acertou!! ")
                for letra in palavra_secreta:
                    if chute == letra:
                        letras_acertadas[index] = letra
                        letras_faltando = str(letras_acertadas.count("_"))
                    index += 1

                if letras_faltando == "0":
                    print("\nVocê ganhou!! A palavra secreta foi descoberta. Parabéns!! ")
                    acertou = True
                else:
                    print(f"Agora faltam {letras_faltando} letras para completar a palavra secreta.")
                    print(letras_acertadas)
            else:
                tentativas -= 1
                print(f"\nVocê errou!!")
                letras_faltando = str(letras_acertadas.count("_"))
                print(f"Ainda faltam {letras_faltando} letras para completar a palavra.")
                print(letras_acertadas)
        else:
            print("Você perdeu!! Suas tentativas acabaram.")
            enforcou = True

    print('\nFim do jogo')

if __name__ == '__main__':
    jogar()