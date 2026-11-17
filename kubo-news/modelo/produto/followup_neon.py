"""Follow Up Solution no padrao original do perfil: foto industrial escura, moldura neon,
titulo branco + ciano no topo, selo do produto e botao 'Peça uma demonstração' embaixo."""
import sys,os
AQUI=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,os.path.join(AQUI,'..'))
exec(open(os.path.join(AQUI,'vivid.py')).read())
from PIL import ImageFilter,ImageEnhance
CY=(0,212,255);NB=(40,120,255);DARK=(4,10,30)

def cover_photo(path,yoff=0,zoom=1.0):
    im=Image.open(path).convert('RGB');r=max(W/im.width,H/im.height)*zoom
    im=im.resize((int(im.width*r)+1,int(im.height*r)+1),Image.LANCZOS)
    x=(im.width-W)//2;im=im.crop((x,0,x+W,H))
    if yoff: bg=Image.new('RGB',(W,H),DARK);bg.paste(im,(0,yoff));im=bg
    im=ImageEnhance.Color(im).enhance(0.85);im=ImageEnhance.Brightness(im).enhance(0.9)
    tint=Image.new('RGB',(W,H),(10,40,110));im=Image.blend(im,tint,0.22)
    return im.convert('RGBA')

def vgrad(top_a,bot_a,y1,y2,col=DARK):
    g=Image.new('RGBA',(W,H),(0,0,0,0));d=ImageDraw.Draw(g)
    for y in range(H):
        if y<y1: a=top_a*(1-y/y1)
        elif y>y2: a=bot_a*((y-y2)/(H-y2))
        else: a=0
        d.line((0,y,W,y),fill=col+(int(a),))
    return g

def glow_rr(c,box,r,col,w=4,blur=14,alpha=230):
    g=Image.new('RGBA',(W,H),(0,0,0,0));ImageDraw.Draw(g).rounded_rectangle(box,r,outline=col+(alpha,),width=w+6)
    c.alpha_composite(g.filter(ImageFilter.GaussianBlur(blur)))
    ImageDraw.Draw(c).rounded_rectangle(box,r,outline=col+(255,),width=w)

def chip(c,x,y,txt,icon):
    d=ImageDraw.Draw(c,'RGBA');fo=f('SemiBold',30);w=d.textlength(txt,font=fo)+110
    box=(x,y,x+w,y+70);d.rounded_rectangle(box,18,fill=(8,20,60,200));glow_rr(c,box,18,NB,3,10)
    d=ImageDraw.Draw(c);ix,iy=x+24,y+19
    if icon=='doc': d.rounded_rectangle((ix,iy,ix+26,iy+32),4,outline='white',width=3);[d.line((ix+6,iy+9+k*7,ix+20,iy+9+k*7),fill='white',width=2) for k in range(3)]
    if icon=='cal': d.rounded_rectangle((ix,iy+3,ix+32,iy+32),4,outline='white',width=3);d.line((ix,iy+12,ix+32,iy+12),fill='white',width=3)
    if icon=='cam': d.rounded_rectangle((ix,iy+6,ix+34,iy+30),5,outline='white',width=3);d.ellipse((ix+10,iy+11,ix+24,iy+25),outline='white',width=3)
    if icon=='bar': [d.rectangle((ix+k*9,iy+30-k*8-6,ix+k*9+5,iy+30),fill='white') for k in range(4)]
    if icon=='bell': d.pieslice((ix+2,iy+2,ix+30,iy+40),180,360,fill='white');d.rectangle((ix+2,iy+20,ix+30,iy+26),fill='white')
    d.text((x+74,y+15),txt,font=fo,fill='white')

def alerta(c,x,y,t1,t2):
    d=ImageDraw.Draw(c,'RGBA');box=(x,y,x+560,y+130);d.rounded_rectangle(box,24,fill=(20,10,10,215));glow_rr(c,box,24,(255,170,0),3,12)
    d=ImageDraw.Draw(c);d.ellipse((x+28,y+33,x+92,y+97),fill=(255,170,0));d.text((x+50,y+36),'!',font=f('Black',46),fill=DARK)
    d.text((x+118,y+28),t1,font=f('Bold',32),fill='white');d.text((x+118,y+72),t2,font=f('SemiBold',28),fill=(255,200,120))

