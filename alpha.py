import time
import thumby
import math

# BITMAP: width: 110, height: 78
# BITMAP: width: 32, height: 23
# BITMAP: width: 64, height: 45
bitmap0 = bytearray([255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,241,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,255,255,255,255,255,255,255,255,255,
           255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,203,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,156,252,252,254,254,252,0,0,0,192,254,255,255,255,255,255,255,255,255,255,
           255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,241,128,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,192,192,128,0,0,3,7,135,199,207,255,254,144,247,255,255,255,255,255,255,255,255,255,255,255,
           255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,252,252,252,224,0,0,0,0,0,0,0,0,0,0,0,0,31,159,199,3,2,0,2,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
           255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,127,63,31,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,255,1,1,3,7,15,15,31,31,63,63,63,63,63,127,127,127,
           31,15,7,3,7,31,31,31,31,31,31,15,15,7,7,7,3,3,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

# Make a sprite object using bytearray (a path to binary file from 'IMPORT SPRITE' is also valid)
thumbySprite = thumby.Sprite(64, 45, bitmap0)

# Set the FPS (without this call, the default fps is 30)
thumby.display.setFPS(60)
musicCount = 1
def music():
    thumby.audio.play(98, 345)#g
    time.sleep(0.2)
    thumby.audio.stop()
    
    thumby.audio.play(110, 345)#a
    time.sleep(0.2)
    thumby.audio.stop()
    
    
    thumby.audio.play(131, 345)#c
    time.sleep(0.2)
    thumby.audio.stop()
    
    thumby.audio.play(110, 345)#a
    time.sleep(0.2)
    thumby.audio.stop()
    
    thumby.audio.play(165, 345)#e
    time.sleep(0.5)
    thumby.audio.stop()
    
    thumby.audio.play(165, 345)#e
    time.sleep(0.5)
    thumby.audio.stop()
    
    thumby.audio.play(147, 345)#d
    time.sleep(0.5)
    thumby.audio.stop()
    ####
    thumby.audio.play(98, 345)#g
    time.sleep(0.2)
    thumby.audio.stop()
    
    thumby.audio.play(110, 345)#a
    time.sleep(0.2)
    thumby.audio.stop()
    
    thumby.audio.play(131, 345)#c
    time.sleep(0.2)
    thumby.audio.stop()
    
    thumby.audio.play(110, 345)#a
    time.sleep(0.2)
    thumby.audio.stop()
    
    thumby.audio.play(147, 345)#d
    time.sleep(0.5)
    thumby.audio.stop()
    
    thumby.audio.play(147, 345)#d
    time.sleep(0.5)
    thumby.audio.stop()
    
    thumby.audio.play(131, 345)#d
    time.sleep(0.5)
    thumby.audio.stop()
    ##########
    thumby.audio.play(98, 345)#g
    time.sleep(0.2)
    thumby.audio.stop()
    
    thumby.audio.play(110, 345)#a
    time.sleep(0.2)
    thumby.audio.stop()
    
    
    thumby.audio.play(131, 345)#c
    time.sleep(0.2)
    thumby.audio.stop()
    
    thumby.audio.play(110, 345)#a
    time.sleep(0.2)
    thumby.audio.stop()
    
    thumby.audio.play(131, 345)#c
    time.sleep(0.5)
    thumby.audio.stop()
    
    thumby.audio.play(147, 345)#e
    time.sleep(0.5)
    thumby.audio.stop()
    
    thumby.audio.play(123, 345)#B
    time.sleep(0.5)
    thumby.audio.stop()
    
    thumby.audio.play(110, 345)#a
    time.sleep(0.5)
    thumby.audio.stop()
    
    thumby.audio.play(98, 345)#g
    time.sleep(0.2)
    thumby.audio.stop()
    
    thumby.audio.play(98, 345)#g
    time.sleep(0.2)
    thumby.audio.stop()
    
    thumby.audio.play(146, 345)#d
    time.sleep(0.5)
    thumby.audio.stop()

    thumby.audio.play(131, 345)#c
    time.sleep(0.5)
    thumby.audio.stop()

    
    
    
    

while(1):
    t0 = time.ticks_ms()   # Get time (ms)
    thumby.display.fill(0) # Fill canvas to black

    bobRate = 250 # Set arbitrary bob rate (higher is slower)
    bobRange = 0  # How many pixels to move the sprite up/down (-5px ~ 5px)

    # Calculate number of pixels to offset sprite for bob animation
    bobOffset = math.sin(t0 / bobRate) * bobRange

    # Center the sprite using screen and bitmap dimensions and apply bob offset
    thumbySprite.x = int((thumby.display.width/2) - (30))
    thumbySprite.y = int(round((thumby.display.height/2) - (20) + bobOffset))

    # Display the bitmap using bitmap data, position, and bitmap dimensions
    thumby.display.drawSprite(thumbySprite)
    thumby.display.update()
    if musicCount > 0:
        music()  
        musicCount -= 1
