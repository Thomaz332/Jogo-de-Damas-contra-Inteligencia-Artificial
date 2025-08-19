class JogoDeDamas:
    def __init__(self):
        self.tabuleiro = [[0 for _ in range(8)] for _ in range(8)]
        self.jogador_atual = 1
        self.inicializar_tabuleiro()
    
    def inicializar_tabuleiro(self):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 1:
                    if i < 3:
                        self.tabuleiro[i][j] = 2
                    elif i > 4:
                        self.tabuleiro[i][j] = 1

    def imprimir_tabuleiro(self):
        print("  0 1 2 3 4 5 6 7")
        for i in range(8):
            linha = f"{i} "
            for j in range(8):
                if self.tabuleiro[i][j] == 0:
                    linha += ". " if (i + j) % 2 == 1 else "  "
                elif self.tabuleiro[i][j] == 1:
                    linha += "p "
                elif self.tabuleiro[i][j] == 2:
                    linha += "b "
            print(linha)

    def movimento_valido(self, linha_origem, coluna_origem, linha_destino, coluna_destino):
        # Verifica se está dentro do tabuleiro
        if not (0 <= linha_origem < 8 and 0 <= coluna_origem < 8 and
                0 <= linha_destino < 8 and 0 <= coluna_destino < 8):
            return False
        
        # Verifica se o movimento é diagonal
        if abs(linha_destino - linha_origem) != 1 or abs(coluna_destino - coluna_origem) != 1:
            print("Erro: Movimento não é diagonal de 1 casa")
            return False
        
        if self.tabuleiro[linha_destino][coluna_destino] != 0:
            print("Erro: Casa de destino não está vazia")
            return False

        if (linha_destino + coluna_destino) % 2 == 0:
            print("Erro: Casa de destino não é escura")
            return False
        
        return True

    def fazer_movimento(self, linha_origem, coluna_origem, linha_destino, coluna_destino):
        if self.movimento_valido(linha_origem, coluna_origem, linha_destino, coluna_destino):
            # Move a peça
            self.tabuleiro[linha_destino][coluna_destino] = self.tabuleiro[linha_origem][coluna_origem]
            self.tabuleiro[linha_origem][coluna_origem] = 0
            
            # Verifica se é uma captura
            if abs(linha_destino - linha_origem) == 2:
                # Remove a peça capturada
                linha_meio = (linha_origem + linha_destino) // 2
                coluna_meio = (coluna_origem + coluna_destino) // 2
                self.tabuleiro[linha_meio][coluna_meio] = 0
            
            # Promoção a dama
            if self.jogador_atual == 1 and linha_destino == 0:
                self.tabuleiro[linha_destino][coluna_destino] = 3  # Dama preta
            elif self.jogador_atual == 2 and linha_destino == 7:
                self.tabuleiro[linha_destino][coluna_destino] = 4  # Dama branca
            
            # Troca o jogador
            self.jogador_atual = 3 - self.jogador_atual
            return True
        return False
    
# Iniciar o jogo
if __name__ == "__main__":

    jogo = JogoDeDamas()
    print(jogo.fazer_movimento(5,0,4,1))
    jogo.imprimir_tabuleiro()
