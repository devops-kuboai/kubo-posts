import sys,os
AQUI=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,os.path.join(AQUI,'..'))
exec(open(os.path.join(AQUI,'vivid.py')).read())
from PIL import ImageFilter
INK=(10,14,30);TEAL=(13,148,136);BLUE=(22,104,240);AMB=(255,184,0);RED=(229,57,53);GRN=(22,163,74);MUT=(84,100,132)
TAG='FOLLOW UP SOLUTION'

def hl(d,x,y,txt,fo,fill,bg):
    w=d.textlength(txt,font=fo);b=d.textbbox((x,y),txt,font=fo)
    d.rectangle((x-12,b[1]+fo.size*0.18,x+w+12,b[3]+8),fill=bg);d.text((x,y),txt,font=fo,fill=fill)

def foot(c,i,n,dark=False):
    d=ImageDraw.Draw(c);tc='white' if dark else INK;sc=(220,240,238) if dark else MUT
    c.alpha_composite(K.CUBE.resize((58,62)),(70,H-122))
    d.text((142,H-114),'KUBO AI',font=f('Bold',32),fill=tc);d.text((142,H-78),'@_kuboai',font=f('Medium',23),fill=sc)
    for k in range(n):
        cx=W-90-(n-1-k)*26;d.ellipse((cx-6,H-100,cx+6,H-88),fill=(AMB if dark else TEAL) if k==i else ((255,255,255,90) if dark else (205,214,222)))

def painel(rows,alerta=None,w=560):
    """cartao de painel de fornecedores"""
    h=150+len(rows)*118+(130 if alerta else 0)
    im=Image.new('RGBA',(w+60,h+60),(0,0,0,0));sh=Image.new('RGBA',im.size,(0,0,0,0))
    ImageDraw.Draw(sh).rounded_rectangle((30,40,w+30,h+30),36,fill=(0,20,30,120));im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(18)))
    d=ImageDraw.Draw(im);x0,y0=30,30
    d.rounded_rectangle((x0,y0,x0+w,y0+h),36,fill='white')
    d.text((x0+36,y0+34),'Fornecedores',font=f('Black',36),fill=INK)
    d.text((x0+36,y0+82),'Projeto Linha 3',font=f('Medium',24),fill=MUT)
    y=y0+140
    for nome,pct,st,col in rows:
        d.text((x0+36,y),nome,font=f('Bold',28),fill=INK)
        fo=f('Bold',22);tw=d.textlength(st,font=fo)
        d.rounded_rectangle((x0+w-36-tw-32,y-4,x0+w-36,y+34),17,fill=col+(40,) if False else tuple(int(255-(255-v)*0.18) for v in col))
        d.text((x0+w-36-tw-16,y+2),st,font=fo,fill=col)
        d.rounded_rectangle((x0+36,y+52,x0+w-36,y+66),7,fill=(230,236,240))
        d.rounded_rectangle((x0+36,y+52,x0+36+int((w-72)*pct),y+66),7,fill=col)
        y+=118
    if alerta:
        d.rounded_rectangle((x0+24,y+4,x0+w-24,y+108),24,fill=(255,243,224))
        d.ellipse((x0+48,y+30,x0+100,y+82),fill=AMB);d.text((x0+66,y+30),'!',font=f('Black',40),fill=INK)
        ls=wrap(d,alerta,f('SemiBold',24),w-170);yy=y+56-len(ls)*15
        for l in ls: d.text((x0+120,yy),l,font=f('SemiBold',24),fill=INK);yy+=30
    return im

ROWS=[('Montagem elétrica',0.82,'No prazo',GRN),('Usinagem de peças',0.45,'Atenção',(217,119,6)),('Pintura industrial',0.30,'Atrasado',RED)]

def capa(stamp_txt,linhas,hls,sub,alerta,out,n=4,rows=ROWS,py=690):
    c=Image.new('RGBA',(W,H),(255,255,255))
    c.paste(grad(TEAL,BLUE).crop((0,720,W,H)),(0,720));d=ImageDraw.Draw(c,'RGBA')
    for k in range(4): d.ellipse((640-k*60,840-k*60,1420+k*60,1620+k*60),outline=(255,255,255,40),width=3)
    stamp(c,stamp_txt,70,100,TEAL,'white')
    fo=f('Black',100);y=200
    for i,l in enumerate(linhas):
        if i in hls: hl(d,66,y,l,fo,INK,AMB)
        else: d.text((66,y),l,font=fo,fill=INK)
        y+=116
    para(d,70,800,sub,f('Bold',38),'white',430,1.3)
    foot(c,0,n,dark=True)
    p=painel(rows,alerta,500);p=p.rotate(-4,expand=True,resample=Image.BICUBIC);c.alpha_composite(p,(W-p.width+40,py))
    c.convert('RGB').save(out,quality=92)

