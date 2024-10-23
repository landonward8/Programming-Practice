from bridges.bridges import *
from bridges.avl_tree_element import *
from AVLTree import AVLTree
import argparse

def useAVLTree(tree_id):

    # get your_user_name and your_key from your profile at http://bridges-cs.herokuapp.com/profile
    your_user_name = "lrw0404"
    your_key = "1707749816574"
    bridges = Bridges(tree_id, your_user_name, your_key)

    avl = AVLTree('tree'+ str(tree_id) + '.txt')

    # add some visual attributes
    avl.root.visualizer.color = "magenta"
    avl.root.visualizer.opacity = 0.8

    # set visualizer type
    bridges.set_data_structure(avl.root)

    # visualize the tree
    bridges.visualize()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='AVL')

    parser.add_argument('-tree', dest='tree_id', required = True, type = int, help='id of the tree')
    args = parser.parse_args()

    # tree_id is 1, 2, 3, or 4
    # Example usage: python useAVLTree.py -tree 1
    useAVLTree(args.tree_id)
