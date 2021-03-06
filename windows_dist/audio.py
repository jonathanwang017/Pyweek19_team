import pygame
pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=4096)

directory = ''


def play_sound(sound, time):
	sound = pygame.mixer.Sound(sound)
	if time == 0:
		sound.play()
	else:
		sound.play(maxtime = time)

def stop_sound(sound):
    sound = pygame.mixer.Sound(sound)
    sound.stop()

def hit_wall():
	play_sound(directory + 'hitwall_sfx.wav', 0)

def level_end():
	play_sound(directory + 'levelend_sfx.wav', 0)

def hit_switch():
	play_sound(directory + 'switchstep_sfx.wav', 1000)

def step_spike():
	play_sound(directory + 'spikestep_sfx.wav', 0)

def bg_music():
	bgm = pygame.mixer.Sound('Pyweek_BG_1.wav')	
	bgm.set_volume(0.3)
	bgm.play()

def bg_music_stop():
	bgm = pygame.mixer.Sound('Pyweek_BG_1.wav')	
	bgm.stop()