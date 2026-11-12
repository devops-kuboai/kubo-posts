# Modelo KUBO News

Gera os carrosséis da série KUBO News no padrão aprovado (1080 x 1350, formato 4:5).

## Padrão visual
- Capa: foto na metade de cima, com o selo "Imagem ilustrativa" quando a foto for gerada por IA
- Telas internas: fundo claro, "O que aconteceu" e "Por que isso inspira"
- Última tela: fonte da notícia e "Siga a KUBO AI"
- Em todas as telas: selo "KUBO NEWS" igual no topo e logo no canto inferior esquerdo
- Títulos sempre sem ponto final
- Tom positivo e inspirador, sobre o mundo da tecnologia

## Como usar
1. Coloque a foto da capa em `fotos/` (horizontal 3:2, sem logotipos de marcas)
2. Copie `exemplo_2026-11-11.py`, troque os textos e rode: `python3 exemplo.py`
3. As telas saem em `saida/`. Suba em `kubo-news/AAAA-MM-DD/` neste repositório
4. Publique o carrossel com os links raw do GitHub

Requisitos: Python 3 com Pillow e NumPy, e a fonte Inter Display (arquivos `InterDisplay-*.otf`).
Se a fonte estiver em outra pasta, use a variável `KUBO_FONTES`.
Para usar o logo oficial no lugar do recorte, defina `LOGO=caminho/do/logo.png`.

# Modelo dos posts de produto (Agent-Hub e Follow Up)

Fica em `produto/`. Visual diferente das notícias, para separar na galeria:
- Cada tela com uma cor forte (branco, gradiente azul e violeta, amarelo)
- Produto citado já na capa, título gigante e destaque amarelo
- Selo com o nome do produto (AGENT-HUB ou FOLLOW UP) e logo no canto inferior esquerdo
- Títulos sem ponto final

Exemplo: `python3 produto/agenthub_carrossel.py` gera o carrossel "22h, a loja fechou" em `saida/`.
Rascunhos ficam em `conteudo-kubo/<produto>/rascunhos/` e, depois de aprovados, em `conteudo-kubo/<produto>/AAAA-MM-DD/`.
