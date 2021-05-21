from dirsync import sync
from secrets import game_sync_secrets

print("Sync start")
# this is sort of like a config file right
# since you can just change these values welp
sourcedir = "C:\\Users\\Will Jones\\Documents\\Saved Games\\Hades"
targetdir = "C:\\Users\\Will Jones\\OneDrive\\Documents\\Saved Games\\Hades"
action = "update"

sync(sourcedir,targetdir,action,verbose=True,twoway=True)

print("Sync complete! Press any key to continue.")
input()