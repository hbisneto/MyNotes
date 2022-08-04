# PyBridge
###### Last repository update: 25/06/2021

Com o PyBridge é possível executar scripts em Python fazendo uma ponte do código implementado no projeto criado com outras plataformas.
Uso sugerido pra quem precisa coletar dados de diferentes locais do sistema de arquivos do ambiente em que o projeto é executado.

Com o PyBridge é possível a implementação de scripts para:

1. Linux;
2. macOS;
3. Windows;

O PyBridge conta com uma biblioteca de ***tratamento de erros*** padrão que pode ser executada em qualquer ambiente. Qualquer método dentro da biblioteca pode ser chamado de qualquer parte do código. Desse jeito, não é necessário a implementação da chamada de exceção ```raise RuntimeError()``` dentro do módulo de execução do programa. Basta referenciar a chamada da função condizente com o tratamento que deve ser executado.

## Estrutura do projeto

***COLOCAR AQUI, UM TREEVIEW DA ESTRUTURA DO PROJETO. MOSTRANDO TODAS AS PASTAS E ARQUIVOS CRIADOS PELO PYBRIDGE***

.
├── _config.yml
├── _data
│   └── members.yml
├── _drafts
│   ├── begin-with-the-crazy-ideas.md
│   └── on-simplicity-in-technology.md
├── _includes
│   ├── footer.html
│   └── header.html
├── _layouts
│   ├── default.html
│   └── post.html
├── _posts
│   ├── 2007-10-29-why-every-programmer-should-play-nethack.md
│   └── 2009-04-26-barcamp-boston-4-roundup.md
├── _sass
│   ├── _base.scss
│   └── _layout.scss
├── _site
├── .jekyll-cache
│   └── Jekyll
│       └── Cache
│           └── [...]
├── .jekyll-metadata
└── index.html # can also be an 'index.md' with valid front matter

## Implementações futuras

* Adicionar suporte a ```Android```;
* Colocar o projeto criado no PyBridge em um ambiente virtual;
* Trabalhar o amadurecimento do software: Após o termino do período do implementeções, diminuir variáveis e tornar o processo ainda mais rápido e automatizado;
* Criar verificação dos arquivos de sistema: NÃO executar o PyBridge se os arquivos não estiverem devidamente instalados;