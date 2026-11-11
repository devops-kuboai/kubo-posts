# Estilo escuro para posts de produto (Agent-Hub / Follow Up)
import kubonews as K
from kubonews import *
from PIL import ImageFilter
NV=(6,14,38);WH=(255,255,255);SKY=(92,170,255);MUT=(165,182,215)
def dbg():
    y,x=np.mgrid[0:H,0:W]
    r=np.hypot(x-W*0.9,y-H*0.05)/1300
    g=np.dstack([6+26*np.exp(-r*3),14+44*np.exp(-r*3),38+120*np.exp(-r*2.4)])
    r2=np.hypot(x-W*0.0,y-H*1.0)/900
    g+=np.dstack([8*np.exp(-r2*3),20*np.exp(-r2*3),55*np.exp(-r2*3)])
    img=Image.fromarray(np.clip(g,0,255).astype(np.uint8)).convert('RGBA');d=ImageDraw.Draw(img,'RGBA')
    for gx in range(0,W,90): d.line((gx,0,gx,H),fill=(90,150,255,16))
    for gy in range(0,H,90): d.line((0,gy,W,gy),fill=(90,150,255,16))
    a=Image.new('RGBA',(W,H));ad=ImageDraw.Draw(a)
    ad.ellipse((W-420,-520,W+900,800),outline=(50,130,255,230),width=5)
    img.alpha_composite(a.filter(ImageFilter.GaussianBlur(14)));img.alpha_composite(a)
    return img
def dpill(img,t,x=70,y=110):
    d=ImageDraw.Draw(img);fo=f('Bold',24);sp=5
    tw=sum(d.textlength(c,font=fo)+sp for c in t)-sp
    d.rounded_rectangle((x,y,x+tw+56,y+54),27,fill=(10,28,70),outline=(61,160,255),width=2)
    cx=x+28
    for c in t: d.text((cx,y+13),c,font=fo,fill=SKY);cx+=d.textlength(c,font=fo)+sp
def dfooter(img,i,n):
    d=ImageDraw.Draw(img)
    d.line((70,H-150,W-70,H-150),fill=(40,60,110),width=2)
    img.alpha_composite(K.CUBE.resize((58,62)),(70,H-122))
    d.text((142,H-114),'KUBO',font=f('Bold',32),fill=WH);d.text((142+d.textlength('KUBO ',font=f('Bold',32)),H-114),'AI',font=f('Bold',32),fill=SKY)
    d.text((142,H-78),'@_kuboai',font=f('Medium',23),fill=MUT)
    for k in range(n):
        cx=W-90-(n-1-k)*26;d.ellipse((cx-6,H-100,cx+6,H-88),fill=SKY if k==i else (50,70,120))
    if i<n-1:
        fo=f('SemiBold',26);d.text((W-90-(n-1)*26-28-d.textlength('Arraste',font=fo),H-109),'Arraste',font=fo,fill=MUT)
def dcover(tag,visual,t1,t2,sub,out,n=4):
    img=dbg();dpill(img,tag)
    v=visual.convert('RGBA');v.thumbnail((940,600))
    sh=Image.new('RGBA',(W,H));ImageDraw.Draw(sh).rounded_rectangle(((W-v.width)//2,215,(W+v.width)//2,215+v.height),30,fill=(0,0,0,150))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(25)))
    m=Image.new('L',v.size,0);ImageDraw.Draw(m).rounded_rectangle((0,0,v.width,v.height),30,fill=255)
    img.paste(v,((W-v.width)//2,200),m)
    d=ImageDraw.Draw(img);y=200+v.height+60
    for l in wrap(d,t1,f('Black',80),940): d.text((70,y),l,font=f('Black',80),fill=WH);y+=92
    for l in wrap(d,t2,f('Black',80),940): d.text((70,y),l,font=f('Black',80),fill=SKY);y+=92
    para(d,70,y+14,sub,f('Medium',34),MUT,930,1.38)
    dfooter(img,0,n);img.convert('RGB').save(out,quality=92)
def dbody(tag,kicker,head,items,out,i,n=4):
    img=dbg();dpill(img,tag);d=ImageDraw.Draw(img)
    y=230;d.text((70,y),kicker,font=f('Bold',28),fill=SKY);y+=58
    for l in wrap(d,head,f('Black',72),940): d.text((70,y),l,font=f('Black',72),fill=WH);y+=84
    y+=50
    for k,it in enumerate(items,1):
        d.ellipse((70,y+2,124,y+56),fill=(22,104,240));t=str(k);fo=f('Bold',30);d.text((97-d.textlength(t,font=fo)/2,y+10),t,font=fo,fill='white')
        y=max(para(d,150,y+4,it,f('Medium',40),WH,860,1.34),y+60)+38
    dfooter(img,i,n);img.convert('RGB').save(out,quality=92)
def dcta(tag,head,sub,botao,out,n=4):
    img=dbg();dpill(img,tag);d=ImageDraw.Draw(img);y=300
    for l in wrap(d,head,f('Black',84),940): d.text((70,y),l,font=f('Black',84),fill=WH);y+=96
    y=para(d,70,y+20,sub,f('Medium',40),MUT,930,1.36)+60
    fo=f('Bold',40);tw=d.textlength(botao,font=fo)
    d.rounded_rectangle((70,y,70+tw+90,y+96),48,fill=(22,104,240));d.text((115,y+24),botao,font=fo,fill='white')
    dfooter(img,n-1,n);img.convert('RGB').save(out,quality=92)
