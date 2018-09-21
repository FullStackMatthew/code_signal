def growingPlant(upSpeed, downSpeed, desiredHeight):
    if(desiredHeight <= upSpeed):
        return 1
    return (desiredHeight - upSpeed - 1) // (upSpeed - downSpeed) + 2