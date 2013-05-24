wordexplorer
============

Interactively explore a text document using word trees

After listening to a presentation by Martin Wattenberg and Fernanda Viegas at the "Visualization: From Data To Discovery" symposium held at the California Institute of Technology on May 23, 2013, I was inspired to learn a bit more about Word Trees (see the duo's [2008 paper](http://hint.fm/papers/wordtree_final2.pdf) on the subject, and the original [project page](http://hint.fm/projects/wordtree)). I found a [great javascript implementation](https://github.com/silverasm/wordtree) that utilizes [Raphael.js](http://raphaeljs.com) to render the visualizations. I wrote a quick parser in Python to generate the JSON data structure needed to represent the tree structure and whipped up a simple interface to allow for search. 

This is a work in progress, with no particular goal at the moment -- just playing around with the concept. Right now the parser looks at 1-grams (individual words) only, so the search is limited to single words (i.e.: searches like "she saw" or "climate research" are not supported)...yet.
