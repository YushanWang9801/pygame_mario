import pygame
import Components as Com

def display_score(start_time):
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    Com.text_score_surface = Com.test_font.render(
                        "Scores: " + f'{current_time}', False, "Green")
    Com.text_score_rect = Com.text_score_surface.\
                                get_rect(center= 
                                  (Com.FONT_POS_X, Com.FONT_SIZE))
    return current_time

def obstacle_collision_sprite():
    if pygame.sprite.spritecollide(Com.player.sprite,Com.obstacle_group,False):
        Com.obstacle_group.empty()
        return True
    else: return False

def coin_collision_sprite():
    coin_hit_list = pygame.sprite.spritecollide(\
                    Com.player.sprite,Com.coins_group, True)
    return len(coin_hit_list)

def render_life(life):
    Com.text_life_surface = Com.test_font.render(
                        "Life: " + f'{life}', False, "Green")
    Com.text_life_rect = Com.text_life_surface.\
                            get_rect(center= (Com.FONT_POS_X, Com.FONT_SIZE*2)) 
       
def add_coin_score(start_time, hit_score):
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    current_time += hit_score*10
    Com.text_score_surface = Com.test_font.render(
                "Scores: " + f'{current_time}', False, "Green")

    Com.text_score_rect = Com.text_score_surface.get_rect(
                                    center = (Com.FONT_POS_X, Com.FONT_SIZE))
    return current_time