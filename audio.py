import pygame
pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=4096)


def play_sound(sound, time):
	sound = pygame.mixer.Sound(sound)
	if time == 0:
		sound.play()
	else:
		sound.play(maxtime = time)

def hit_wall():
	play_sound('SFX/HitWall_SFX_16.wav', 0)

def level_end():
	play_sound('SFX/LevelEnd_SFX_16.wav', 0)

def hit_switch():
	play_sound('SFX/SwitchStep_SFX_NoReveal_16.wav', 1000)

def step_spike():
	play_sound('SFX/SpikeStep_SFX_16.wav', 0)
