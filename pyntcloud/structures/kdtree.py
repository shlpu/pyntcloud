from scipy.spatial import cKDTree

from .base import Structure


class KDTree(cKDTree, Structure):

    def __init__(self, PyntCloud, leafsize=16, compact_nodes=False, balanced_tree=False):
        cKDTree.__init__(
            self,
            PyntCloud.xyz,
            leafsize=leafsize,
            compact_nodes=compact_nodes,
            balanced_tree=balanced_tree)
        Structure.__init__(self, PyntCloud)
        self.id = "K({},{},{})".format(leafsize, compact_nodes, balanced_tree)

    def extract_info(self):
        pass

    def compute(self):
        pass
