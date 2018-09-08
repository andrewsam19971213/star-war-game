import pygame
import random
from game.bullet import Bullet
from game.airplane import Airplane
from game.otherairplane import Otherairplane
from game.bombs import Bombs
from game.bossairplane import Bossairplane
from game.supplies import Supplies
from game.ufo import Ufo
from game.light import Light
pygame.init()
pygame.mixer.init()
yellow=(255,242,0)
bright_yellow=(255,255,220)
white=(255,255,255)
red=(200,0,0)
black=(0,0,0)
green=(0,200,0)
bright_green=(0,255,0)
bright_red=(255,0,0)
gameDisplay=pygame.display.set_mode((800,600))
pygame.display.set_caption("Airplane War")
bg=pygame.image.load("D:/python practice/background.png").convert_alpha()
bg_rect=bg.get_rect()
icon=pygame.image.load("D:/python practice/airplane.png").convert_alpha()
pygame.display.set_icon(icon)
supply_sound=pygame.mixer.Sound("C:/Users/acer/Desktop/music/single_bubble (mp3cut.net).wav")
bullet_sound=pygame.mixer.Sound("C:/Users/acer/Desktop/music/rapid_fire_from_small_caliber_pistol (mp3cut.net).wav")
fire_sound=pygame.mixer.Sound("C:/Users/acer/Desktop/music/single_blast_of_propane_burner_from_hot_air_balloon.wav")
other_dead_sound=pygame.mixer.Sound("C:/Users/acer/Desktop/music/plastic_explosion_with_charge (mp3cut.net).wav")
myairplane_dead_sound=pygame.mixer.Sound("C:/Users/acer/Desktop/music/plastic_explosion_with_charge (mp3cut.net).wav")
boss_dead_sound=pygame.mixer.Sound("C:/Users/acer/Desktop/music/four_plastic_explosions_with_charge-_mp3cut.net_.wav")
win_music=pygame.mixer.Sound("C:/Users/acer/Desktop/music/yisell_sound_2014042815100491321_88366.wav")
ufo_music=pygame.mixer.Sound("C:/Users/acer/Desktop/music/bgm_maoudamashii_neorock82-_1_.wav")
gameover_music=pygame.mixer.Sound("C:/Users/acer/Desktop/music/zth070516_aigei_com.wav")
bullet_sound.set_volume(0.5)
fire_sound.set_volume(0.5)
supply_sound.set_volume(0.8)
other_dead_sound.set_volume(0.9)
myairplane_dead_sound.set_volume(0.9)
boss_dead_sound.set_volume(1)
win_music.set_volume(1)
ufo_music.set_volume(0.1)
gameover_music.set_volume(1)
u=Ufo(gameDisplay,"D:/python practice/ufo.png",(143,-700))
l=Light("D:/python practice/light.png",(325,120))
ublist=[]
ubgroup=pygame.sprite.Group()
ub=Bullet("D:/python practice/bulletufo.png",200,116)
ub2=Bullet("D:/python practice/bulletufo.png",320,150)
ub3=Bullet("D:/python practice/bulletufo.png",485,150)
ub5=Bullet("D:/python practice/bulletufo.png",611,116)
ublist=[ub,ub2,ub3,ub5]
for ufobullet in ublist:
    ubgroup.add(ufobullet)
clock=pygame.time.Clock()
def game_over():
    pygame.mixer.music.pause()
    LargeText=pygame.font.SysFont("comicsansms",115)
    Textsurface=LargeText.render("Game Over!",True,white)
    Textrect=Textsurface.get_rect()
    Textrect.center=(400,300)
    over=True
    while over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()    
        gameDisplay.blit(Textsurface,Textrect)
        button("Continue",150,450,100,50,green,bright_green,gameloop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)
def pass_game():
    pygame.mixer.music.pause()
    LargeText=pygame.font.SysFont("comicsansms",115)
    Textsurface=LargeText.render("PASS!",True,white)
    Textrect=Textsurface.get_rect()
    Textrect.center=(400,300)
    over=True
    while over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()    
        gameDisplay.blit(Textsurface,Textrect)
        #button("Continue",150,450,100,50,green,bright_green,gameloop)
        button("Quit",350,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)
def button(msg,x,y,w,h,ic,ac,action=None):
    pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x < mouse[0] < x+w and y < mouse[1] < y+h:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            action()
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
    smallText=pygame.font.SysFont("comicsansms",20)
    textSurface=smallText.render(msg,True,black)
    textRect=textSurface.get_rect()
    textRect.center=(x+w/2,y+h/2)
    gameDisplay.blit(textSurface,textRect)
