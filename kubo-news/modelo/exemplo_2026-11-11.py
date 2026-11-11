import os
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from kubonews import *
o='saida/';os.makedirs(o,exist_ok=True)
cover('fotos/stripe.jpg','1 semana para criar','5 mil pessoas usando','A Stripe criou um agente de IA para toda a empresa, e a adoção foi rapidíssima',o+'stripe_1.jpg')
body('O QUE ACONTECEU','A Stripe ganhou um novo colega de trabalho',['A Stripe, uma das maiores empresas de pagamentos online do mundo, criou o Kai, um agente de IA para uso interno','A equipe construiu a ferramenta em cerca de uma semana','Em cerca de 4 semanas, ela já tinha aproximadamente 5 mil usuários'],o+'stripe_2.jpg',1)
body('POR QUE ISSO INSPIRA','Boas ideias com IA não precisam levar anos',['Com as ferramentas certas, um projeto pode sair do papel em dias','A procura por agentes de IA também cresceu entre quem não é programador','O desafio deixa de ser "dá para fazer?" e passa a ser "o que vale a pena fazer primeiro?"'],o+'stripe_3.jpg',2)
last('Blog da LangChain: "How Stripe Built Kai on Deep Agents in 1 Week", resumido pelo AIBriefs (9/11/2026)',o+'stripe_4.jpg')
cover('fotos/braine.jpg','Da USP','para o mundo','Startup brasileira apresenta no Web Summit Lisboa uma IA que ajuda a identificar sinais de autismo mais cedo',o+'braine_1.jpg')
body('O QUE ACONTECEU','Pesquisa brasileira no palco global',['A Braine nasceu de pesquisas na USP e criou o AURA-T, uma ferramenta de teletriagem','A IA analisa padrões de comportamento, linguagem e interação social de crianças','Ela não faz diagnóstico: organiza sinais para apoiar a busca por avaliação especializada'],o+'braine_2.jpg',1)
body('POR QUE ISSO INSPIRA','Tecnologia que encurta o caminho até o cuidado',['Mais de 1.000 triagens já feitas em campo','Mais de 40 organizações parceiras','Presença em mais de 30 municípios brasileiros','Pesquisa feita no Brasil virando produto e ganhando o mundo'],o+'braine_3.jpg',2)
last('Jornal da USP: "Startup criada na USP apresenta tecnologia para neurodiversidade no Web Summit Lisboa 2026" (9/11/2026)',o+'braine_4.jpg')
cover('fotos/mec.jpg','A IA chegou às escolas','com regras','O MEC definiu como a inteligência artificial pode ser usada da educação infantil à universidade',o+'mec_1.jpg')
body('O QUE MUDA','Pessoas continuam no comando',['A IA não pode decidir sozinha se um aluno é aprovado ou reprovado','Redações e trabalhos autorais continuam sendo avaliados por pessoas','Até o 5º ano, os alunos só usam IA com supervisão','Escolas e universidades têm 12 meses para se adaptar'],o+'mec_2.jpg',1)
body('POR QUE É UMA BOA NOTÍCIA','Regras claras abrem espaço para inovar',['A tecnologia entra na sala de aula de forma segura e com responsabilidade','Escolas, famílias e empresas de tecnologia ganham clareza sobre o que pode e o que não pode','O recado vale para qualquer setor: a IA ajuda, e as decisões importantes ficam com pessoas'],o+'mec_3.jpg',2)
last('MEC e Conselho Nacional de Educação, via Brasil 247 (10/11/2026) e Fast Company Brasil',o+'mec_4.jpg')
