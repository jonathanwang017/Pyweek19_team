import pygame
pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=4096)

directory = 'data/'

def play_sound(sound, time):
	sound = pygame.mixer.Sound(sound)
	if time == 0:
		sound.play()
	else:
		sound.play(maxtime = time)

def hit_wall():
	play_sound(directory + 'hitwall_sfx.wav', 0)

def level_end():
	play_sound(directory + 'levelend_sfx.wav', 0)

def hit_switch():
	play_sound(directory + 'switchstep_sfx.wav', 1000)

def step_spike():
	play_sound(directory + 'spikestep_sfx.wav', 0)
