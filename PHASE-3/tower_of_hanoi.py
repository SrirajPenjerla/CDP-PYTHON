def moveDisks(n,src,ex,dt):
    if n == 1:
        print(f"Move first disk from {src} to {dt} ")
        return 
    moveDisks(n-1,src,dt,ex)
    print(f"Move {n}th disk from {src} to {dt}")
    moveDisks(n-1,ex,src,dt)

moveDisks(15,"source","extraSpace","Destinatiom")