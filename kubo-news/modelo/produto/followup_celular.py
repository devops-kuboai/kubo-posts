"""Follow Up Solution: o lado do fornecedor. Ele atualiza pelo celular e o gestor ve na hora."""
import sys,os
AQUI=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,AQUI)
_src=open(os.path.join(AQUI,'followup_tablet.py')).read();exec(_src[:_src.rindex("if __name__")])
LIN2=[('Usinagem de eixos',0.75,'75%',CY,'Atualizado agora  ·  4 fotos'),
      ('Pintura industrial',0.60,'60%',CY,'Nova previsão: 02/12'),
      ('Montagem elétrica',1.0,'Concluído',GRN,'Entregue no prazo  ·  6 fotos')]
def feixe2(c,src,box):
    g=Image.new('RGBA',(W,H),(0,0,0,0));d=ImageDraw.Draw(g);x1,y1,x2,y2=box
    d.polygon([src,(x2,y1+40),(x2,y2-30)],fill=CY+(60,))
    c.alpha_composite(g.filter(ImageFilter.GaussianBlur(8)))
    sx,sy=src;g=Image.new('RGBA',(W,H),(0,0,0,0));ImageDraw.Draw(g).ellipse((sx-62,sy-62,sx+62,sy+62),outline=CY+(255,),width=6)
    c.alpha_composite(g.filter(ImageFilter.GaussianBlur(6)));ImageDraw.Draw(c,'RGBA').ellipse((sx-62,sy-62,sx+62,sy+62),outline=CY+(230,),width=3)
def arte3(foto,cx,scale,yoff,l1,l2,itens,out,pxy,src,pw=440):
    c=place_photo(foto,cx,scale,yoff);c.alpha_composite(vgrad(250,250,300,900))
    glow_rr(c,(22,22,W-22,H-22),40,NB,3,18,200)
    d=ImageDraw.Draw(c);fo=f('Black',70);y=70
    for l in l1: d.text((58,y),l,font=fo,fill='white');y+=80
    for l in l2: d.text((58,y),l,font=fo,fill=CY);y+=80
    p=painel(pw,LIN2);px,py=pxy
    feixe2(c,src,(px+40,py+40,px+40+pw,py+p.height-40));c.alpha_composite(p,(px,py))
    faixa(c,870,itens);selo(c);c.convert('RGB').save(out,quality=93)
if __name__=='__main__':
    PX='/home/claude/fus_px';o='/home/claude/kubo-posts/saida/followup_celular/';os.makedirs(o,exist_ok=True)
    F=[('Sem app','O fornecedor só abre o link no celular'),('Com fotos','Mostra a peça e a nova previsão'),('Na hora','Você vê no painel e recebe alerta')]
    cx=float(sys.argv[1]) if len(sys.argv)>1 else 0.67
    sx=int(sys.argv[2]) if len(sys.argv)>2 else 783; sy=int(sys.argv[3]) if len(sys.argv)>3 else 694
    arte3(f'{PX}/8986141.jpg',cx,0.85,120,['Seu fornecedor atualiza'],['e você vê na hora'],F,o+'celular.jpg',(20,250),(sx,sy))
