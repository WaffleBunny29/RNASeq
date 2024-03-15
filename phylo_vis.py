#!/usr/bin/env python3

from Bio import AlignIO
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator 
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from phytreeviz import TreeViz

infile = open('multiple_sequence.aln','r')
aligned = AlignIO.read(infile,'clustal')

calculator = DistanceCalculator('identity')
distance_matrix = calculator.get_distance(aligned)

constructor = DistanceTreeConstructor(calculator,'nj')
tree = constructor.build_tree(aligned)

Phylo.draw_ascii(tree)
Phylo.write(tree, "tree.nwk", "newick")

treefile = Phylo.read("tree.nwk","newick")

tv = TreeViz(treefile, align_leaf_label=True)
tv.show_scale_axis()

group = ["ATCC_19977", "MAB_4395"]

tv.highlight(group, "orange")
tv.annotate(group, "Group")

tv.marker(group, marker="s", color="blue", descendent=True)
tv.marker("AGQU01000001.1", color="red")

tv.savefig("tree.png", dpi=300)

infile.close()