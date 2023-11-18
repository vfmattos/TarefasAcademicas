/*Em um arquivo js, crie um objeto chamado Livro. 
Esse objeto deve possuir os atributos título, autor, totalDePaginas e paginaAtual.
 Crie o construtor desse objeto de forma que receba por parâmetro os atributos título, autor e totalDePaginas. 
 O atributo paginaAtual deve ser iniciado com valor 0. 
 Crie um método progressoDeLeitura que receba como parâmetro a página atual que o usuário está lendo. 
 Esse método deve modificar o valor do atributo paginaAtual e em seguida, retornar a porcentagem de leitura 
 (considerando o valor dos atributos totalDePaginas e páginaAtual.*/

 class Livro{
    constructor(titulo, autor, totalDePaginas){
        this.titulo = titulo;
        this.autor = autor;
        this.totalDePaginas = totalDePaginas;
        this.paginaAtual = 0;
    }

    progressoDeLeitura(pgnAtual){
        this.paginaAtual = pgnAtual;

        /*totaldePaginas = 100%
        paginaAtual = x%

        totaldePaginas * x% = paginaAtual * 100%
        x% = (paginaAtual * 100) / totaldePaginas*/

        var progresso = (this.paginaAtual * 100) / this.totalDePaginas;
        return `\nPágina atual: ${this.paginaAtual}\nProgresso de leitura: ${progresso.toFixed(0)}%\n`;
    }
 }

 const myBook = new Livro("Javascript: O guia Definitivo", "David Flanagan", 704);

 for(let i in myBook){
    if(i !== "paginaAtual"){
        console.log(`${i}: ${myBook[i]}`);
    }
    
 }

 console.log(myBook.progressoDeLeitura(352));