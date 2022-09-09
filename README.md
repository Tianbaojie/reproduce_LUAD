| Parameter | Definition        | Default                        | Remarks            |
|:---------:|:-----------------:|:------------------------------:|:------------------:|
|           | input_path        | Path of trace data             | ./input            |
|           | output_path       | Path of output                 | ./output           |
|           | save_weights      | Save candidates' weight or not | False              |
|           | region_centre     | Location of regions' centers   | ./RegionCenters    |
|           | region_popularity | Popularity of regions          | ./RegionPopularity |
|           | Tmax              | The number of time-bins        | 24\*8              |
|           | scale             | Spatial granularity            | 0.01               |
|           | K                 | Top-K in hit-precision         | 10                 |

1. Run
   
   $ python algorithms/pois.py  --input_path ./algorithms/input/  --output_path ./algorithms/output/ --save_weights False  --region_centre ./algorithms/RegionCenters  --region_popularity ./algorithms/RegionPopularity  --scale 0.01 --K 10
   
   ```bash
   $ python algorithms/pois.py \
    --input_path ./algorithms/input/ \
    --output_path ./algorithms/output/ \
    --save_weights False \
    --region_centre ./algorithms/RegionCenters \
    --region_popularity ./algorithms/RegionPopularity \
    --scale 0.01 \
    --K 10
   ```

数据格式
----------

数据分为fs_example.txt和tt_example.txt分别是foursquare和twitter的轨迹数据，每一行代表一个用户的轨迹。每一行都是如下格式

```bash
101;|3836,963221636|4053,577522790|
```

分号前的字符串是用户 ID。轨迹中的时空点用竖线划分。逗号前的元素是时间的ID，逗号后的元素是binId。

REFERENCES
==========

[WWW 2016] C. Riederer, Y. Kim, A. Chaintreau, N. Korula, and S. Lattanzi, “Linking users across domains with location data: Theory and validation,” in Proc. WWW, 2016.
