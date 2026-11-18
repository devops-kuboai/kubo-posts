"""Follow Up Solution, padrao neon original: gestor com tablet e o painel do sistema
'projetado' saindo da tela, com o que a ferramenta faz escrito de forma direta."""
import sys,os
AQUI=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,AQUI)
_src=open(os.path.join(AQUI,'followup_neon.py')).read();exec(_src[:_src.index("if __name__")])
RED=(255,80,80);GRN=(40,220,130)

def place_photo(path,cx_frac,scale,yoff):
    im=Image.open(path).convert('RGB');r=H*scale/im.height
    im=im.resize((int(im.width*r),int(im.height*r)),Image.LANCZOS)
    x=int(im.width*cx_frac-W/2);x=max(0,min(im.width-W,x))
    bg=Image.new('RGB',(W,H),DARK);bg.paste(im.crop((x,0,x+W,min(im.height,H-yoff))),(0,yoff))
    bg=ImageEnhance.Color(bg).enhance(0.85);bg=Image.blend(bg,Image.new('RGB',(W,H),(10,40,110)),0.22)
    return bg.convert('RGBA')

def painel(w,linhas):
    h=110+len(linhas)*122
    im=Image.new('RGBA',(w+80,h+80),(0,0,0,0))
    g=Image.new('RGBA',im.size,(0,0,0,0));ImageDraw.Draw(g).rounded_rectangle((40,40,w+40,h+40),28,outline=CY+(255,),width=12)
    im.alpha_composite(g.filter(ImageFilter.GaussianBlur(16)))
    d=ImageDraw.Draw(im,'RGBA');d.rounded_rectangle((40,40,w+40,h+40),28,fill=(6,16,48,236),outline=CY+(255,),width=3)
    x0,y0=40,40;im.alpha_composite(K.CUBE.resize((40,43)),(x0+28,y0+26))
    fo=f('Black',32);d.text((x0+82,y0+26),'Follow Up ',font=fo,fill='white')
    d.text((x0+82+d.textlength('Follow Up ',font=fo),y0+26),'Solution',font=fo,fill=CY)
    d.line((x0+24,y0+92,x0+w-24,y0+92),fill=(60,90,160),width=2)
    y=y0+112
    for nome,pct,st,col,info in linhas:
        d.text((x0+28,y),nome,font=f('Bold',27),fill='white')
        fo=f('Bold',21);tw=d.textlength(st,font=fo)
        d.rounded_rectangle((x0+w-28-tw-28,y-2,x0+w-28,y+32),16,fill=col)
        d.text((x0+w-28-tw-14,y+3),st,font=fo,fill=DARK)
        d.rounded_rectangle((x0+28,y+46,x0+w-28,y+58),6,fill=(40,60,110))
        d.rounded_rectangle((x0+28,y+46,x0+28+int((w-56)*pct),y+58),6,fill=col)
        d.text((x0+28,y+70),info,font=f('Medium',21),fill=(170,195,235))
        y+=122
    return im

LIN=[('Usinagem de eixos',0.75,'75%',CY,'Nova previsão: 28/11  ·  4 fotos'),
     ('Pintura industrial',0.40,'Atrasado',RED,'3 dias de atraso  ·  alerta enviado ao gestor'),
     ('Montagem elétrica',1.0,'Concluído',GRN,'Entregue no prazo  ·  6 fotos')]

def feixe(c,src,box):
    g=Image.new('RGBA',(W,H),(0,0,0,0));d=ImageDraw.Draw(g);x1,y1,x2,y2=box
    d.polygon([src,(x1,y1+30),(x1,y2),(x2,y2)],fill=CY+(34,))
    c.alpha_composite(g.filter(ImageFilter.GaussianBlur(8)))

def faixa(c,y,itens):
    d=ImageDraw.Draw(c,'RGBA');box=(70,y,W-70,y+150);d.rounded_rectangle(box,26,fill=(4,12,40,228));glow_rr(c,box,26,NB,3,12)
    d=ImageDraw.Draw(c);cw=(W-140)/len(itens)
    for k,(a,b) in enumerate(itens):
        x=70+k*cw
        if k: d.line((x,y+28,x,y+122),fill=(70,100,170),width=2)
        d.text((x+26,y+26),a,font=f('Black',30),fill=CY)
        for j,l in enumerate(wrap(d,b,f('SemiBold',23),cw-46)): d.text((x+26,y+70+j*29),l,font=f('SemiBold',23),fill='white')

def arte2(foto,cx,scale,yoff,l1,l2,itens,out,pxy,txy,pw=500):
    c=place_photo(foto,cx,scale,yoff);c.alpha_composite(vgrad(250,250,300,900))
    glow_rr(c,(22,22,W-22,H-22),40,NB,3,18,200)
    d=ImageDraw.Draw(c);fo=f('Black',72);y=70
    for l in l1: d.text((58,y),l,font=fo,fill='white');y+=80
    for l in l2: d.text((58,y),l,font=fo,fill=CY);y+=80
    p=painel(pw,LIN);px,py=pxy
    feixe(c,txy,(px+40,py+40,px+40+pw,py+p.height-40));c.alpha_composite(p,(px,py))
    faixa(c,870,itens);selo(c);c.convert('RGB').save(out,quality=93)

if __name__=='__main__':
    PX=sys.argv[1] if len(sys.argv)>1 else '/home/claude/fus_px'
    o='/home/claude/kubo-posts/saida/followup_tablet/';os.makedirs(o,exist_ok=True)
    F=[('Atualiza','O fornecedor informa a evolução pelo link'),('Comprova','Fotos e nova previsão de entrega'),('Avisa','Alerta de atraso antes do prazo')]
    arte2(f'{PX}/32845694.jpg',0.43,0.85,120,['Acompanhe fornecedores'],['sem precisar cobrar'],F,o+'custo.jpg',(570,250),(250,690),pw=440)
    arte2(f'{PX}/32845694.jpg',0.43,0.85,120,['O projeto atrasou'],['e ninguém avisou?'],F,o+'projeto.jpg',(570,250),(250,690),pw=440)
