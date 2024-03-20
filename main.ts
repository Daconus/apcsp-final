namespace SpriteKind {
    export const UI = SpriteKind.create()
    export const enemy_Proj = SpriteKind.create()
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (weapon_1 == playerWeapon) {
        playerWeapon = weapon_2
        currentWeapon = 2
    } else {
        playerWeapon = weapon_1
        currentWeapon = 1
    }
})
sprites.onOverlap(SpriteKind.enemy_Proj, SpriteKind.Player, function (sprite, otherSprite) {
    sprites.destroy(sprite)
    playLongSFX(lsfx_player_hit, 0)
    info.changeLifeBy(-1)
})
// This function takes a long sound effect and plays it
function playLongSFX (lsfx: music.Playable[], delay: number) {
    for (let sound of lsfx) {
        music.play(sound, music.PlaybackMode.UntilDone)
        pause(delay)
    }
}
info.onLifeZero(function () {
    sprites.destroy(playerSprite, effects.disintegrate, 500)
    music.play(sfx_death, music.PlaybackMode.UntilDone)
    game.gameOver(false)
})
function updateMissileDisplay () {
    ui_missileDigitTen.setPosition(7, 9)
    ui_missileDigitOne.setPosition(13, 9)
    ui_missileDigitOne.setImage(digits[missile_count % 10])
    ui_missileDigitTen.setImage(digits[Math.trunc(missile_count / 10)])
}
let proj_plasma: Sprite = null
let proj_missile: Sprite = null
let proj_trishot: Sprite = null
let proj_basic: Sprite = null
let currentWeapon = 0
let ui_missileDigitTen: Sprite = null
let ui_missileDigitOne: Sprite = null
let playerWeapon = 0
let weapon_2 = 0
let weapon_1 = 0
let missile_count = 0
let playerSprite: Sprite = null
let sfx_death: music.SoundEffect = null
let lsfx_player_hit: music.SoundEffect[] = []
let digits: Image[] = []
effects.starField.startScreenEffect()
digits = [
assets.image`ui_digit_0`,
assets.image`ui_digit_1`,
assets.image`ui_digit_2`,
assets.image`ui_digit_3`,
assets.image`ui_digit_4`,
assets.image`ui_digit_5`,
assets.image`ui_digit_6`,
assets.image`ui_digit_7`,
assets.image`ui_digit_8`,
assets.image`ui_digit_9`
]
// sound for weaker hits
let lsfx_basic_hit = [music.createSoundEffect(WaveShape.Noise, 3856, 1, 255, 255, 30, SoundExpressionEffect.Tremolo, InterpolationCurve.Linear), music.createSoundEffect(WaveShape.Noise, 1984, 1627, 148, 81, 100, SoundExpressionEffect.Warble, InterpolationCurve.Logarithmic)]
// sound for player hit
lsfx_player_hit = [music.createSoundEffect(WaveShape.Noise, 1627, 3232, 255, 255, 300, SoundExpressionEffect.Tremolo, InterpolationCurve.Linear), music.createSoundEffect(WaveShape.Noise, 1627, 3232, 255, 255, 300, SoundExpressionEffect.Tremolo, InterpolationCurve.Linear), music.createSoundEffect(WaveShape.Noise, 1627, 3232, 255, 255, 300, SoundExpressionEffect.Tremolo, InterpolationCurve.Linear)]
// sound for basic shot
let sfx_shoot_basic = music.createSoundEffect(WaveShape.Square, 3648, 300, 255, 129, 150, SoundExpressionEffect.None, InterpolationCurve.Logarithmic)
// sound for missile shot
let sfx_shoot_missile = music.createSoundEffect(WaveShape.Noise, 2430, 958, 255, 55, 300, SoundExpressionEffect.Vibrato, InterpolationCurve.Logarithmic)
// sound for missile shot
let sfx_shoot_plasma = music.createSoundEffect(WaveShape.Square, 1463, 1, 255, 50, 400, SoundExpressionEffect.Warble, InterpolationCurve.Curve)
// sound for missile shot
sfx_death = music.createSoundEffect(WaveShape.Square, 4299, 1137, 255, 50, 1000, SoundExpressionEffect.Warble, InterpolationCurve.Curve)
// sound for player heal
let sfx_heal = music.createSoundEffect(WaveShape.Sine, 1, 3812, 255, 113, 200, SoundExpressionEffect.None, InterpolationCurve.Curve)
let sfx_plasma_explosion = music.createSoundEffect(WaveShape.Square, 1463, 1, 255, 17, 500, SoundExpressionEffect.Warble, InterpolationCurve.Curve)
let sfx_missile_explosion = music.createSoundEffect(WaveShape.Noise, 1538, 379, 255, 0, 250, SoundExpressionEffect.Tremolo, InterpolationCurve.Curve)
playerSprite = sprites.create(assets.image`player_ship`, SpriteKind.Player)
let weaponCooldown = 0
missile_count = 15
weapon_1 = 0
weapon_2 = 1
playerWeapon = weapon_1
playerSprite.setPosition(80, 100)
controller.moveSprite(playerSprite, 100, 100)
let ui_base = sprites.create(assets.image`ui`, SpriteKind.UI)
ui_missileDigitOne = sprites.create(assets.image`ui_digit_0`, SpriteKind.UI)
ui_missileDigitTen = sprites.create(assets.image`ui_digit_0`, SpriteKind.UI)
updateMissileDisplay()
game.onUpdate(function () {
    if (playerWeapon == 0 && (weaponCooldown == 0 && controller.A.isPressed())) {
        weaponCooldown = 0.2
        proj_basic = sprites.createProjectileFromSprite(assets.image`proj_basic`, playerSprite, 0, -250)
        music.play(sfx_shoot_basic, music.PlaybackMode.InBackground)
    }
    if (playerWeapon == 2 && (weaponCooldown == 0 && controller.A.isPressed())) {
        weaponCooldown = 0.3
        proj_trishot = sprites.createProjectileFromSprite(assets.image`proj_trishot`, playerSprite, 50, -250)
        proj_trishot = sprites.createProjectileFromSprite(assets.image`proj_trishot`, playerSprite, 0, -250)
        proj_trishot = sprites.createProjectileFromSprite(assets.image`proj_trishot`, playerSprite, -50, -250)
        music.play(sfx_shoot_basic, music.PlaybackMode.InBackground)
    }
    if (playerWeapon == 1 && (missile_count > 0 && (weaponCooldown == 0 && controller.A.isPressed()))) {
        weaponCooldown = 0.6
        proj_missile = sprites.createProjectileFromSprite(assets.image`myImage`, playerSprite, 0, -250)
        music.play(sfx_shoot_missile, music.PlaybackMode.InBackground)
        missile_count += -1
        updateMissileDisplay()
    }
    if (playerWeapon == 3 && (weaponCooldown == 0 && controller.A.isPressed())) {
        weaponCooldown = 1.5
        proj_plasma = sprites.createProjectileFromSprite(assets.image`proj_plasma`, playerSprite, 0, -250)
        music.play(sfx_shoot_plasma, music.PlaybackMode.InBackground)
    }
})
game.onUpdate(function () {
    if (playerSprite.x < 9) {
        playerSprite.x = 9
    }
    if (playerSprite.x > 152) {
        playerSprite.x = 152
    }
    if (playerSprite.y < 7) {
        playerSprite.y = 7
    }
    if (playerSprite.y > 114) {
        playerSprite.y = 114
    }
})
game.onUpdateInterval(100, function () {
    if (weaponCooldown < 0.1 && weaponCooldown != 0) {
        weaponCooldown = 0
    }
    if (weaponCooldown > 0) {
        weaponCooldown += -0.1
    }
})
