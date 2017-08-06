# spacefill
spacefill is a [Python](http://www.python.org) library to generate space filling curves. 
This library is targeted for a more practical use and allows you to generate curves to fit your data.

Currently you can create a 2d space filling curve filling a shape of width x height.

This library is inspired by this demo: [Space filling curves](http://lutanho.net/pic2html/draw_sfc.html)
This demo is created by Lutz Tautenhahn

## Usage
Import the library first
```python
import spacefill.curvetools as curvetools
```

Generate a curve map. This can be stored so you dont have to generate it again. A curve map is a list of subsequent coordinates.
```python
>> curve_map = curvetools.generate_map(64, 48)
```

Get a position on the curve by its coordinate:
```python
>> point = curvetools.coord_to_position((25, 25), curve_map)
0.48518397915988276
```

Get a coordinate on the curve by its position:
```python
>> coordinate = curvetools.position_to_coord(point, curve_map)
(25.0, 25.0)
```

![Example space 64x48](https://raw.githubusercontent.com/EgorDm/spacefill/master/examples/Example1.png)


Thats basically it. More functions will be added soon.

## License
spacefill is licensed under the MIT License.