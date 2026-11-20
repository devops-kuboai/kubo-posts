"""Agent-Hub (25/11): 3 sinais de que o atendimento vai travar na Black Friday. Slides para reel."""
import sys,os
AQUI=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,AQUI)
_s=open(os.path.join(AQUI,'blackfriday.py')).read();exec(_s[:_s.index("def celular")])
def base(n=None):
    c=Image.new('RGBA',(W,H),YEL);d=ImageDraw.Draw(c,'RGBA')
    for r in (300,370,440): d.ellipse((1150-r,1350-r,1150+r,1350+r),outline=INK,width=3)
    stamp(c,'AGENT-HUB · BLACK FRIDAY',70,200,INK,'white')
    c.alpha_composite(K.CUBE.resize((58,62)),(70,H-122));d=ImageDraw.Draw(c)
    d.text((142,H-114),'KUBO AI',font=f('Bold',32),fill=INK);d.text((142,H-78),'@_kuboai',font=f('Medium',23),fill=(84,100,132))
    if n: d.text((W-150,H-118),n,font=f('Bold',30),fill=INK)
    return c,d
def capa(out):
    c,d=base();fo=f('Black',110);y=300
    for l in ['3 SINAIS','DE QUE SEU','ATENDIMENTO','VAI TRAVAR']: d.text((66,y),l,font=fo,fill=INK);y+=118
    y+=30;fo2=f('Black',44);t='na Black Friday';w=d.textlength(t,font=fo2)
    d.rectangle((70,y,70+w+40,y+76),fill=INK);d.text((90,y+12),t,font=fo2,fill='white')
    c.convert('RGB').save(out,quality=92)
def sinal(out,num,l1,txt):
    c,d=base(f'{num}/3');d.text((60,280),num,font=f('Black',300),fill=INK)
    y=640;fo=f('Black',76)
    for l in l1: d.text((66,y),l,font=fo,fill=INK);y+=86
    para(d,70,y+30,txt,f('SemiBold',40),INK,900,1.3);c.convert('RGB').save(out,quality=92)
def fim(out):
    c,d=base();fo=f('Black',96);y=300
    for l in ['O AGENT-HUB','RESPONDE','NA HORA']: d.text((66,y),l,font=fo,fill=INK);y+=106
    para(d,70,y+30,'24 horas por dia, no WhatsApp e no Instagram, com as informações do seu negócio',f('SemiBold',40),INK,900,1.3)
    y=880;d.rounded_rectangle((70,y,560,y+110),55,fill=INK);fb=f('Bold',44)
    d.text((315-d.textlength('Comente BLACK',font=fb)/2,y+29),'Comente BLACK',font=fb,fill='white')
    para(d,70,1020,'e receba a demonstração no Direct',f('SemiBold',36),INK,700,1.3)
    c.convert('RGB').save(out,quality=92)
if __name__=='__main__':
    o='/home/claude/kubo-posts/conteudo-kubo/agent-hub/2026-11-25/';os.makedirs(o,exist_ok=True)
    capa(o+'sinais_1.jpg')
    sinal(o+'sinais_2.jpg','1',['Cliente esperando','mais de 10 minutos'],'Quem espera muito por uma resposta no WhatsApp desiste e compra no concorrente')
    sinal(o+'sinais_3.jpg','2',['A mesma pergunta','50 vezes por dia'],'Frete, prazo, troca, tamanho: sua equipe responde tudo de novo, o dia inteiro')
    sinal(o+'sinais_4.jpg','3',['Ninguém responde','depois das 18h'],'A Black Friday vai até a madrugada, e o cliente quer resposta na hora')
    fim(o+'sinais_5.jpg')
