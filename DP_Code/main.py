import os
import numpy as np
import matplotlib.pyplot as plt

totalN = 1798550.0
totalT = 192.0

def main():
    pass


if __name__ == '__main__':
    # region_c_dict:
    # 区域中心表，isp的HashId映射到其经纬度坐标的字典。
    # ispHashId:str -> 'Longitude'_'Latitude':str
    region_c_list = open('./src/RegionCenters', 'r').readlines()
    region_c_dict = dict(
        zip([k.split('_')[0] for k in region_c_list], [
            k.split('_')[1]+'_'+k.split('_')[2] for k in region_c_list]))

    # center_map_dict:
    # 对region_c_dict中的经纬度坐标进行一个范围限制，即设定一个区块而不是具体定位。
    # ispHashId:str -> 'Longitude'-'Latitude':str
    center_map_dict = {}
    for center in region_c_dict:
        loc = region_c_dict[center].split('_')
        new_loc = str(round(float(loc[0]), 2)) + \
            '-' + str(round(float(loc[1]), 2))
        center_map_dict[center] = new_loc

    # region_pop_list:
    # 区域热点表，isp的HashId映射到热度的字典。
    # ispHashId:str -> Popularity:numberic_str
    region_pop_list = open('./src/RegionPopularity', 'r').readlines()
    region_pop_dict = dict(
        zip([k.strip().split()[0] for k in region_pop_list], [k.strip().split()[1] for k in region_pop_list]))
    
    # region_mapped_count:
    # 映射区域化的经纬度到到区域热度。
    region_mapped_count = dict()
    for region in center_map_dict:
        if region not in region_pop_dict:
            continue
        region_mapped = center_map_dict[region]
        print(region_mapped)
        if region_mapped in region_mapped_count:
            region_mapped_count[region_mapped] += int(region_pop_dict[region])
        else:
            region_mapped_count[region_mapped] = int(region_pop_dict[region])
    
    region_p_dict = region_mapped_count
    for k in region_p_dict:
        region_p_dict[k] = region_p_dict[k] * 1.0 / (totalN * totalT)
    

