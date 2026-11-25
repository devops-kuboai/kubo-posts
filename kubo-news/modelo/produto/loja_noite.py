"""Agent-Hub (25/11): história "Black Friday, 23h40". Carrossel com foto (gerada no Lovable)."""
import sys,os
PROD=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,os.path.join(PROD,'..'))
from kubodark import *
from PIL import ImageFilter,ImageEnhance
INK=(10,14,30);BLUE=(22,104,240);VIO=(124,58,237);YEL=(255,214,10);GR=(84,100,132);BG=(246,247,251)
src=open(os.path.join(PROD,'vivid.py')).read();exec(src[src.index('def grad'):src.index('def foot')])
FOTO=os.environ.get('FOTO','/tmp/fotos/loja_noite.jpg')
N=5
def foot(c,i,dark=False):
    d=ImageDraw.Draw(c);c.alpha_composite(K.CUBE.resize((58,62)),(70,H-122))
    d.text((142,H-114),'KUBO AI',font=f('Bold',32),fill='white' if dark else INK)
    d.text((142,H-78),'@_kuboai',font=f('Medium',23),fill=(220,228,255) if dark else GR)
    for k in range(N):
        cx=W-90-(N-1-k)*26
        on=(YEL if dark else BLUE);off=(255,255,255,90) if dark else (205,210,228)
        d.ellipse((cx-6,H-100,cx+6,H-88),fill=on if k==i else off)
def hl(d,x,y,txt,fo,fill,bg):
    w=d.textlength(txt,font=fo);b=d.textbbox((x,y),txt,font=fo)
    d.rectangle((x-12,b[1]-8,x+w+12,b[3]+10),fill=bg);d.text((x,y),txt,font=fo,fill=fill)
def bubble(c,x,y,txt,hora,mine=False,maxw=640,size=36):
    d=ImageDraw.Draw(c);fo=f('Medium',size);ls=wrap(d,txt,fo,maxw)
    tw=max(d.textlength(l,font=fo) for l in ls);bw=int(max(tw,180))+60;bh=len(ls)*int(size*1.32)+70
    if mine: x=W-70-bw
    col=(220,248,198) if mine else (255,255,255)
    sh=Image.new('RGBA',(W,H));ImageDraw.Draw(sh).rounded_rectangle((x,y+6,x+bw,y+bh+6),28,fill=(0,0,40,28));c.alpha_composite(sh.filter(ImageFilter.GaussianBlur(8)))
    d=ImageDraw.Draw(c);d.rounded_rectangle((x,y,x+bw,y+bh),28,fill=col)
    yy=y+22
    for l in ls: d.text((x+30,yy),l,font=fo,fill=INK);yy+=int(size*1.32)
    fh=f('Medium',22);d.text((x+bw-30-d.textlength(hora,font=fh),y+bh-38),hora,font=fh,fill=(110,120,140))
    return y+bh+22

def capa(out):
    c=Image.new('RGBA',(W,H),(255,255,255))
    ph=Image.open(FOTO).convert('RGB');ph=ImageEnhance.Brightness(ph).enhance(1.12)
    s=W/ (ph.width*0.80);ph=ph.crop((int(ph.width*0.20),0,ph.width,ph.height)).resize((W,int(ph.height*s)))
    ph=ph.crop((0,0,W,760));c.paste(ph,(0,0))
    d=ImageDraw.Draw(c,'RGBA')
    fi=f('SemiBold',20);t='Imagem ilustrativa';w=d.textlength(t,font=fi)
    d.rounded_rectangle((W-70-w-28,700,W-70,736),18,fill=(0,0,0,120));d.text((W-70-w-14,706),t,font=fi,fill='white')
    stamp(c,'AGENT-HUB · BLACK FRIDAY',70,800,INK,'white',24)
    d=ImageDraw.Draw(c);fo=f('Black',82);y=880
    d.text((66,y),'BLACK FRIDAY, 23H40',font=fo,fill=INK);y+=100
    hl(d,70,y,'A loja fechou às 18h',f('Black',54),INK,YEL);y+=86
    d.text((70,y),'Os clientes não pararam',font=f('Bold',54),fill=INK)
    foot(c,0);c.convert('RGB').save(out,quality=92)

