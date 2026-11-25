"""Versão final (25/11) do carrossel da pizzaria: 4 telas, sem a lista de conversas."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import loja_noite as L, pizzaria_bf as P
orig=L.foot;MAP={0:0,2:1,3:2,4:3}
def foot(c,i,dark=False): L.N=4;orig(c,MAP[i],dark)
L.foot=foot
o=sys.argv[1];os.makedirs(o,exist_ok=True)
P.capa(o+'pizzaria_1.jpg');P.quem(o+'pizzaria_2.jpg');P.solucao(o+'pizzaria_3.jpg');P.cta(o+'pizzaria_4.jpg')
