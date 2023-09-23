import cx_Freeze

OPTIONS = {"build_exe": {"packages": ["pygame"], 
                         "include_files": ["Explosion.py", "Bullet.py", "Meteor.py", "Player.py", 
                         "spaceInvadersGUI.py", "TekkiePygameLib.py", "img", "sounds" ]}}

EXECUTABLE = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(options=OPTIONS, executables=EXECUTABLE)