def mensagens(out):
    c=Image.new('RGBA',(W,H),BG);d=ImageDraw.Draw(c)
    stamp(c,'AGENT-HUB · BLACK FRIDAY',70,200,INK,'white',24)
    y=270;fo=f('Black',80)
    d.text((66,y),'37 MENSAGENS',font=fo,fill=INK);y+=90
    d.text((66,y),'SEM RESPOSTA',font=fo,fill=INK);y+=120
    for t,h in [('Oi! Ainda tem o vestido floral no M?','21:12'),('Qual o frete para Curitiba?','21:47'),('O desconto da Black vale até que horas?','22:30'),('Vocês parcelam em quantas vezes?','23:05'),('Alguém aí?','23:38')]:
        y=bubble(c,70,y,t,h,maxw=800,size=33)-6
    foot(c,1);c.convert('RGB').save(out,quality=92)

def manha(out):
    c=Image.new('RGBA',(W,H),(255,255,255));d=ImageDraw.Draw(c)
    stamp(c,'AGENT-HUB · BLACK FRIDAY',70,200,INK,'white',24)
    y=300;fo=f('Black',92)
    for l in ['NO SÁBADO,','ELA RESPONDEU','TODO MUNDO']: d.text((66,y),l,font=fo,fill=INK);y+=102
    y+=50
    para(d,70,y,'Mas muita gente já tinha comprado em outra loja, que respondeu primeiro',f('SemiBold',46),INK,900,1.3)
    y=860
    hl(d,70,y,'Não faltou cliente',f('Black',74),INK,YEL);y+=120
    hl(d,70,y,'Faltou resposta',f('Black',74),INK,YEL)
    foot(c,2);c.convert('RGB').save(out,quality=92)

def agenthub(out):
    c=grad((22,104,240),(124,58,237));d=ImageDraw.Draw(c)
    stamp(c,'AGENT-HUB · BLACK FRIDAY',70,200,YEL,INK,24)
    y=270;fo=f('Black',76)
    for l in ['A MESMA NOITE,','COM O AGENT-HUB']: d.text((66,y),l,font=fo,fill='white');y+=88
    y+=40
    y=bubble(c,70,y,'O desconto da Black vale até que horas?','23:38',maxw=760,size=34)
    y=bubble(c,0,y,'Oi! Vale até domingo, 23h59. E o vestido floral no M ainda tem 2 unidades. Quer que eu separe um para você?','23:38',mine=True,maxw=640,size=34)
    y=bubble(c,70,y,'Quero! Pode separar','23:39',size=34)
    y+=10;para(d,70,y,'Resposta na hora, com as informações da sua loja',f('Bold',38),'white',960,1.3)
    foot(c,3,dark=True);c.convert('RGB').save(out,quality=92)

def cta(out):
    c=Image.new('RGBA',(W,H),YEL);d=ImageDraw.Draw(c,'RGBA')
    for r in (300,370,440): d.ellipse((1150-r,1350-r,1150+r,1350+r),outline=INK,width=3)
    stamp(c,'AGENT-HUB · BLACK FRIDAY',70,200,INK,'white',24)
    y=290;fo=f('Black',96)
    for l in ['SUA LOJA VAI','ESTAR ACORDADA','NA BLACK','FRIDAY?']: d.text((66,y),l,font=fo,fill=INK);y+=106
    y+=50;d.rounded_rectangle((70,y,560,y+110),55,fill=INK);fb=f('Bold',44)
    d.text((315-d.textlength('Comente BLACK',font=fb)/2,y+29),'Comente BLACK',font=fb,fill='white')
    para(d,70,y+140,'e veja o Agent-Hub funcionando no Direct',f('SemiBold',36),INK,700,1.3)
    foot(c,4);c.convert('RGB').save(out,quality=92)

if __name__=='__main__':
    o=sys.argv[1] if len(sys.argv)>1 else 'saida/';os.makedirs(o,exist_ok=True)
    capa(o+'noite_1.jpg');mensagens(o+'noite_2.jpg');manha(o+'noite_3.jpg');agenthub(o+'noite_4.jpg');cta(o+'noite_5.jpg')