def game_intro(): #開始選單
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        largetext=pygame.font.SysFont("comicsansms",115)
        TextSurface=largetext.render("Star Wars",True,yellow,black)
        TextRect=TextSurface.get_rect()
        TextRect.center=(400,300)
        gameDisplay.blit(TextSurface,TextRect)
        button("Start",150,450,100,50,green,bright_green,gameloop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)
def quitgame():
    pygame.quit()
    quit()
def ufoappear():
    if u.active: #飛碟存活時
        u.rect[1]+=2
        if u.rect[1] > -74:   #當飛碟的高度大於-74時
            u.rect[1]=-74     #固定
        gameDisplay.blit(u.image,u.rect)
        if u.rect[1]==-74:
            if u.goright:
                u.rect[0]+=1
                ub.rect[0]=u.rect[0]+57
                ub2.rect[0]=u.rect[0]+177
                ub3.rect[0]=u.rect[0]+342
                ub5.rect[0]=u.rect[0]+468
                l.rect[0]=u.rect[0]+182
                if u.rect[0]==278:
                    u.goright=False
                    u.goleft=True
            if u.goleft:
                u.rect[0]-=1
                ub.rect[0]=u.rect[0]+57
                ub2.rect[0]=u.rect[0]+177
                ub3.rect[0]=u.rect[0]+342
                ub5.rect[0]=u.rect[0]+468
                l.rect[0]=u.rect[0]+182
                if u.rect[0] < 0:
                    u.goleft=False
                    u.goright=True
            if l.visible:  #可看見飛碟光束時
                gameDisplay.blit(l.image,l.rect)
                if u.ub_visible==False:
                    u.ub_visible_index+=1
                    if u.ub_visible_index >= 180:  #激光彈發射時間,到了
                        u.ub_visible=True
                        u.start=True
                        u.ub_visible_index=0
            if u.ub_visible:   #看見激光彈時
                for ufob in ubgroup:
                    gameDisplay.blit(ufob.image,ufob.rect)
                    ufob.rect[1]+=ufob.bullet_speed
                    if ufob.rect[1] > 600:
                        ufob.rect[1]=130
            if u.start:  #重新啟動激光彈發射
                u.ub_revisible()
    else:   #飛碟掛載時
        if u.bombhappen:
            ufo_music.stop()
            win_music.play()
            u.draw(u.rect)
            u.action()
        if u.gameover:
            u.reset((143,-700))
            u.appeared=False
            pass_game()
