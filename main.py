import pygame as pg
import sys
import os
clock = pg.time.Clock()
Battleground_frame = os.listdir("Battleground")
Boss_frame = os.listdir("Boss of location")
FPS = 8 #Можно выставить и 60, но будет некомфортно глазам
pg.init()
Boss_iterator = 0
sc = pg.display.set_mode((1600, 900))
iterator = 0
def Battleground1_drawing(iterator):
    Battleground_frame_surf = pg.image.load('Battleground/' + Battleground_frame[iterator])
    Battleground_frame_scale = pg.transform.scale(Battleground_frame_surf, (1600,900))
    Battleground_frame_rect = Battleground_frame_scale.get_rect()
    sc.blit(Battleground_frame_scale, Battleground_frame_rect)
def Boss1_drawing(iterator):
    Boss_frame_surf = pg.image.load('Boss of location/' + Boss_frame[iterator])
    Boss_frame_scale = pg.transform.scale(Boss_frame_surf, (800, 600))
    Boss_frame_rect = Boss_frame_scale.get_rect(bottomright = (1200,800))
    sc.blit(Boss_frame_scale, Boss_frame_rect)
pg.display.update()
while True:
    clock.tick(FPS)
    Battleground1_drawing(iterator)
    Boss1_drawing(Boss_iterator)
    if Boss_iterator >= len(Boss_frame)-1:
        Boss_iterator = 0
    else:
        Boss_iterator += 1
    if iterator>=len(Battleground_frame)-1:
        iterator=0
    else:
        iterator+=1
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    pg.display.update()