def cards(titulo,itens,out,i,n=4,fundo='grad'):
    dark=fundo=='grad'
    c=grad(TEAL,BLUE) if dark else Image.new('RGBA',(W,H),(255,255,255))
    d=ImageDraw.Draw(c)
    stamp(c,TAG,70,100,AMB if dark else TEAL,INK if dark else 'white')
    y=210
    for l in titulo: d.text((66,y),l,font=f('Black',92),fill='white' if dark else INK);y+=100
    y+=50
    for lab,t in itens:
        d.rounded_rectangle((70,y,W-70,y+176),30,fill='white' if dark else (240,247,247))
        d.rounded_rectangle((100,y+38,214,y+138),24,fill=AMB if dark else TEAL)
        fo2=f('Black',30 if len(lab)<6 else 22);d.text((157-d.textlength(lab,font=fo2)/2,y+88-fo2.size*0.6),lab,font=fo2,fill=INK if dark else 'white')
        ls=wrap(d,t,f('SemiBold',36),690);yy=y+88-len(ls)*23
        for l in ls: d.text((250,yy),l,font=f('SemiBold',36),fill=INK);yy+=46
        y+=200
    foot(c,i,n,dark=dark);c.convert('RGB').save(out,quality=92)

def cta(linhas,botao,sub,out,n=4):
    c=Image.new('RGBA',(W,H),AMB);d=ImageDraw.Draw(c)
    stamp(c,TAG,70,100,INK,'white')
    y=230
    for l in linhas: d.text((66,y),l,font=f('Black',96),fill=INK);y+=106
    y+=40;fb=f('Bold',42);bw=d.textlength(botao,font=fb)
    d.rounded_rectangle((70,y,70+bw+100,y+104),52,fill=INK);d.text((120,y+27),botao,font=fb,fill='white')
    y+=140;para(d,70,y,sub,f('SemiBold',36),INK,470,1.28)
    foot(c,n-1,n)
    p=painel(ROWS,None,470).rotate(-5,expand=True,resample=Image.BICUBIC);c.alpha_composite(p,(W-p.width+60,H-p.height+120))
    c.convert('RGB').save(out,quality=92)

if __name__=='__main__':
    o=os.path.join(AQUI,'..','saida','followup')+'/';os.makedirs(o,exist_ok=True)
    # A) LinkedIn: quanto custa cobrar um fornecedor
    capa(TAG,['QUANTO CUSTA','COBRAR UM','FORNECEDOR?'],[2],'Ligações, visitas e planilhas também entram na conta',None,o+'custo_1.jpg')
    cards(['O CUSTO QUE','NÃO APARECE'],[('TEL','Ligações e mensagens só para saber o andamento do serviço'),('VISITA','Deslocamentos para conferir se o trabalho avançou'),('PLAN','Planilhas desatualizadas e informações espalhadas')],o+'custo_2.jpg',1)
    cards(['TUDO EM UM','SÓ LUGAR'],[('PRAZO','Prazos e evolução de cada fornecedor em tempo real'),('FOTO','Evidências do serviço centralizadas na plataforma'),('ALERTA','Atrasos sinalizados antes de virarem problema')],o+'custo_3.jpg',2,fundo='branco')
    cta(['QUANTO TEMPO','SUA EQUIPE','GASTA COBRANDO','FORNECEDORES?'],'Agende uma demonstração','Fale com a KUBO AI pelo Direct ou WhatsApp',o+'custo_4.jpg')
    # B) Instagram: o projeto atrasou e ninguem avisou
    capa(TAG,['O PROJETO','ATRASOU E','NINGUÉM','AVISOU'],[2,3],'Com o Follow Up Solution, o aviso chega antes','Pintura industrial: etapa 2 com 3 dias de atraso',o+'projeto_1.jpg',rows=[ROWS[0],ROWS[2]],py=700)
    cards(['SEXTA, 17H','O PRAZO ERA HOJE'],[('1','O fornecedor não respondeu as mensagens da semana'),('2','A última atualização estava numa planilha antiga'),('3','O atraso só apareceu quando já era tarde')],o+'projeto_2.jpg',1)
    cards(['AGORA, COM O','FOLLOW UP'],[('ALERTA','O sistema avisa quando uma etapa começa a atrasar'),('FOTO','Evolução e evidências de cada fornecedor num só lugar'),('AGIR','Você decide antes do prazo, não depois')],o+'projeto_3.jpg',2,fundo='branco')
    cta(['NENHUM','PROJETO','ATRASADO DE','SURPRESA'],'Chame no Direct','ou comente PROJETO aqui embaixo',o+'projeto_4.jpg')
    m=Image.new('RGB',(2160,1350))
    for j,nm in enumerate(['custo','projeto']):
        for k in range(4): m.paste(Image.open(f'{o}{nm}_{k+1}.jpg').resize((540,675)),(k*540,j*675))
    m.save(o+'previa.jpg',quality=88)
