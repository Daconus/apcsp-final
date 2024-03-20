@namespace
class SpriteKind:
    UI = SpriteKind.create()
    enemy_Proj = SpriteKind.create()

def on_b_pressed():
    global playerWeapon, currentWeapon
    if weapon_1 == playerWeapon:
        playerWeapon = weapon_2
        currentWeapon = 2
    else:
        playerWeapon = weapon_1
        currentWeapon = 1
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(sprite)
    playLongSFX(lsfx_player_hit, 0)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.enemy_Proj, SpriteKind.player, on_on_overlap)

# This function takes a long sound effect and plays it
def playLongSFX(lsfx: List[music.Playable], delay: number):
    for sound in lsfx:
        music.play(sound, music.PlaybackMode.UNTIL_DONE)
        pause(delay)

def on_life_zero():
    sprites.destroy(playerSprite, effects.disintegrate, 500)
    music.play(sfx_death, music.PlaybackMode.UNTIL_DONE)
    game.game_over(False)
info.on_life_zero(on_life_zero)

def updateMissileDisplay():
    ui_missileDigitTen.set_position(7, 9)
    ui_missileDigitOne.set_position(13, 9)
    ui_missileDigitOne.set_image(digits[missile_count % 10])
    ui_missileDigitTen.set_image(digits[int(missile_count / 10)])
proj_plasma: Sprite = None
proj_missile: Sprite = None
proj_trishot: Sprite = None
proj_basic: Sprite = None
currentWeapon = 0
ui_missileDigitTen: Sprite = None
ui_missileDigitOne: Sprite = None
playerWeapon = 0
weapon_2 = 0
weapon_1 = 0
missile_count = 0
playerSprite: Sprite = None
sfx_death: music.SoundEffect = None
lsfx_player_hit: List[music.SoundEffect] = []
digits: List[Image] = []
effects.star_field.start_screen_effect()
digits = [assets.image("""
        ui_digit_0
    """),
    assets.image("""
        ui_digit_1
    """),
    assets.image("""
        ui_digit_2
    """),
    assets.image("""
        ui_digit_3
    """),
    assets.image("""
        ui_digit_4
    """),
    assets.image("""
        ui_digit_5
    """),
    assets.image("""
        ui_digit_6
    """),
    assets.image("""
        ui_digit_7
    """),
    assets.image("""
        ui_digit_8
    """),
    assets.image("""
        ui_digit_9
    """)]
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
    55,
    300,
    SoundExpressionEffect.VIBRATO,
    InterpolationCurve.LOGARITHMIC)
# sound for missile shot
sfx_shoot_plasma = music.create_sound_effect(WaveShape.SQUARE,
    1463,
    1,
    255,
    50,
    400,
    SoundExpressionEffect.WARBLE,
    InterpolationCurve.CURVE)
# sound for missile shot
sfx_death = music.create_sound_effect(WaveShape.SQUARE,
    4299,
    1137,
    255,
    50,
    1000,
    SoundExpressionEffect.WARBLE,
    InterpolationCurve.CURVE)
# sound for player heal
sfx_heal = music.create_sound_effect(WaveShape.SINE,
    1,
    3812,
    255,
    113,
    200,
    SoundExpressionEffect.NONE,
    InterpolationCurve.CURVE)
sfx_plasma_explosion = music.create_sound_effect(WaveShape.SQUARE,
    1463,
    1,
    255,
    17,
    500,
    SoundExpressionEffect.WARBLE,
    InterpolationCurve.CURVE)
sfx_missile_explosion = music.create_sound_effect(WaveShape.NOISE,
    1538,
    379,
    255,
    0,
    250,
    SoundExpressionEffect.TREMOLO,
    InterpolationCurve.CURVE)
playerSprite = sprites.create(assets.image("""
    player_ship
"""), SpriteKind.player)
weaponCooldown = 0
missile_count = 15
weapon_1 = 0
weapon_2 = 1
playerWeapon = weapon_1
playerSprite.set_position(80, 100)
controller.move_sprite(playerSprite, 100, 100)
ui_base = sprites.create(assets.image("""
    ui
"""), SpriteKind.UI)
ui_missileDigitOne = sprites.create(assets.image("""
    ui_digit_0
"""), SpriteKind.UI)
ui_missileDigitTen = sprites.create(assets.image("""
    ui_digit_0
"""), SpriteKind.UI)
updateMissileDisplay()

def on_on_update():
    global weaponCooldown, proj_basic, proj_trishot, proj_missile, missile_count, proj_plasma
    if playerWeapon == 0 and (weaponCooldown == 0 and controller.A.is_pressed()):
        weaponCooldown = 0.2
        proj_basic = sprites.create_projectile_from_sprite(assets.image("""
            proj_basic
        """), playerSprite, 0, -250)
        music.play(sfx_shoot_basic, music.PlaybackMode.IN_BACKGROUND)
    if playerWeapon == 2 and (weaponCooldown == 0 and controller.A.is_pressed()):
        weaponCooldown = 0.3
        proj_trishot = sprites.create_projectile_from_sprite(assets.image("""
                proj_trishot
            """),
            playerSprite,
            50,
            -250)
        proj_trishot = sprites.create_projectile_from_sprite(assets.image("""
                proj_trishot
            """),
            playerSprite,
            0,
            -250)
        proj_trishot = sprites.create_projectile_from_sprite(assets.image("""
                proj_trishot
            """),
            playerSprite,
            -50,
            -250)
        music.play(sfx_shoot_basic, music.PlaybackMode.IN_BACKGROUND)
    if playerWeapon == 1 and (missile_count > 0 and (weaponCooldown == 0 and controller.A.is_pressed())):
        weaponCooldown = 0.6
        proj_missile = sprites.create_projectile_from_sprite(assets.image("""
            myImage
        """), playerSprite, 0, -250)
        music.play(sfx_shoot_missile, music.PlaybackMode.IN_BACKGROUND)
        missile_count += -1
        updateMissileDisplay()
    if playerWeapon == 3 and (weaponCooldown == 0 and controller.A.is_pressed()):
        weaponCooldown = 1.5
        proj_plasma = sprites.create_projectile_from_sprite(assets.image("""
            proj_plasma
        """), playerSprite, 0, -250)
        music.play(sfx_shoot_plasma, music.PlaybackMode.IN_BACKGROUND)
game.on_update(on_on_update)

def on_on_update2():
    if playerSprite.x < 9:
        playerSprite.x = 9
    if playerSprite.x > 152:
        playerSprite.x = 152
    if playerSprite.y < 7:
        playerSprite.y = 7
    if playerSprite.y > 114:
        playerSprite.y = 114
game.on_update(on_on_update2)

def on_update_interval():
    global weaponCooldown
    if weaponCooldown < 0.1 and weaponCooldown != 0:
        weaponCooldown = 0
    if weaponCooldown > 0:
        weaponCooldown += -0.1
game.on_update_interval(100, on_update_interval)
