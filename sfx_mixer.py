import pygame

class SFXMixer:
    def __init__(self, path, state_mngr):
        self.statemixer = StateSFXMixer(path, state_mngr)

    def mix(self):
        self.statemixer.mix_state()

    def mix_now(self, state_string):
        self.statemixer.mix_now(state_string)


class StateSFXMixer:
    def __init__(self, path, state_mngr):
        self.path = path
        self.mixer_state_mngr = state_mngr
        self.sfx_dict = {}
        for state in self.mixer_state_mngr.states[1:]:
            # ASSUMING THERE IS ONLY 1 SOUND FOR EACH STATE
            path = self.path + "sounds/" + state + ".wav"
            sfx_sound = pygame.mixer.Sound(path)
            self.sfx_dict[state] = dict(length=sfx_sound.get_length(), sound=sfx_sound)

        self.counter = 0
        self.last_state = None

    def mix_state(self):
        current_state = self.mixer_state_mngr.state

        if current_state in self.mixer_state_mngr.states[5:]:
            sound = self.sfx_dict[current_state]["sound"]
            sound_frames = int(self.sfx_dict[current_state]["length"] / (1/60))

            if current_state != self.last_state:
                self.counter = 0

            if self.counter % sound_frames == 0:
                pygame.mixer.Sound.play(sound)

        self.counter += 1
        self.last_state = current_state

    def mix_now(self, state_string):
        current_state = state_string
        if current_state != "normal":
            sound = self.sfx_dict[current_state]["sound"]
            pygame.mixer.Sound.play(sound)

class EventSFX:
    def __init__(self, path):
        pass
