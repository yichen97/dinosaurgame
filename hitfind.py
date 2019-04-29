def hit_find(x1, x2, x3,  x5, y):
    if abs(x1-x2) < 21 and (y <= 205) and (y>180):
        hit = True
        return hit
    if abs(x1-x3) < 21 and (y <= 205) and (y > 180):
        hit = True
        return hit
    if abs(x1 - x5) < 28 and (y <= 153) and (y > 130):
        hit = True
        return hit

