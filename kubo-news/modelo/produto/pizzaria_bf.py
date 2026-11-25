"""Agent-Hub (25/11): pizzaria no pico da Black Friday, alto volume de mensagens."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import loja_noite as L
from loja_noite import *
L.N=5
FOTO=os.environ.get('FOTO','/tmp/fotos/pizzaria_pico.jpg')
TAG='AGENT-HUB · BLACK FRIDAY'
GREEN=(37,211,102)

def capa(out):
    c=Image.new('RGBA',(W,H),(255,255,255))
    ph=Image.open(FOTO).convert('RGB');ph=ImageEnhance.Brightness(ph).enhance(1.08)
    x0=int(ph.width*0.20);ph=ph.crop((x0,0,ph.width,ph.height));s=W/ph.width
    ph=ph.resize((W,int(ph.height*s))).crop((0,0,W,780));c.paste(ph,(0,0))
    d=ImageDraw.Draw(c,'RGBA');fi=f('SemiBold',20);t='Imagem ilustrativa';w=d.textlength(t,font=fi)
    d.rounded_rectangle((W-70-w-28,720,W-70,756),18,fill=(0,0,0,120));d.text((W-70-w-14,726),t,font=fi,fill='white')
    stamp(c,TAG,70,815,INK,'white',24)
    d=ImageDraw.Draw(c);y=890
    d.text((66,y),'BLACK FRIDAY NA PIZZARIA',font=f('Black',70),fill=INK);y+=100
    hl(d,70,y,'A promoção bombou',f('Black',56),INK,YEL);y+=88
    d.text((70,y),'E o WhatsApp também',font=f('Bold',56),fill=INK)
    L.foot(c,0);c.convert('RGB').save(out,quality=92)

def lista(out):
    c=Image.new('RGBA',(W,H),BG);d=ImageDraw.Draw(c)
    stamp(c,TAG,70,200,INK,'white',24)
    d.text((66,270),'SEXTA, 19H30',font=f('Black',84),fill=INK)
    hl(d,70,375,'47 conversas esperando resposta',f('Black',44),INK,YEL)
    y=470;d.rounded_rectangle((70,y,W-70,y+735),30,fill=(255,255,255))
    rows=[('Ana Paula','A promo de 2 grandes vale para entrega?','19:29',3),('Carlos','Quanto tempo para entregar no Centro?','19:28',2),
          ('Marcos','Cadê minha pizza? Pedi faz 1 hora','19:27',4),('Juliana','Aceita Pix?','19:27',1),
          ('Roberto','Me manda o cardápio da Black','19:26',2),('Bia','Oi?? Tem alguém aí?','19:25',5)]
    cols=[(255,159,67),(84,160,255),(238,90,111),(46,204,113),(155,89,182),(241,196,15)]
    yy=y+20
    for (n,m,h,k),cl in zip(rows,cols):
        d.ellipse((100,yy+14,184,yy+98),fill=cl);ini=n[0];fi=f('Black',38)
        d.text((142-d.textlength(ini,font=fi)/2,yy+32),ini,font=fi,fill='white')
        d.text((210,yy+14),n,font=f('Bold',34),fill=INK)
        fm=f('Medium',29);mm=m
        while d.textlength(mm,font=fm)>640: mm=mm[:-2]
        if mm!=m: mm=mm.rstrip()+'…'
        d.text((210,yy+60),mm,font=fm,fill=GR)
        fh=f('SemiBold',24);d.text((W-110-d.textlength(h,font=fh),yy+20),h,font=fh,fill=(30,170,80))
        d.ellipse((W-150,yy+58,W-110,yy+98),fill=GREEN);fk=f('Bold',24);t=str(k)
        d.text((W-130-d.textlength(t,font=fk)/2,yy+64),t,font=fk,fill='white')
        yy+=118
        if yy<y+700: d.line((210,yy-6,W-100,yy-6),fill=(236,238,244),width=2)
    L.foot(c,1);c.convert('RGB').save(out,quality=92)

def quem(out):
    c=Image.new('RGBA',(W,H),(255,255,255));d=ImageDraw.Draw(c)
    stamp(c,TAG,70,200,INK,'white',24)
    d.text((66,270),'E QUEM RESPONDE?',font=f('Black',88),fill=INK)
    y=410
    for t in ['O pizzaiolo está no forno','O atendente está no balcão','O motoboy espera o próximo pedido']:
        d.ellipse((74,y+12,100,y+38),fill=YEL);d.text((124,y),t,font=f('SemiBold',40),fill=INK);y+=64
    y+=40;hl(d,70,y,'Cada mensagem sem resposta',f('Black',54),INK,YEL);y+=86
    hl(d,70,y,'é um pedido que esfria',f('Black',54),INK,YEL)
    ph=Image.open(FOTO).convert('RGB');ph=ImageEnhance.Brightness(ph).enhance(1.1)
    ph=ph.crop((0,100,1000,100+int(1000*350/940))).resize((940,350))
    m=Image.new('L',ph.size,0);ImageDraw.Draw(m).rounded_rectangle((0,0,939,349),30,fill=255)
    c.paste(ph,(70,840),m)
    L.foot(c,2);c.convert('RGB').save(out,quality=92)

def solucao(out):
    c=grad((22,104,240),(124,58,237));d=ImageDraw.Draw(c)
    stamp(c,TAG,70,200,YEL,INK,24)
    y=280;fo=f('Black',80)
    for l in ['COM O AGENT-HUB,','TODO MUNDO É','RESPONDIDO NA HORA']: d.text((66,y),l,font=fo,fill='white');y+=90
    y+=50
    for t in ['Manda o cardápio e a promoção da Black','Informa taxa e tempo de entrega','Anota o pedido completo','Atende dezenas de conversas ao mesmo tempo']:
        d.rounded_rectangle((70,y,W-70,y+104),26,fill=(255,255,255))
        d.ellipse((96,y+27,146,y+77),fill=YEL);d.text((109,y+30),'✓',font=f('Black',34),fill=INK)
        d.text((172,y+30),t,font=f('SemiBold',36),fill=INK);y+=122
    L.foot(c,3,dark=True);c.convert('RGB').save(out,quality=92)

def cta(out):
    c=Image.new('RGBA',(W,H),YEL);d=ImageDraw.Draw(c,'RGBA')
    for r in (300,370,440): d.ellipse((1150-r,1350-r,1150+r,1350+r),outline=INK,width=3)
    stamp(c,TAG,70,200,INK,'white',24)
    y=290;fo=f('Black',96)
    for l in ['SEU WHATSAPP','ESTÁ PRONTO','PARA A BLACK','FRIDAY?']: d.text((66,y),l,font=fo,fill=INK);y+=106
    y+=40;d.text((70,y),'Conheça hoje o Agent-Hub!',font=f('Bold',52),fill=INK);y+=110
    d.rounded_rectangle((70,y,560,y+110),55,fill=INK);fb=f('Bold',44)
    d.text((315-d.textlength('Comente BLACK',font=fb)/2,y+29),'Comente BLACK',font=fb,fill='white')
    L.foot(c,4);c.convert('RGB').save(out,quality=92)

if __name__=='__main__':
    o=sys.argv[1] if len(sys.argv)>1 else 'saida/';os.makedirs(o,exist_ok=True)
    capa(o+'pizzaria_1.jpg');lista(o+'pizzaria_2.jpg');quem(o+'pizzaria_3.jpg');solucao(o+'pizzaria_4.jpg');cta(o+'pizzaria_5.jpg')
