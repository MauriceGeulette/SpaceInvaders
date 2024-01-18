from spaceInvadersGUI import *
import os

go_to_the_game = False
pause_sounds = False
mouse_up = False
score = 0

while True:
    if not go_to_the_game:
        show_opening_screen()
        with open('score.txt', 'r') as file:
            print_high_score = int(file.read())
        text_high_score = Label(x=90, y=50, text="High score: " + str(print_high_score), color=WHITE, size=30)
        go_to_the_game = True

    clock.tick(FPS)
    win.blit(background, (0,0))

    my_shieldbar.draw(my_shieldbar.shield_pct)
    all_sprites.draw(win)
    all_sprites.update()
    user_score.draw(win)
    text_high_score.draw(win)
    stop_bg_music.draw(win)

    if stop_bg_music.is_clicked():
        if not mouse_up:
            if not pause_sounds:
                stop_sounds()
                stop_bg_music.text = 'Play sounds'
                pause_sounds = True
            else:
                play_sounds()
                stop_bg_music.text = 'Stop sounds'
                pause_sounds = False
        else:
            mouse_up = False

    pygame.display.update()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.shoot()


    bullet_and_meteor_collide = pygame.sprite.groupcollide(meteors, my_player.bullets, True, True)
    for collision in bullet_and_meteor_collide:
        score += 1
        if score == 50:
            create_boss()
        new_high_score = score
        user_score.set_text('Score: ' + str(score))
        create_meteor()
        create_explosion(collision.rect.center, 'large')

    bullet_and_player_collide = pygame.sprite.spritecollide(my_player, meteors, True)
    for collision in bullet_and_player_collide:
        my_shieldbar.shield_pct -= 10
        create_meteor()
        create_explosion(collision.rect.center, 'small')
        if my_shieldbar.shield_pct <= 0:
            with open('score.txt', 'r') as file:
                high_score = int(file.read())
            if score > high_score:
                with open('score.txt', 'w') as file:
                    file.write(str(new_high_score))
            message = 'score: ' + str(score)
            game_over(message)

            if not game_over(message):
                score = 0
                boss_
                user_score.set_text(str(score))
                my_shieldbar.shield_pct = 100
                go_to_the_game = False
