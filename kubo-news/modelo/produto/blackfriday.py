import sys,os
AQUI=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,os.path.join(AQUI,'..'))
from kubodark import *
from PIL import ImageFilter
INK=(10,14,30);BLUE=(22,104,240);YEL=(255,214,10)
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'vivid.py')).read();exec(src[src.index('def grad'):])

def celular(msgs):
    S=2;w,h=1536*S,1024*S
    im=Image.new('RGBA',(w,h),(0,0,0,0));d=ImageDraw.Draw(im)
    px,py,pw,ph=w//2-520,170,1040,2000
    d.rounded_rectangle((px,py,px+pw,py+ph),110,fill=(18,24,40),outline=(70,80,110),width=10)
    sx,sy=px+40,py+40;d.rounded_rectangle((sx,sy,px+pw-40,py+ph-40),80,fill=(240,244,250))
    d.rounded_rectangle((sx,sy,px+pw-40,sy+200),80,fill=BLUE);d.rectangle((sx,sy+120,px+pw-40,sy+200),fill=BLUE)
    d.ellipse((sx+50,sy+50,sx+150,sy+150),fill='white');d.text((sx+82,sy+66),'L',font=f('Black',60),fill=BLUE)
    d.text((sx+180,sy+52),'Sua loja',font=f('Bold',56),fill='white');d.text((sx+180,sy+118),'responde em segundos',font=f('Medium',36),fill=(220,232,255))
    def bub(y0,txt,me,t):
        fo=f('Medium',46);lines=wrap(d,txt,fo,640);bh=len(lines)*62+70;bw=max(d.textlength(l,font=fo) for l in lines)+80
        x1=sx+40 if not me else px+pw-80-bw
        d.rounded_rectangle((x1,y0,x1+bw,y0+bh),40,fill=BLUE if me else 'white')
        yy=y0+30
        for l in lines: d.text((x1+40,yy),l,font=fo,fill='white' if me else (12,27,64));yy+=62
        d.text((x1+bw-110,y0+bh+8),t,font=f('Medium',30),fill=(120,130,150));return y0+bh+70
    yy=sy+280
    for txt,me,t in msgs: yy=bub(yy,txt,me,t)
    im=im.resize((1536,1024),Image.LANCZOS).crop((508,85,1029,1024))
    m=Image.new('L',im.size,0);ImageDraw.Draw(m).rounded_rectangle((0,0,im.width-1,im.height+80),55,fill=255)
    a=Image.new('RGBA',im.size);a.paste(im,(0,0),m);return a

ph=celular([('Oi! O desconto da Black Friday vale para o tênis azul?',False,'23:47'),
            ('Vale sim! Ele está com 30% de desconto e frete grátis. Quer que eu reserve o seu número?',True,'23:47'),
            ('Quero! Número 40',False,'23:48')])

def blackfriday(out,phone_y=660):
    c=Image.new('RGBA',(W,H),YEL);d=ImageDraw.Draw(c,'RGBA')
    for r in (440,515,590): d.ellipse((1080-r,1090-r,1080+r,1090+r),outline=INK,width=3)
    stamp(c,'AGENT-HUB · BLACK FRIDAY',70,100,INK,'white')
    fo=f('Black',104);y=205
    for l in ['A BLACK FRIDAY','É DIA 27/11']: d.text((66,y),l,font=fo,fill=INK);y+=114
    y+=30;fo2=f('Black',40);t='Prepare seu atendimento antes do pico';w=d.textlength(t,font=fo2)
    d.rectangle((70,y,70+w+40,y+70),fill=INK);d.text((90,y+12),t,font=fo2,fill='white')
    para(d,70,620,'Veja o Agent-Hub funcionando com as informações do seu negócio',f('Bold',40),INK,400,1.28)
    y=865;d.rounded_rectangle((70,y,500,y+100),50,fill=INK);fb=f('Bold',40)
    d.text((285-d.textlength('Chame no Direct',font=fb)/2,y+27),'Chame no Direct',font=fb,fill='white')
    para(d,70,995,'ou comente BLACK aqui embaixo',f('SemiBold',34),INK,400,1.28)
    pb=ph.resize((int(ph.width*0.78),int(ph.height*0.78)))
    sh=Image.new('RGBA',(W,H));ImageDraw.Draw(sh).rounded_rectangle((620,phone_y+40,620+pb.width,phone_y+40+pb.height),50,fill=(60,40,0,110))
    c.alpha_composite(sh.filter(ImageFilter.GaussianBlur(30)))
    c.alpha_composite(pb.rotate(-5,expand=True,resample=Image.BICUBIC),(590,phone_y))
    d=ImageDraw.Draw(c)
    c.alpha_composite(K.CUBE.resize((58,62)),(70,H-122))
    d.text((142,H-114),'KUBO AI',font=f('Bold',32),fill=INK);d.text((142,H-78),'@_kuboai',font=f('Medium',23),fill=(84,100,132))
    c.convert('RGB').save(out,quality=92)

if __name__=='__main__':
    os.makedirs('saida',exist_ok=True);blackfriday('saida/blackfriday.jpg')
