"""Reel animado (25/11): Black Friday na pizzaria. Mesmo conteúdo do carrossel pizzaria_bf.py.
Uso: python3 reel_pizzaria.py <pasta_saida>  -> gera cenas .mp4, junta e põe trilha."""
import sys,os,subprocess,shutil
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import loja_noite as L
from loja_noite import *
import pizzaria_bf as P
FPS=30;TAG=P.TAG;FOTO=P.FOTO;GREEN=P.GREEN
def layer(fn):
    im=Image.new('RGBA',(W,H),(0,0,0,0));fn(im,ImageDraw.Draw(im));return im
def ease(x): x=max(0,min(1,x));return 1-(1-x)**3
def comp(base,layers,t):
    fr=base.copy()
    for im,t0 in layers:
        p=ease((t-t0)/0.35)
        if p<=0: continue
        if p<1:
            a=im.copy();a.putalpha(a.getchannel('A').point(lambda v:int(v*p)))
            fr.alpha_composite(a,(0,int(36*(1-p))))
        else: fr.alpha_composite(im)
    return fr
def foot(i,dark=False):
    L.N=0;c=Image.new('RGBA',(W,H),(0,0,0,0));L.foot(c,i,dark);return c
def render(name,dur,frame_fn,out):
    tmp=out+name+'.tmp.mp4'
    p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
        '-c:v','libx264','-crf','18','-preset','veryfast','-pix_fmt','yuv420p','-r',str(FPS),tmp],stdin=subprocess.PIPE)
    n=int(round(dur*FPS))
    for k in range(n):
        t=k/FPS;fr=frame_fn(t).convert('RGB')
        fi=min(1,t/0.2)  # entrada rápida a partir do branco
        if fi<1: fr=Image.blend(Image.new('RGB',(W,H),'white'),fr,fi)
        p.stdin.write(fr.tobytes())
    p.stdin.close();assert p.wait()==0;os.replace(tmp,out+name+'.mp4')

# ---------- cena 1: capa ----------
def cena1():
    ph=Image.open(FOTO).convert('RGB');ph=ImageEnhance.Brightness(ph).enhance(1.08)
    x0=int(ph.width*0.20);ph=ph.crop((x0,0,ph.width,ph.height));s=W/ph.width;ph=ph.resize((W,int(ph.height*s)))
    base=Image.new('RGBA',(W,H),(255,255,255));base.alpha_composite(foot(0))
    def badge(im,d):
        fi=f('SemiBold',20);t='Imagem ilustrativa';w=d.textlength(t,font=fi)
        d.rounded_rectangle((W-70-w-28,720,W-70,756),18,fill=(0,0,0,120));d.text((W-70-w-14,726),t,font=fi,fill='white')
    ls=[(layer(lambda im,d:stamp(im,TAG,70,815,INK,'white',24)),0.4),
        (layer(lambda im,d:d.text((66,890),'BLACK FRIDAY NA PIZZARIA',font=f('Black',70),fill=INK)),0.7),
        (layer(lambda im,d:hl(d,70,990,'A promoção bombou',f('Black',56),INK,YEL)),1.5),
        (layer(lambda im,d:d.text((70,1078),'E o WhatsApp também',font=f('Bold',56),fill=INK)),2.3)]
    bd=layer(badge)
    def fr(t):
        z=1+0.07*t/5;pw,phh=int(W*z),int(ph.height*z);im=ph.resize((pw,phh))
        ox=(pw-W)//2;crop=im.crop((ox,0,ox+W,780))
        b=base.copy();b.paste(crop,(0,0));b.alpha_composite(bd);return comp(b,ls,t)
    return fr,5.0

# ---------- cena 2: lista de conversas ----------
def cena2():
    base=Image.new('RGBA',(W,H),BG);d=ImageDraw.Draw(base)
    stamp(base,TAG,70,200,INK,'white',24);d.text((66,270),'SEXTA, 19H30',font=f('Black',84),fill=INK)
    base.alpha_composite(foot(1))
    y=470;card=layer(lambda im,d:d.rounded_rectangle((70,y,W-70,y+735),30,fill=(255,255,255)))
    rows=[('Ana Paula','A promo de 2 grandes vale para entrega?','19:29',3),('Carlos','Quanto tempo para entregar no Centro?','19:28',2),
          ('Marcos','Cadê minha pizza? Pedi faz 1 hora','19:27',4),('Juliana','Aceita Pix?','19:27',1),
          ('Roberto','Me manda o cardápio da Black','19:26',2),('Bia','Oi?? Tem alguém aí?','19:25',5)]
    cols=[(255,159,67),(84,160,255),(238,90,111),(46,204,113),(155,89,182),(241,196,15)]
    ls=[(card,0.15)]
    for i,((n,m,h,k),cl) in enumerate(zip(rows,cols)):
        yy=y+20+i*118
        def draw(im,d,n=n,m=m,h=h,k=k,cl=cl,yy=yy,i=i):
            d.ellipse((100,yy+14,184,yy+98),fill=cl);fi=f('Black',38);d.text((142-d.textlength(n[0],font=fi)/2,yy+32),n[0],font=fi,fill='white')
            d.text((210,yy+14),n,font=f('Bold',34),fill=INK);d.text((210,yy+60),m,font=f('Medium',29),fill=GR)
            fh=f('SemiBold',24);d.text((W-110-d.textlength(h,font=fh),yy+20),h,font=fh,fill=(30,170,80))
            d.ellipse((W-150,yy+58,W-110,yy+98),fill=GREEN);fk=f('Bold',24);d.text((W-130-d.textlength(str(k),font=fk)/2,yy+64),str(k),font=fk,fill='white')
            if i<5: d.line((210,yy+112,W-100,yy+112),fill=(236,238,244),width=2)
        ls.append((layer(draw),0.5+i*0.45))
    def fr(t):
        b=comp(base,ls,t);d=ImageDraw.Draw(b)
        n=int(min(47,47*ease((t-0.4)/3.2)))
        hl(d,70,375,f'{n} conversas esperando resposta',f('Black',44),INK,YEL);return b
    return fr,5.5

