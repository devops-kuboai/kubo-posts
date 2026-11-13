import sys;sys.path.insert(0,'.')
import os;AQUI=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,os.path.join(AQUI,'..'));exec(open(os.path.join(AQUI,'vivid.py')).read())
INK=(10,14,30);BLUE=(22,104,240);VIO=(124,58,237);YEL=(255,214,10);GR=(70,80,110)
def hl(d,x,y,txt,fo,fill,bg):
    w=d.textlength(txt,font=fo);b=d.textbbox((x,y),txt,font=fo)
    d.rectangle((x-12,b[1]+fo.size*0.18,x+w+12,b[3]+8),fill=bg);d.text((x,y),txt,font=fo,fill=fill)
def foot(c,i,n,dark=False):
    d=ImageDraw.Draw(c);tc='white' if dark else INK;sc=(220,228,255) if dark else (84,100,132)
    c.alpha_composite(K.CUBE.resize((58,62)),(70,H-122))
    d.text((142,H-114),'KUBO AI',font=f('Bold',32),fill=tc);d.text((142,H-78),'@_kuboai',font=f('Medium',23),fill=sc)
    for k in range(n):
        cx=W-90-(n-1-k)*26;d.ellipse((cx-6,H-100,cx+6,H-88),fill=(YEL if dark else BLUE) if k==i else ((255,255,255,90) if dark else (205,210,228)))
o='saida/';os.makedirs(o,exist_ok=True);n=4
# 1 capa: metade branca com título forte + metade azul vibrante com o celular
c=Image.new('RGBA',(W,H),(255,255,255))
c.paste(grad((22,104,240),(124,58,237)).crop((0,700,W,H)),(0,700))
d=ImageDraw.Draw(c,'RGBA')
for k in range(4): d.ellipse((620-k*60,820-k*60,1400+k*60,1600+k*60),outline=(255,255,255,40),width=3)
stamp(c,'AGENT-HUB',70,100,BLUE,'white')
fo=f('Black',104);y=200
d.text((66,y),'22H, A LOJA',font=fo,fill=INK);y+=112
d.text((66,y),'FECHOU',font=fo,fill=INK);y+=122
hl(d,66,y,'A IA',fo,INK,YEL);y+=122
hl(d,66,y,'RESPONDEU',fo,INK,YEL)
pb=ph.resize((int(ph.width*0.78),int(ph.height*0.78)))
sh=Image.new('RGBA',(W,H));ImageDraw.Draw(sh).rounded_rectangle((640,700,640+pb.width,700+pb.height),50,fill=(0,0,30,140));c.alpha_composite(sh.filter(ImageFilter.GaussianBlur(30)))
c.alpha_composite(pb.rotate(-5,expand=True,resample=Image.BICUBIC),(610,660))
para(d,70,790,'Atendimento com IA no WhatsApp, no Instagram e no site',f('Bold',40),'white',450,1.28)
foot(c,0,n,dark=True);c.convert('RGB').save(o+'ah2_1.jpg',quality=92)
# 2 fundo azul sólido: o que ele faz
c=grad((22,104,240),(124,58,237));d=ImageDraw.Draw(c)
stamp(c,'AGENT-HUB',70,100,YEL,INK)
y=210
for l in ['O QUE O','AGENT-HUB FAZ']: d.text((66,y),l,font=f('Black',96),fill='white');y+=104
y+=50
for ic,t in [('24h','Responde clientes a qualquer hora, inclusive de madrugada'),('📄','Usa o cardápio, o catálogo e os documentos da sua empresa'),('👤','Passa a conversa para a sua equipe quando precisa')]:
    d.rounded_rectangle((70,y,W-70,y+170),30,fill=(255,255,255))
    d.rounded_rectangle((100,y+35,200,y+135),24,fill=YEL)
    lab='24h' if ic=='24h' else ('DOC' if ic=='📄' else 'EQUIPE')
    fo2=f('Black',30 if len(lab)<5 else 22);d.text((150-d.textlength(lab,font=fo2)/2,y+85-fo2.size*0.6),lab,font=fo2,fill=INK)
    ls=wrap(d,t,f('SemiBold',38),700);yy=y+85-len(ls)*24
    for l in ls: d.text((235,yy),l,font=f('SemiBold',38),fill=INK);yy+=48
    y+=195
foot(c,1,n,dark=True);c.convert('RGB').save(o+'ah2_2.jpg',quality=92)
# 3 branco: onde funciona + resultado
c=Image.new('RGBA',(W,H),(255,255,255));d=ImageDraw.Draw(c)
stamp(c,'AGENT-HUB',70,100,BLUE,'white')
y=210
for l in ['UM ATENDENTE','EM 3 CANAIS']: d.text((66,y),l,font=f('Black',96),fill=INK);y+=104
y+=60
for t,col in [('WhatsApp',(37,211,102)),('Instagram',(225,48,108)),('Site',BLUE)]:
    d.rounded_rectangle((70,y,W-70,y+130),65,fill=col);d.text((130,y+36),t,font=f('Black',50),fill='white')
    d.text((W-200,y+36),'✓' if False else 'OK',font=f('Black',50),fill='white');y+=155
y+=20;hl(d,70,y,'Mesmo agente, mesmas respostas',f('Black',44),INK,YEL)
foot(c,2,n);c.convert('RGB').save(o+'ah2_3.jpg',quality=92)
# 4 amarelo: CTA
c=Image.new('RGBA',(W,H),YEL);d=ImageDraw.Draw(c)
stamp(c,'AGENT-HUB',70,100,INK,'white')
y=260
for l in ['QUER VER','FUNCIONANDO','NO SEU','NEGÓCIO?']: d.text((66,y),l,font=f('Black',112),fill=INK);y+=120
y+=40;d.rounded_rectangle((70,y,640,y+110),55,fill=INK);d.text((120,y+28),'Chame no Direct',font=f('Bold',46),fill='white')
y+=150;d.text((70,y),'ou comente 1 aqui embaixo',font=f('SemiBold',38),fill=INK)
# celular da capa, no canto inferior direito
pb=ph.resize((int(ph.width*0.78),int(ph.height*0.78)))
sh=Image.new('RGBA',(W,H));ImageDraw.Draw(sh).rounded_rectangle((630,830,630+pb.width,830+pb.height),50,fill=(60,40,0,110));c.alpha_composite(sh.filter(ImageFilter.GaussianBlur(30)))
c.alpha_composite(pb.rotate(-5,expand=True,resample=Image.BICUBIC),(600,790))
foot(c,3,n);c.convert('RGB').save(o+'ah2_4.jpg',quality=92)
