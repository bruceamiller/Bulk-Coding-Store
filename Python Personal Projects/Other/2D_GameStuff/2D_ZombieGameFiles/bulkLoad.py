from ObjectClasses_2D import *

def loadMapInfo():


    """ FLOOR"""
    objects = []
    objects.append(Floor([-925, -1175], [1000, -425], "green4"))
    #floorObjects.append(Floor([-925, -425], [1000, 875], "grey39")) #House Foundation
    #floorObjects.append(Floor([-200, -200], [500, 500], "brown")) #Living Room Carpet
    #floorObjects.append(Floor([-900, 150], [-200, 850], "grey33")) #Garage Floor
    #floorObjects.append(Floor([-750, -400], [-200, 150], "orange4")) #Bedroom Floor
    #floorObjects.append(Floor([-900, -400], [-750, 150], "grey5")) #Master Bathroom
    #floorObjects.append(Floor([500, -200], [900, 200], "saddle brown")) #Dining Room Floor
    #floorObjects.append(Floor([500, 200], [900, 600], "thistle1")) #Kitchen Floor
    #floorObjects.append(Floor([500, 600], [900, 850], "grey33")) #Storage
    #floorObjects.append(Floor([150, 500], [500, 850], "grey5")) #Front Bathroom
    backgroundImage = pygame.image.load(r"C:\Users\Bruce\Desktop\Python Coding\Personal Projects\Other\2D_GameStuff\2D_ZombieGameFiles\Images\HouseDrawn.png").convert()
    backgroundFloorObject = Floor([-940.5, -438], [0,0])
    backgroundFloorObject.setImage(backgroundImage)
    objects.append(backgroundFloorObject)


    """ WALLS """
    walls = [Wall([-550, -400], width = 700),
            Wall([-550, 150], width = 700),
            Wall([-550, 850], width = 700),
            Wall([-5, -200], width = 380),
            Wall([620, -200], width = 560),
            Wall([540, 200], width = 80),
            Wall([860, 200], width = 100),
            Wall([-155, 500], width = 90),
            Wall([265, 500], width = 460),
            Wall([525, 850], width = 750),
            Wall([520, 600], width = 60),
            Wall([780, 600], width = 250),
            Wall([-900, 225], height = 1250),
            Wall([-750, -125], height = 540),
            Wall([-200, 150], height = 220),
            Wall([-200, -240], height = 320),
            Wall([-200, 610], height = 470),
            Wall([150, 675], height = 350),
            Wall([500, 630], height = 440),
            Wall([495, 210], height = 150),
            Wall([495, -85], height = 230),
            Wall([905, 325], height = 1050)]
    roomBarriers = [Wall([325, 675], 350, 350),
                    Wall([-825, -125], 150, 550)]
    for wall in roomBarriers:
        wall.setColor("black")
        walls.insert(0, wall)
    interactableObjects = [Wall([-705, 45], 60, 140),
                        Wall([-755, 210], 190, 60),
                        Wall([440, -85], 60, 180),
                        Wall([670, -245], 165, 60),
                        Wall([660, -140], 240, 60),
                        Wall([870, 285], 45, 110),
                        Wall([845, 780], 60, 95)]
    for i in interactableObjects:
        i.setColor(None)
    walls.extend(interactableObjects)
    objects.extend(walls)

    return walls, objects

def loadWeapons():
    weapons = []

    weapons.append(Weapon("pistol"))

    shotgun = Weapon("shotgun")
    shotgun.setDamage(20)
    shotgun.setSpread(150)
    shotgun.setBurst(10)
    shotgun.setRange(50)
    shotgun.setSpreadVariation(10)
    shotgun.setBulletsPerSecond(2)
    weapons.append(shotgun)

    machineGun = Weapon("machine gun")
    machineGun.setDamage(15)
    machineGun.setSpread(0.2)
    machineGun.setBulletsPerSecond(4)
    machineGun.setSemiAuto(False)
    machineGun.setMagSize(30)
    machineGun.setMaxAmmo(300)
    machineGun.setReloadSpeed(1.5)
    weapons.append(machineGun)


    return weapons