def gameloop():
    x=800*0.5
    y=600*0.8
    n=600*0.8
    delay=120
    index=0
    index1=0
    index2=0
    index3=0
    bg_x=0
    bg_y=0
    bg_x1=0
    bg_y1=-600
    otherairplanes=pygame.sprite.Group()
    imagename="D:/python practice/otherairplane.png"
    x1=random.randint(0,380)
    y1=-80
    o=Otherairplane(imagename,x1,y1,3)  #小敵機
    x2=random.randint(410,775)
    y2=-80
    o1=Otherairplane(imagename,x2,y2,3)
    otherairplanes.add(o)
    otherairplanes.add(o1)
    imagename1="D:/python practice/otherairplane1.png"
    bossname="D:/python practice/bossairplane.png"
    boss=Bossairplane(gameDisplay,bossname,(400,-600),1) #大敵機
    for enemy in range(0,3):
        x3=random.randint(0,775)
        y3=random.randint(-250,-150)
        otherairplanes.add(Otherairplane(imagename1,x3,y3,3))
    bomb=Bombs(gameDisplay,(0,0))  #爆炸
    bomb1=Bombs(gameDisplay,(0,0))
    airplanegroups=pygame.sprite.Group()
    name="D:/python practice/airplane.png"
    name1="D:/python practice/airplane1.png"
    a=Airplane(gameDisplay,name,(x,y),10)   #我方飛機
    a1=Airplane(gameDisplay,name1,(x,y),10)
    airplanegroups.add(a)
    airplanegroups.add(a1)
    filename1="D:/python practice/bullet.png"
    filename2="D:/python practice/firebullet.png"
    bullets=pygame.sprite.Group()
    b=Bullet(filename1,x+25,n)  #子彈物件(我方飛機)
    fire_b=Bullet(filename2,x-25,n)  #火彈(子彈)
    fire_b1=Bullet(filename2,x+41,n)
    bullets.add(fire_b)
    bullets.add(fire_b1)
    b1=Bullet(filename1,400,1)  #子彈(大敵機)
    b2=Bullet(filename1,585,1)
    s=Supplies(filename2)  #補給物(火彈)
    s1=Supplies("D:/python practice/supply.png")  #補給物(補血)
    bullet_group=pygame.sprite.Group()
    bullet_group.add(b1)
    bullet_group.add(b2)
    pygame.mixer.music.load("C:/Users/acer/Desktop/music/reckless_abandon (1).mp3")
    pygame.mixer.music.play(-1)
    UFOEVENT=pygame.USEREVENT+1
    pygame.time.set_timer(UFOEVENT,90000)
    game_start=True
    a.Y_bolen=False
    a.X_bolen=False
    b.btbolen=False
    a_image=True
    a_image1=True
    a_image2=True
    launch=True
    launch1=True
    u_appear=False
    while game_start:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    a.Leftmove()
                    a.Y_bolen=False
                if event.key==pygame.K_RIGHT:
                    a.Rightmove()
                    a.Y_bolen=False
                if event.key==pygame.K_UP:
                    a.Upmove()
                if event.key==pygame.K_DOWN:
                    a.Downmove()
                if event.key==pygame.K_z:
                    b.move()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN or event.key==pygame.K_z:
                    a.X_bolen=False
                    a.Y_bolen=False
                    b.btbolen=False
            if event.type==UFOEVENT:
                u_appear=True
                u.appeared=True
        gameDisplay.blit(bg,bg_rect)
        if not u.appeared:  #當飛碟沒出現時,畫面滾動
            bg_y+=1
            bg_y1+=1
        gameDisplay.blit(bg,(bg_x,bg_y))
        gameDisplay.blit(bg,(bg_x1,bg_y1))
        if bg_y > 600:
            bg_y=-600
        if bg_y1 > 600:
            bg_y1=-600
        if u_appear:  #當飛碟事件觸發時
            pygame.mixer.music.pause()
            ufo_music.play(-1)
            ufoappear()
            s.reset1()  #當補給物(火彈)被吃掉時,過一段時間會再出現
            s1.reset1() #同上(補血)
            if s.visible:   #補給物(火彈)
                gameDisplay.blit(s.image,s.rect)
                s.rect[1]+=s.supply_speed
                if s.rect[1] > 600:
                    s.reset()
            if s1.visible:  #補給物(補血)
                gameDisplay.blit(s1.image,s1.rect)
                s1.rect[1]+=s1.supply_speed
                if s1.rect[1] > 600:
                    s1.reset()
        #飛機的生命值顯示(*3)
        if a_image2:
            gameDisplay.blit(pygame.transform.scale(a.image,(41,56)),(120,0))
        if a_image1:
            gameDisplay.blit(pygame.transform.scale(a.image,(41,56)),(181,0))
        if a_image:
            gameDisplay.blit(pygame.transform.scale(a.image,(41,56)),(242,0))
        a.health(gameDisplay,red,0,0) #飛機血條
        if a.active:  #如果飛機存活
            if a.X_bolen:
                a.rect[0]+=a.airplane_speedx
                b.rect[0]=a.rect[0]+25
                fire_b.rect[0]=a.rect[0]-25
                fire_b1.rect[0]=a.rect[0]+41
                if a.rect[0]+71 > 800:
                    a.rect[0]=729
                if a.rect[0] < 0:
                    a.rect[0]=0
            if a.Y_bolen:
                a.rect[1]+=a.airplane_speedy
                if a.rect[1]+86 > 600:
                    a.rect[1]=514
                if a.rect[1] < 0:
                    a.rect[1]=0
            #使飛機有噴氣效果
            if a.switch_name:  
                gameDisplay.blit(a.image,a.rect)
            else:
                gameDisplay.blit(a1.image,a.rect)
            if not (delay%5):  #延時效果,每五幀換一次
                a.switch_name=not a.switch_name
            delay-=1
            if not delay:
                delay=120
        else:    #飛機死亡
            if bomb1.visible:
                myairplane_dead_sound.play()
                bomb1.draw(a.rect)
                bomb1.action()
                #飛機的生命值減掉
                if index1==0:
                    gameDisplay.blit(bg,(242,0),(242,0,41,56))
                    a_image=False
                if index1==1:
                    gameDisplay.blit(bg,(181,0),(181,0,41,56))
                    a_image1=False
                if index1==2:
                    gameDisplay.blit(bg,(120,0),(120,0,41,56))
                    a_image2=False
                    game_start=False
                    u.reset((143,-700))
                    l.reset((325,120))
                    u.appeared=False
                    u.health=10000
                    ufo_music.stop()
                    pygame.mixer.music.pause()
                    gameover_music.play()
                    game_over()
            if bomb1.otherairplane_alive:   #爆炸播放完畢後
                a.reset((x-300,y))  #飛機復位
                a.airplane_speedy=0
                b.rect[0]=x-300+25  #子彈復位
                b.rect[1]=y
                fire_b.rect[0]=x-300-25  #火彈復位
                fire_b1.rect[0]=x-300+61
                fire_b.rect[1]=fire_b1.rect[1]=y
                index1+=1
        if boss.rect[1] > -100:  #如果大敵機的高度大於-100時,會出現補給物
            if s.visible:   #補給物(火彈)
                gameDisplay.blit(s.image,s.rect)
                s.rect[1]+=s.supply_speed
                if s.rect[1] > 600:
                    s.reset()
            if s1.visible:  #補給物(補血)
                gameDisplay.blit(s1.image,s1.rect)
                s1.rect[1]+=s1.supply_speed
                if s1.rect[1] > 600:
                    s1.reset()
        #飛機與敵機,大敵機,補給物,飛碟的碰撞檢測
        if pygame.sprite.spritecollide(a,otherairplanes,False,pygame.sprite.collide_rect_ratio(0.5)):
            if u.appeared==False:
                a.blood_len-=1
                if a.blood_len <= 0:
                    a.active=False
                    bomb1.visible=True
                    a.blood_len=100
        if pygame.sprite.spritecollide(a,bullet_group,False,pygame.sprite.collide_rect_ratio(0.5)):
            if u.appeared==False:
                a.blood_len-=1
                if a.blood_len <= 0:
                    a.active=False
                    bomb1.visible=True
                    a.blood_len=100
        if pygame.sprite.collide_rect_ratio(0.5)(boss,a):
            if u.appeared==False:
                a.blood_len-=5
                if a.blood_len <= 0:
                    a.active=False
                    bomb1.visible=True
                    a.blood_len=100
        if pygame.sprite.collide_mask(a,s1):
            supply_sound.play()
            s1.visible=False
            a.blood_len+=50
            if a.blood_len >= 100:
                a.blood_len=100
            s1.reset() #補給物復位
        if pygame.sprite.collide_mask(a,s):
            supply_sound.play()
            s.visible=False
            fire_b.fire_btbolen=True
            s.reset()  #補給物復位
        if pygame.sprite.collide_rect(a,l):
            if u.rect[1]==-74:
                a.Y_bolen=True
                a.airplane_speedy=-8
        if pygame.sprite.collide_mask(a,u):
            if u.rect[1]==-74:
                a.blood_len-=40
                if a.blood_len <= 0:
                    a.active=False
                    bomb1.visible=True
                    a.blood_len=100
        if pygame.sprite.spritecollide(a,ubgroup,False,pygame.sprite.collide_rect_ratio(0.4)):
            if u.ub_visible==True:
                a.blood_len-=15
                if a.blood_len <= 0:
                    a.active=False
                    bomb1.visible=True
                    a.blood_len=100
        if b.btbolen:    #按下z鍵發射子彈
            bullet_sound.play()
            if launch:  #當我方飛機不是在初始位置發射時,子彈的初始高度(y)存取我方飛機的高度
                b.rect[1]=a.rect[1]
                launch=False
            gameDisplay.blit(b.image,b.rect)
            b.rect[1]+=b.bullet_speed
            if b.rect[1]<-60:
                b.rect[1]=a.rect[1] #子彈復位
                gameDisplay.blit(b.image,b.rect)
        if fire_b.fire_btbolen:  #發射火彈
            fire_sound.play()
            if launch1:  #同launch的作法
                fire_b.rect[1]=a.rect[1]
                fire_b1.rect[1]=a.rect[1]
                launch1=False
            gameDisplay.blit(fire_b.image,fire_b.rect)
            gameDisplay.blit(fire_b1.image,fire_b1.rect)
            fire_b.rect[1]+=fire_b.fire_speed
            fire_b1.rect[1]+=fire_b1.fire_speed
            if fire_b.rect[1] < -60 or fire_b1.rect[1] < -60:
                fire_b.rect[1]=a.rect[1]  #火彈復位
                fire_b1.rect[1]=a.rect[1]
            index2+=1
            if index2==500: #火彈持續時間
                fire_b.fire_btbolen=False
                index2=0
        #子彈與敵機的碰撞檢測
        result=pygame.sprite.spritecollide(b,otherairplanes,False,pygame.sprite.collide_mask)
        if result:
            if  b.btbolen:   #子彈發射後
                for r in result:
                    r.active=False
                    bombposition=r.rect
                bomb.visible=True
                bomb.otherairplane_alive=False
        if not u.appeared:
            for p in otherairplanes:
                if p.rect[1]>600:
                    p.active=False
                    bomb.otherairplane_alive=True
                if  boss.add_other_speed:  #當boss被打敗時,所有小敵機速度加2
                    p.o_speed+=2
            for i in otherairplanes:
                if i.active:  #如果敵機存活
                    gameDisplay.blit(i.image,i.rect)
                    i.rect[1]+=i.o_speed
                else:      #敵機死亡
                    if bomb.visible:
                        other_dead_sound.play()
                        bomb.draw(bombposition)
                        bomb.action()
                    if bomb.otherairplane_alive:
                        i.reset(random.randint(0,775),random.randint(-250,-150))  #敵機復位
        #子彈與大敵機的碰撞檢測
        result1=pygame.sprite.collide_mask(b,boss)
        if result1:
            if u.appeared==False:
                if  b.btbolen:
                    b.rect[1]=a.rect[1] #打中之後,子彈復位
                    index+=1
                    if index==140: #打中一百四十發後大敵機死亡
                        boss.active=False
                        boss.bombhappen=True
                        boss.boss_relive=False
                        index=0
        #子彈與飛碟的碰撞檢測
        if pygame.sprite.collide_rect_ratio(0.67)(b,u):
            if b.btbolen:
                b.rect[1]=a.rect[1] 
                u.health-=3
                if u.health <= 0:
                    u.active=False
                    u.bombhappen=True
                    u.health=10000
        #火彈與小敵機的碰檢
        result3=pygame.sprite.groupcollide(otherairplanes,bullets,False,False,pygame.sprite.collide_mask)
        if result3:
            if fire_b.fire_btbolen:  #火彈發射後
                for rr in result3:
                    rr.active=False
                    bombposition=rr.rect
                bomb.visible=True
                bomb.otherairplane_alive=False
        #火彈與大敵機的碰撞檢測
        result4=pygame.sprite.spritecollide(boss,bullets,False,pygame.sprite.collide_mask)
        if result4:
            if fire_b.fire_btbolen:
                fire_b.rect[1]=a.rect[1]
                fire_b1.rect[1]=a.rect[1]
                index3+=30  #火彈的殺傷力
                if index3 >= 780:
                    boss.active=False
                    boss.bombhappen=True
                    boss.boss_relive=False
                    index3=0
        #火彈與飛碟的碰撞檢測
        if pygame.sprite.spritecollide(u,bullets,False,pygame.sprite.collide_rect_ratio(0.67)):
            if fire_b.fire_btbolen:
                fire_b.rect[1]=a.rect[1]
                fire_b1.rect[1]=a.rect[1]
                u.health-=70
                if u.health <= 0:
                    u.active=False
                    u.bombhappen=True
                    u.health=15000
        if not u.appeared:
            if boss.rect[1] > 600:
                boss.reset((random.randint(0,500),-600))
                b1.rect[0]=boss.rect[0]
                b2.rect[0]=boss.rect[0]+185
                index=0
                index3=0
                s.visible=True  #當大敵機活著飛到高度大於600時,會再度出現補給物s,s1
                s1.visible=True
            if boss.active: #如果大敵機存活
                boss.add_other_speed=False #關掉速度加1
                gameDisplay.blit(boss.image,boss.rect)
                boss.rect[1]+=boss.boss_speed
                if boss.rect[1] > 0: #當大敵機出現時發射子彈
                    bullet_sound.play()
                    gameDisplay.blit(b1.image,b1.rect)
                    gameDisplay.blit(b2.image,b2.rect)
                    b1.rect[1]+=b1.bullet_speed
                    b2.rect[1]+=b2.bullet_speed
                    if b1.rect[1] > 660 or b2.rect[1] > 660:
                        b1.rect[1]=boss.rect[1]
                        b2.rect[1]=boss.rect[1]
            else:  #大敵機死亡
                b.rect[1]=a.rect[1]
                if boss.bombhappen:
                    boss_dead_sound.play()
                    boss.draw(boss.rect)
                    boss.action()
                if boss.boss_relive:
                    boss.reset((random.randint(0,500),-600))
                    b1.rect[0]=boss.rect[0]
                    b2.rect[0]=boss.rect[0]+185
                    s1.visible=True  #出現補給物(補血)
        pygame.display.update()  #畫面刷新
        clock.tick(60)  #遊戲幀率60幀
game_intro()
gameloop()
pygame.quit()
quit()