# This function takes a long sound effect and plays it
def playLongSFX(lsfx: List[music.Playable], delay: number):
    for sound in lsfx:
        music.play(sound, music.PlaybackMode.UNTIL_DONE)
        pause(delay)
# sound for basic shot
sfx_shoot_basic = music.create_sound_effect(WaveShape.SQUARE,
    3648,
    300,
    255,
    129,
    150,
    SoundExpressionEffect.NONE,
    InterpolationCurve.LOGARITHMIC)
# sound for missile shot
sfx_shoot_missile = music.create_sound_effect(WaveShape.NOISE,
    2430,
    958,
    255,
    113,
    300,
    SoundExpressionEffect.VIBRATO,
    InterpolationCurve.LOGARITHMIC)
# sound for salvo shot
lsfx_shoot_salvo = [music.create_sound_effect(WaveShape.SAWTOOTH,
        2430,
        958,
        255,
        113,
        75,
        SoundExpressionEffect.VIBRATO,
        InterpolationCurve.LOGARITHMIC),
    music.create_sound_effect(WaveShape.SAWTOOTH,
        2430,
        958,
        255,
        113,
        75,
        SoundExpressionEffect.VIBRATO,
        InterpolationCurve.LOGARITHMIC),
    music.create_sound_effect(WaveShape.SAWTOOTH,
        2430,
        958,
        255,
        113,
        75,
        SoundExpressionEffect.VIBRATO,
        InterpolationCurve.LOGARITHMIC)]
# sound for weaker hits
lsfx_basic_hit = [music.create_sound_effect(WaveShape.NOISE,
        3856,
        1,
        255,
        255,
        30,
        SoundExpressionEffect.TREMOLO,
        InterpolationCurve.LINEAR),
    music.create_sound_effect(WaveShape.NOISE,
        1984,
        1627,
        148,
        81,
        100,
        SoundExpressionEffect.WARBLE,
        InterpolationCurve.LOGARITHMIC)]
# sound for player hit
lsfx_player_hit = [music.create_sound_effect(WaveShape.NOISE,
        1627,
        3232,
        255,
        255,
        300,
        SoundExpressionEffect.TREMOLO,
        InterpolationCurve.LINEAR),
    music.create_sound_effect(WaveShape.NOISE,
        1627,
        3232,
        255,
        255,
        300,
        SoundExpressionEffect.TREMOLO,
        InterpolationCurve.LINEAR),
    music.create_sound_effect(WaveShape.NOISE,
        1627,
        3232,
        255,
        255,
        300,
        SoundExpressionEffect.TREMOLO,
        InterpolationCurve.LINEAR)]
# sound for player heal
sfx_heal = music.create_sound_effect(WaveShape.SINE,
    1,
    3812,
    255,
    113,
    200,
    SoundExpressionEffect.NONE,
    InterpolationCurve.CURVE)
sfx_missile_explosion = music.create_sound_effect(WaveShape.NOISE,
    2474,
    1137,
    255,
    108,
    500,
    SoundExpressionEffect.TREMOLO,
    InterpolationCurve.LOGARITHMIC)
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)