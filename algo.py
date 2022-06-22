import string
import numpy as np


class article:

    def __init__(self, xyz) -> None:
        self.xyz = xyz.sort(reverse=True)
        self.volume = xyz[0] * xyz[1] * xyz[2]
        self.longest_side = max(xyz)

class package:

    def __init__(self, xyz) -> None:
        self.xyz = xyz.sort(reverse=True)
        self.volume = xyz[0] * xyz[1] * xyz[2]
        self.longest_side = max(xyz)
        self.coordinates = np.array([xyz[0],xyz[1],xyz[2]])
        self.reference_point = (0, 0, 0)
        self.articles = np.array()

    
    def fits_into_package(self, artic) -> bool:
        # length width check
        # update next (x-value), after one iteration (y-value)
        four_edge_points = self.reference_point + artic.xyz
        # Check outside of package
        if any(four_edge_points > self.xyz):
            return False
        # Check for each article already in package
        for artic in self.articles:
            if four_edge_points in artic:
                pass
                

packages_list = [package([120,70,40])]

# rotation matrix
def rotation(artic:article, rot_type:string) -> None:
    if rot_type == "xy":
        artic.xyz = [artic.xyz[1], artic.xyz[0], artic.xyz[2]]
    if rot_type == "xz":
        artic.xyz = [artic.xyz[2], artic.xyz[1], artic.xyz[0]]

# input from image recognition
articles = list()

def return_longest_side(article):
    return article.longest_side 

# sort by 
articles.sort(key=return_longest_side, reverse=True)
volume_order = sum(articles.volume)


# program flow
for pack in packages_list:

    # generell request
    if pack.volume < volume_order or pack.longest_side < articles[0].longest_side:
        continue
    
    # check one after the other
    for artic in articles:

        if package.fits_into_package(artic):
            # overwrite white boxes
            pass
        else:
            #rotation
            pass