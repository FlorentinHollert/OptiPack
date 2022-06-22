import string
import numpy as np


class article:

    def __init__(self, xyz, rank) -> None:
        xyz.sort(reverse=True)
        self.xyz = xyz
        self.volume = xyz[0] * xyz[1] * xyz[2]
        self.longest_side = max(xyz)
        self.rank = rank

class package:

    def __init__(self, xyz) -> None:
        xyz.sort(reverse=True)
        self.xyz = xyz
        self.volume = xyz[0] * xyz[1] * xyz[2]
        self.longest_side = max(xyz)
        self.coordinates = np.array(xyz[0] * [xyz[1] * [xyz[2] * [0]]])
        self.reference_point = (0, 0, 0)

    def mark_cells(self, mnk, xyz, rank):
        for a in range(mnk[0],mnk[0]+xyz[0]):
            for b in range(mnk[1],mnk[1]+xyz[1]):
                for c in range(mnk[2],mnk[2]+xyz[2]):
                    self.coordinates[a][b][c] = rank
        
    
    def fits_into_package(self, artic) -> bool:
        # length width check
        # update next (x-value), after one iteration (y-value)
        # m->x n->y k->z
        pass


package_large = package([120,60,60])
package_middle = package([60,30,15])
package_small = package([35,25,10])

packages = [package_small, package_middle, package_large]

# rotation matrix
def rotation(artic:article, rot_type:string) -> None:
    if rot_type == "xy":
        artic.xyz = [artic.xyz[1], artic.xyz[0], artic.xyz[2]]
    if rot_type == "xz":
        artic.xyz = [artic.xyz[2], artic.xyz[1], artic.xyz[0]]

# input from image recognition
article1 = article([15,6,18], 1)
article2 = article([11,4,8], 2)
article3 = article([6,13,6], 3)
article4 = article([6,13,6], 4)
article5 = article([11,4,8], 5)
articles = [article1, article2, article3, article4, article5]

def return_longest_side(article):
    return article.longest_side 

# sort by 
articles.sort(key=return_longest_side, reverse=True)
volume_order = 0
for artic in articles:
    volume_order += artic.volume
# program flow
for pack in packages:
    # generell request
    if pack.volume < volume_order:
        if pack.longest_side < articles[0].longest_side:
            packages.remove(pack)
            continue
    for k in range(pack.xyz[2]):
        for n in range(pack.xyz[1]):
            for m in range(pack.xyz[0]):
                if pack.coordinates[m][n][k] == 0:
                    for artic in articles:
                        if artic.xyz[0] <= pack.xyz[0]-m:
                            if artic.xyz[1] <= pack.xyz[1]-n:
                                if artic.xyz[2] <= pack.xyz[2]-k:
                                    pack.mark_cells([m,n,k],artic.xyz, artic.rank)
                                    articles.remove(artic)

for x in packages[0].coordinates:
    for y in x:
        print(str(y[0])+"/", end="")
    print()
print(packages[0].volume)
print("end")



