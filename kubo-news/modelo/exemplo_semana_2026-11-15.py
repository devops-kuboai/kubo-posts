from kubonews import *
o='news4/'
P={
'patogenos':('px/4033145.jpg','Uma IA que detecta vírus','sem internet','Um notebook e um sequenciador de DNA ligado na porta USB: é tudo de que ela precisa',
 ('O QUE ACONTECEU','Um laboratório que cabe na mochila',['A startup americana Radical Numerics apresentou o Omnii Defense, um modelo de IA que analisa sequências genéticas','Ele roda em um notebook com um sequenciador de DNA ligado na porta USB, sem precisar de internet','Para cada amostra, a IA estima se o organismo pode causar doenças e com qual grupo ele mais se parece']),
 ('POR QUE ISSO INSPIRA','Ciência de ponta onde ela é mais necessária',['Pesquisadores em campo, longe de laboratórios e sem conexão, podem analisar amostras na hora','Em testes, a IA conseguiu sinalizar vírus que ela nunca tinha visto no treinamento','A empresa trabalha com laboratórios e agências públicas para avaliar a ferramenta']),
 'Wired: "A Startup Wants to Fight AI Bioweapons With AI" (11/11/2026)'),
'alia':('px/37605911.jpg','IA feita no Ceará','premiada em São Paulo','O laboratório Alia, do Instituto Atlântico, ficou em 2º lugar no Prêmio GTIS 2026',
 ('O QUE ACONTECEU','Um laboratório de IA no Nordeste',['O Alia é o Laboratório de Inteligência Artificial do Instituto Atlântico, no Ceará','O Prêmio GTIS 2026 reconhece projetos de tecnologia, inovação e sustentabilidade no Brasil','O laboratório tem cerca de R$ 15 milhões em infraestrutura, com 17 GPUs e quase 1 petabyte de armazenamento']),
 ('POR QUE ISSO INSPIRA','Inovação de ponta em todo o Brasil',['O Alia apoia a formação em IA, a pesquisa aplicada e soluções para empresas','A meta, segundo o instituto, é transformar pesquisa em inovação aplicada','O Instituto Atlântico soma 25 anos de pesquisa, desenvolvimento e inovação']),
 'Portal Terra da Luz: "Laboratório de IA do Ceará conquista prêmio nacional" (13/11/2026)'),
'ibm':('px/2105927.jpg','IBM apresenta','novo chip quântico','O Nighthawk r3 terá 520 qubits e foi projetado para rodar 10 mil operações quânticas',
 ('O QUE ACONTECEU','Mais poder para a computação quântica',['A IBM anunciou o Nighthawk r3, a próxima geração do seu processador quântico','Ele terá 520 qubits programáveis e foi projetado para 10 mil operações quânticas','O modelo atual, o Nighthawk r2, roda mais de 7.500 operações com 120 qubits']),
 ('POR QUE ISSO INSPIRA','Um passo rumo aos problemas mais difíceis',['Em 2027, a IBM planeja ligar dois chips e chegar a um sistema com 1.040 qubits','A computação quântica promete resolver problemas complexos demais para os computadores de hoje','O chip também vai apoiar pesquisas de correção de erros, um dos grandes desafios da área']),
 'The Quantum Insider e SiliconANGLE, sobre o anúncio da IBM (11/11/2026)'),
'wallet':('px/7007188.jpg','O ChatGPT agora','faz compras por você','A OpenAI lançou o ChatGPT Wallet, e os agentes de IA já podem finalizar compras',
 ('O QUE ACONTECEU','Do pedido ao pagamento, em uma conversa',['Com o ChatGPT Wallet, a pessoa cadastra o cartão uma vez e pede para a IA comprar','Antes de pagar, ela revisa os itens e o valor e confirma com Face ID ou digital','O cartão é cobrado por um token: nem a IA nem a loja veem o número do cartão']),
 ('POR QUE ISSO IMPORTA','O jeito de comprar está mudando',['Por enquanto, a novidade foi liberada para parte dos assinantes do ChatGPT Pro nos EUA','A OpenAI publicou um guia para lojas que querem atender quem compra usando IA','A pergunta para quem vende: sua loja está pronta para ser encontrada e comprada por uma IA?']),
 'TechCrunch: "ChatGPT\'s new Wallet lets AI agents shop and check out for you" (13/11/2026)'),
'dna':('px/3735769.jpg','Uma IA que ajuda','a ler o DNA','O Google DeepMind lançou o AlphaGenome 2, que prevê como mudanças no DNA afetam cada tipo de célula',
 ('O QUE ACONTECEU','Um novo aliado da pesquisa genética',['O AlphaGenome 2 prevê como variações no DNA afetam tipos específicos de células humanas','Ele foi treinado com mais de 100 milhões de perfis de células, de 68 tecidos','Ele encontra quase o dobro de variantes que alteram a atividade dos genes, em comparação ao melhor modelo anterior']),
 ('POR QUE ISSO INSPIRA','Mais caminhos para entender doenças',['Pesquisadores podem investigar com mais precisão a origem genética de doenças','O modelo já está disponível para pesquisa não comercial','É uma ferramenta de pesquisa: não é usada para diagnóstico']),
 'Google DeepMind: "AlphaGenome 2: deciphering how cells read DNA to better understand disease" (11/11/2026)'),
'drone':('px/drone.jpg','Entrega por drone','em menos de 2 horas','A Amazon recebeu autorização para ampliar as entregas por drone no Reino Unido',
 ('O QUE ACONTECEU','De 600 para 8 mil casas',['A autoridade de aviação do Reino Unido aprovou a ampliação do Prime Air em Darlington','Segundo a Amazon, é a primeira aprovação desse tipo concedida no mundo','O número de casas atendidas sobe de cerca de 600 para aproximadamente 8 mil']),
 ('POR QUE ISSO INSPIRA','A logística do futuro já está voando',['Os drones levam itens de até 2,2 kg em menos de duas horas','Eles atendem clientes num raio de 12 km do centro de distribuição','O serviço está incluído na assinatura Prime, sem taxa extra de entrega']),
 'Retail Times: "Amazon secures landmark UK approval to expand drone deliveries" (10/11/2026)'),
}
names=list(P)
for nm,(ph,t1,t2,sub,b1,b2,src) in P.items():
    cover(ph,t1,t2,sub,o+nm+'_1.jpg')
    body(*b1,o+nm+'_2.jpg',1);body(*b2,o+nm+'_3.jpg',2)
    last(src,o+nm+'_4.jpg')
m=Image.new('RGB',(2160,675*len(names)))
for j,nm in enumerate(names):
    for k in range(4): m.paste(Image.open(f'{o}{nm}_{k+1}.jpg').resize((540,675)),(k*540,j*675))
m.resize((1440,450*len(names))).save('prev_semana.jpg')