# ---------- cena 3: quem responde ----------
def cena3():
    base=Image.new('RGBA',(W,H),(255,255,255));stamp(base,TAG,70,200,INK,'white',24);base.alpha_composite(foot(2))
    ph=Image.open(FOTO).convert('RGB');ph=ImageEnhance.Brightness(ph).enhance(1.1)
    ph=ph.crop((0,100,1000,100+int(1000*350/940))).resize((940,350))
    m=Image.new('L',ph.size,0);ImageDraw.Draw(m).rounded_rectangle((0,0,939,349),30,fill=255)
    phl=Image.new('RGBA',(W,H),(0,0,0,0));phl.paste(ph,(70,840),m)
    ls=[(layer(lambda im,d:d.text((66,270),'E QUEM RESPONDE?',font=f('Black',88),fill=INK)),0.15)]
    for i,t in enumerate(['O pizzaiolo está no forno','O atendente está no balcão','O motoboy espera o próximo pedido']):
        y=410+i*64
        ls.append((layer(lambda im,d,t=t,y=y:(d.ellipse((74,y+12,100,y+38),fill=YEL),d.text((124,y),t,font=f('SemiBold',40),fill=INK))),0.7+i*0.5))
    ls+=[(phl,0.5),(layer(lambda im,d:hl(d,70,654,'Cada mensagem sem resposta',f('Black',54),INK,YEL)),2.5),
         (layer(lambda im,d:hl(d,70,740,'é um pedido que esfria',f('Black',54),INK,YEL)),3.0)]
    return (lambda t:comp(base,ls,t)),5.0

# ---------- cena 4: solução ----------
def cena4():
    base=grad((22,104,240),(124,58,237));stamp(base,TAG,70,200,YEL,INK,24);base.alpha_composite(foot(3,True))
    ls=[]
    for i,l in enumerate(['COM O AGENT-HUB,','TODO MUNDO É','RESPONDIDO NA HORA']):
        ls.append((layer(lambda im,d,l=l,i=i:d.text((66,280+i*90),l,font=f('Black',80),fill='white')),0.15+i*0.25))
    y=600
    for i,t in enumerate(['Manda o cardápio e a promoção da Black','Informa taxa e tempo de entrega','Anota o pedido completo','Atende dezenas de conversas ao mesmo tempo']):
        yy=y+i*122
        def dr(im,d,t=t,yy=yy):
            d.rounded_rectangle((70,yy,W-70,yy+104),26,fill=(255,255,255));d.ellipse((96,yy+27,146,yy+77),fill=YEL)
            d.text((109,yy+30),'✓',font=f('Black',34),fill=INK);d.text((172,yy+30),t,font=f('SemiBold',36),fill=INK)
        ls.append((layer(dr),1.1+i*0.5))
    return (lambda t:comp(base,ls,t)),5.5

# ---------- cena 5: CTA ----------
def cena5():
    base=Image.new('RGBA',(W,H),YEL);d=ImageDraw.Draw(base)
    for r in (300,370,440): d.ellipse((1150-r,1350-r,1150+r,1350+r),outline=INK,width=3)
    stamp(base,TAG,70,200,INK,'white',24);base.alpha_composite(foot(4))
    ls=[(layer(lambda im,d,l=l,i=i:d.text((66,290+i*106),l,font=f('Black',96),fill=INK)),0.15+i*0.25) for i,l in enumerate(['SEU WHATSAPP','ESTÁ PRONTO','PARA A BLACK','FRIDAY?'])]
    ls.append((layer(lambda im,d:d.text((70,754),'Conheça hoje o Agent-Hub!',font=f('Bold',52),fill=INK)),1.5))
    by=919
    def fr(t):
        b=comp(base,ls,t);p=ease((t-2.0)/0.35)
        if p>0:
            s=1+0.04*max(0,np.sin((t-2.4)*2*np.pi/1.2))*(t>2.4)
            btn=Image.new('RGBA',(int(490*s),int(110*s)),(0,0,0,0));dd=ImageDraw.Draw(btn)
            dd.rounded_rectangle((0,0,btn.width-1,btn.height-1),btn.height//2,fill=INK);fb=f('Bold',int(44*s))
            tw=dd.textlength('Comente BLACK',font=fb);dd.text(((btn.width-tw)/2,btn.height/2-fb.size*0.62),'Comente BLACK',font=fb,fill='white')
            if p<1: btn.putalpha(btn.getchannel('A').point(lambda v:int(v*p)))
            b.alpha_composite(btn,(int(315-btn.width/2),int(by-btn.height/2+36*(1-p))))
        return b
    return fr,4.5

if __name__=='__main__':
    o=sys.argv[1] if len(sys.argv)>1 else 'saida_reel/';os.makedirs(o,exist_ok=True)
    so=sys.argv[2:] or ['1','2','3','4','5']
    cenas={'1':cena1,'2':cena2,'3':cena3,'4':cena4,'5':cena5}
    if so==['frames']:
        for k,(fn,du) in [(k,v()) for k,v in cenas.items()]: fn(du-0.01).convert('RGB').save(f'{o}frame_{k}.jpg',quality=85)
        sys.exit()
    for k in so:
        fn,du=cenas[k]();du=float(os.environ.get('DUR'+k,du));render(f'cena{k}',du,fn,o);print('cena',k,du)
