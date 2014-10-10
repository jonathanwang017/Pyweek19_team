import pygame
pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=4096)


def play_sound(sound):
	sound = pygame.mixer.Sound(sound)
	sound.play()

def hit_wall():
	play_sound('SFX/HitWall_SFX_16.wav')

def level_end():
	play_sound('SFX/LevelEnd_SFX_16.wav')

def hit_switch():
	play_sound('SFX/SwitchStep_SFX_NoReveal_16.wav')

def step_spike():
	play_sound('SFX/SpikeStep_SFX_16.wav')

# def start_music():
# 	global volume, tracks
# 	tracks[0].set_volume(volume)
# 	tracks[0].play(-1)

# def play_tracks(trackCount):
# 	global volume, tracks
# 	for x in range(1, trackCount + 1):
# 		tracks[x].set_volume(noise)
# 		tracks[x].play(-1)

# def increase_volume():
# 	global volume, tracks
# 	volume += 0.1
# 	tracks[0].set_volume(volume)

# def stop_music():
# 	global tracks
# 	tracks[0].fadeout(1000)
# 	pygame.time.delay(1000)

# def cut_tracks():
# 	global tracks
# 	for x in range(1, len(tracks) - 1):
# 		tracks[x].stop()

# def pause_track(trackCounter):
# 	global tracks
# 	tracks[trackCounter].set_volume(0)

# def unpause_tracks():
# 	global volume, tracks
# 	for x in range(1, len(tracks)):
# 		tracks[x].set_volume(noise)
