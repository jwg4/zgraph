# zgraph

This is a Python library for creating STL files of 3d graphs. An STL file is input to a 3d printer or similar.

Currently there is only one class for external use: ZGraph. This class will create an stl.Solid of a 3d graph, 
given a function z(x,y) and a range for x and y. The stl.Solid object comes from the stl library, and has methods 
to write the facet data to a file.
