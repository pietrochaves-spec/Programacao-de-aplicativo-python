class Livro:
    def __init__ (self, titulo, autor, totalPaginas):
        self.titulo = titulo
        self.autor = autor
        self.totalPaginas = totalPaginas
        self.paginasLidas = 0

    def ler(self, paginas):
        self.paginasLidas += paginas
        if self.paginasLidas > self.totalPaginas:
            self.paginasLidas = self.totalPaginas

    def porcentagem_lida(self):
        return  self.paginasLidas/self.totalPaginas * 100

    def paginas_restantes (self):
        return self.totalPaginas - self.paginasLidas

    def terminou (self):
        return self.paginasLidas == self.totalPaginas

livro1 = Livro ("Pedrinhas", "Pedro", 100)
livro2 = Livro ("Rios", "João Marcos", 200)
livro1.ler(50)
print(livro1.porcentagem_lida())
print(livro1.paginas_restantes())
print(livro1.terminou())
livro2.ler(67)
print(livro2.porcentagem_lida())
print(livro2.paginas_restantes())
print(livro2.terminou())