def selo(c,y=1040):
    d=ImageDraw.Draw(c,'RGBA');box=(70,y,W-70,y+130);d.rounded_rectangle(box,30,fill=(6,14,45,215));glow_rr(c,box,30,CY,3,14)
    c.alpha_composite(K.CUBE.resize((80,86)),(105,y+22));d=ImageDraw.Draw(c)
    d.line((215,y+30,215,y+100),fill=(180,220,255),width=3)
    fo=f('Black',58);d.text((245,y+14),'Follow Up ',font=fo,fill='white')
    d.text((245+d.textlength('Follow Up ',font=fo),y+14),'Solution',font=fo,fill=CY)
    d.text((247,y+80),'by Kubo AI',font=f('Bold',30),fill='white')
    yb=y+160;fb=f('Black',30);t='PEÇA UMA DEMONSTRAÇÃO';bw=d.textlength(t,font=fb)+110
    box=(70,yb,70+bw,yb+76);ImageDraw.Draw(c,'RGBA').rounded_rectangle(box,38,fill=(20,60,200,230));glow_rr(c,box,38,NB,3,12)
    d=ImageDraw.Draw(c);d.text((104,yb+21),t,font=fb,fill='white')
    ax=70+bw-52;d.line((ax-14,yb+38,ax+12,yb+38),fill='white',width=4);d.line((ax+2,yb+28,ax+13,yb+38),fill='white',width=4);d.line((ax+2,yb+48,ax+13,yb+38),fill='white',width=4)
    sx=70+bw+40;d.line((sx,yb+10,sx,yb+66),fill=(160,190,230),width=2)
    gx=sx+30;d.ellipse((gx,yb+22,gx+32,yb+54),outline='white',width=3);d.line((gx+16,yb+22,gx+16,yb+54),fill='white',width=2);d.line((gx,yb+38,gx+32,yb+38),fill='white',width=2)
    d.text((gx+46,yb+20),'kuboai.com.br',font=f('SemiBold',30),fill='white')

def arte(foto,l1,l2,sub,out,chips=None,alert=None,yoff=0):
    c=cover_photo(foto,yoff);c.alpha_composite(vgrad(245,250,470,820))
    glow_rr(c,(22,22,W-22,H-22),40,NB,3,18,200)
    d=ImageDraw.Draw(c);fo=f('Black',80);y=78
    for l in l1: d.text((60,y),l,font=fo,fill='white');y+=88
    for l in l2: d.text((60,y),l,font=fo,fill=CY);y+=88
    para(d,62,y+14,sub,f('SemiBold',34),(225,235,255),900,1.3)
    if chips:
        yy=440
        for k,(t,ic) in enumerate(chips): chip(c,W-70-(len(t)*17+110)-k*0,yy,t,ic);yy+=95
    if alert: alerta(c,W-70-560,800,*alert)
    selo(c);c.convert('RGB').save(out,quality=93)

if __name__=='__main__':
    PX=sys.argv[1] if len(sys.argv)>1 else '/home/claude/fus_px'
    o=os.path.join(AQUI,'..','..','saida','followup_neon')+'/';os.makedirs(o,exist_ok=True)
    arte(f'{PX}/32845694.jpg',['Quanto custa cobrar'],['um fornecedor?'],'Ligações, visitas e planilhas também entram na conta',o+'custo.jpg',yoff=250,
         chips=[('Prazos','cal'),('Evolução','bar'),('Fotos','cam'),('Alertas','bell')])
    arte(f'{PX}/29988955.jpg',['O projeto atrasou'],['e ninguém avisou?'],'Com o Follow Up Solution, o alerta chega antes do prazo',o+'projeto.jpg',
         alert=('Pintura industrial','Etapa 2 com 3 dias de atraso'))
