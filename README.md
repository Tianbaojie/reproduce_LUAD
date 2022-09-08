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

Example
----------

在这个例子中，第一行data_example代表外部轨迹

```bash
user_000001;|163,31.7324327_120.9655657|181,31.7324327_120.9655657|
```

分号前的字符串是用户 ID。轨迹中的时空点用竖线划分。逗号前的元素是时间的ID，逗号后的元素是纬度和经度。

从第二行到最后一行是bin轨迹，其中一个例子是：

```bash
user_000010;|163,fe4c21d14228bd83d838ee6562332c0b|
```

与外部轨迹不同，bin 轨迹中的位置bin ID 表示。bin中心的地理坐标可以在**algorithm\RegionCenters**中找到。

`algorithms/output/result` 是得到的结果。 `result` 中有一行，两个字段由 "\t" 分隔。 第一个字段是输入文件的名称。 第二个字段是hit_acc@k。

**其他**

1. **RegionPopularity **给出每个区域的访问日志总数。

REFERENCES
==========

[NDSS 2018]  H. Wang, C. Gao, Y. Li, G. Wang, D. Jin, J. Sun, "De-anonymization of Mobility Trajectories: Dissecting the Gaps between Theory and Practice," in Proc. NDSS, 2018.

[WWW 2016] C. Riederer, Y. Kim, A. Chaintreau, N. Korula, and S. Lattanzi, “Linking users across domains with location data: Theory and validation,” in Proc. WWW, 2016.
