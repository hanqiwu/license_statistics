# -*- coding: utf-8 -*-
import sys,getopt
import re
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

List_00_05 = []
List_00_10 = []
List_00_15 = []
List_00_20 = []
List_00_25 = []
List_00_30 = []
List_00_35 = []
List_00_40 = []
List_00_45 = []
List_00_50 = []
List_00_55 = []
List_01_00 = []
List_01_05 = []
List_01_10 = []
List_01_15 = []
List_01_20 = []
List_01_25 = []
List_01_30 = []
List_01_35 = []
List_01_40 = []
List_01_45 = []
List_01_50 = []
List_01_55 = []
List_02_00 = []
List_02_05 = []
List_02_10 = []
List_02_15 = []
List_02_20 = []
List_02_25 = []
List_02_30 = []
List_02_35 = []
List_02_40 = []
List_02_45 = []
List_02_50 = []
List_02_55 = []
List_03_00 = []
List_03_05 = []
List_03_10 = []
List_03_15 = []
List_03_20 = []
List_03_25 = []
List_03_30 = []
List_03_35 = []
List_03_40 = []
List_03_45 = []
List_03_50 = []
List_03_55 = []
List_04_00 = []
List_04_05 = []
List_04_10 = []
List_04_15 = []
List_04_20 = []
List_04_25 = []
List_04_30 = []
List_04_35 = []
List_04_40 = []
List_04_45 = []
List_04_50 = []
List_04_55 = []
List_05_00 = []
List_05_05 = []
List_05_10 = []
List_05_15 = []
List_05_20 = []
List_05_25 = []
List_05_30 = []
List_05_35 = []
List_05_40 = []
List_05_45 = []
List_05_50 = []
List_05_55 = []
List_06_00 = []
List_06_05 = []
List_06_10 = []
List_06_15 = []
List_06_20 = []
List_06_25 = []
List_06_30 = []
List_06_35 = []
List_06_40 = []
List_06_45 = []
List_06_50 = []
List_06_55 = []
List_07_00 = []
List_07_05 = []
List_07_10 = []
List_07_15 = []
List_07_20 = []
List_07_25 = []
List_07_30 = []
List_07_35 = []
List_07_40 = []
List_07_45 = []
List_07_50 = []
List_07_55 = []
List_08_00 = []
List_08_05 = []
List_08_10 = []
List_08_15 = []
List_08_20 = []
List_08_25 = []
List_08_30 = []
List_08_35 = []
List_08_40 = []
List_08_45 = []
List_08_50 = []
List_08_55 = []
List_09_00 = []
List_09_05 = []
List_09_10 = []
List_09_15 = []
List_09_20 = []
List_09_25 = []
List_09_30 = []
List_09_35 = []
List_09_40 = []
List_09_45 = []
List_09_50 = []
List_09_55 = []
List_10_00 = []
List_10_05 = []
List_10_10 = []
List_10_15 = []
List_10_20 = []
List_10_25 = []
List_10_30 = []
List_10_35 = []
List_10_40 = []
List_10_45 = []
List_10_50 = []
List_10_55 = []
List_11_00 = []
List_11_05 = []
List_11_10 = []
List_11_15 = []
List_11_20 = []
List_11_25 = []
List_11_30 = []
List_11_35 = []
List_11_40 = []
List_11_45 = []
List_11_50 = []
List_11_55 = []
List_12_00 = []
List_12_05 = []
List_12_10 = []
List_12_15 = []
List_12_20 = []
List_12_25 = []
List_12_30 = []
List_12_35 = []
List_12_40 = []
List_12_45 = []
List_12_50 = []
List_12_55 = []
List_13_00 = []
List_13_05 = []
List_13_10 = []
List_13_15 = []
List_13_20 = []
List_13_25 = []
List_13_30 = []
List_13_35 = []
List_13_40 = []
List_13_45 = []
List_13_50 = []
List_13_55 = []
List_14_00 = []
List_14_05 = []
List_14_10 = []
List_14_15 = []
List_14_20 = []
List_14_25 = []
List_14_30 = []
List_14_35 = []
List_14_40 = []
List_14_45 = []
List_14_50 = []
List_14_55 = []
List_15_00 = []
List_15_05 = []
List_15_10 = []
List_15_15 = []
List_15_20 = []
List_15_25 = []
List_15_30 = []
List_15_35 = []
List_15_40 = []
List_15_45 = []
List_15_50 = []
List_15_55 = []
List_16_00 = []
List_16_05 = []
List_16_10 = []
List_16_15 = []
List_16_20 = []
List_16_25 = []
List_16_30 = []
List_16_35 = []
List_16_40 = []
List_16_45 = []
List_16_50 = []
List_16_55 = []
List_17_00 = []
List_17_05 = []
List_17_10 = []
List_17_15 = []
List_17_20 = []
List_17_25 = []
List_17_30 = []
List_17_35 = []
List_17_40 = []
List_17_45 = []
List_17_50 = []
List_17_55 = []
List_18_00 = []
List_18_05 = []
List_18_10 = []
List_18_15 = []
List_18_20 = []
List_18_25 = []
List_18_30 = []
List_18_35 = []
List_18_40 = []
List_18_45 = []
List_18_50 = []
List_18_55 = []
List_19_00 = []
List_19_05 = []
List_19_10 = []
List_19_15 = []
List_19_20 = []
List_19_25 = []
List_19_30 = []
List_19_35 = []
List_19_40 = []
List_19_45 = []
List_19_50 = []
List_19_55 = []
List_20_00 = []
List_20_05 = []
List_20_10 = []
List_20_15 = []
List_20_20 = []
List_20_25 = []
List_20_30 = []
List_20_35 = []
List_20_40 = []
List_20_45 = []
List_20_50 = []
List_20_55 = []
List_21_00 = []
List_21_05 = []
List_21_10 = []
List_21_15 = []
List_21_20 = []
List_21_25 = []
List_21_30 = []
List_21_35 = []
List_21_40 = []
List_21_45 = []
List_21_50 = []
List_21_55 = []
List_22_00 = []
List_22_05 = []
List_22_10 = []
List_22_15 = []
List_22_20 = []
List_22_25 = []
List_22_30 = []
List_22_35 = []
List_22_40 = []
List_22_45 = []
List_22_50 = []
List_22_55 = []
List_23_00 = []
List_23_05 = []
List_23_10 = []
List_23_15 = []
List_23_20 = []
List_23_25 = []
List_23_30 = []
List_23_35 = []
List_23_40 = []
List_23_45 = []
List_23_50 = []
List_23_55 = []
List_24_00 = []

List_set = [List_00_05, List_00_10, List_00_15, List_00_20, List_00_25, List_00_30, List_00_35, List_00_40, List_00_45, List_00_50, List_00_55, List_01_00, List_01_05, List_01_10, List_01_15, List_01_20, List_01_25, List_01_30, List_01_35, List_01_40, List_01_45, List_01_50, List_01_55, List_02_00, List_02_05, List_02_10, List_02_15, List_02_20, List_02_25, List_02_30, List_02_35, List_02_40, List_02_45, List_02_50, List_02_55, List_03_00, List_03_05, List_03_10, List_03_15, List_03_20, List_03_25, List_03_30, List_03_35, List_03_40, List_03_45, List_03_50, List_03_55, List_04_00, List_04_05, List_04_10, List_04_15, List_04_20, List_04_25, List_04_30, List_04_35, List_04_40, List_04_45, List_04_50, List_04_55, List_05_00, List_05_05, List_05_10, List_05_15, List_05_20, List_05_25, List_05_30, List_05_35, List_05_40, List_05_45, List_05_50, List_05_55, List_06_00, List_06_05, List_06_10, List_06_15, List_06_20, List_06_25, List_06_30, List_06_35, List_06_40, List_06_45, List_06_50, List_06_55, List_07_00, List_07_05, List_07_10, List_07_15, List_07_20, List_07_25, List_07_30, List_07_35, List_07_40, List_07_45, List_07_50, List_07_55, List_08_00, List_08_05, List_08_10, List_08_15, List_08_20, List_08_25, List_08_30, List_08_35, List_08_40, List_08_45, List_08_50, List_08_55, List_09_00, List_09_05, List_09_10, List_09_15, List_09_20, List_09_25, List_09_30, List_09_35, List_09_40, List_09_45, List_09_50, List_09_55, List_10_00, List_10_05, List_10_10, List_10_15, List_10_20, List_10_25, List_10_30, List_10_35, List_10_40, List_10_45, List_10_50, List_10_55, List_11_00, List_11_05, List_11_10, List_11_15, List_11_20, List_11_25, List_11_30, List_11_35, List_11_40, List_11_45, List_11_50, List_11_55, List_12_00, List_12_05, List_12_10, List_12_15, List_12_20, List_12_25, List_12_30, List_12_35, List_12_40, List_12_45, List_12_50, List_12_55, List_13_00, List_13_05, List_13_10, List_13_15, List_13_20, List_13_25, List_13_30, List_13_35, List_13_40, List_13_45, List_13_50, List_13_55, List_14_00, List_14_05, List_14_10, List_14_15, List_14_20, List_14_25, List_14_30, List_14_35, List_14_40, List_14_45, List_14_50, List_14_55, List_15_00, List_15_05, List_15_10, List_15_15, List_15_20, List_15_25, List_15_30, List_15_35, List_15_40, List_15_45, List_15_50, List_15_55, List_16_00, List_16_05, List_16_10, List_16_15, List_16_20, List_16_25, List_16_30, List_16_35, List_16_40, List_16_45, List_16_50, List_16_55, List_17_00, List_17_05, List_17_10, List_17_15, List_17_20, List_17_25, List_17_30, List_17_35, List_17_40, List_17_45, List_17_50, List_17_55, List_18_00, List_18_05, List_18_10, List_18_15, List_18_20, List_18_25, List_18_30, List_18_35, List_18_40, List_18_45, List_18_50, List_18_55, List_19_00, List_19_05, List_19_10, List_19_15, List_19_20, List_19_25, List_19_30, List_19_35, List_19_40, List_19_45, List_19_50, List_19_55, List_20_00, List_20_05, List_20_10, List_20_15, List_20_20, List_20_25, List_20_30, List_20_35, List_20_40, List_20_45, List_20_50, List_20_55, List_21_00, List_21_05, List_21_10, List_21_15, List_21_20, List_21_25, List_21_30, List_21_35, List_21_40, List_21_45, List_21_50, List_21_55, List_22_00, List_22_05, List_22_10, List_22_15, List_22_20, List_22_25, List_22_30, List_22_35, List_22_40, List_22_45, List_22_50, List_22_55, List_23_00, List_23_05, List_23_10, List_23_15, List_23_20, List_23_25, List_23_30, List_23_35, List_23_40, List_23_45, List_23_50, List_23_55, List_24_00]

# print(len(List_set))


def usage():
    print("Usage:")
    print("")
    print("python license-sta.py -s [file path]")


def version():
    print(1.01)


def license_statis(log_file):
    with open(log_file, "r") as file:
        for num, line in enumerate(file):
            findstr = re.findall(r'(\d+:\d\d:\d\d)\s+\(metrowks\)\s\w+:\s"\w+"\s(\w\S+@\w\S+)', line)
            if findstr:
                temp = list(findstr[0])
                temp = findstr[0]
                if len(temp[0]) == 7:
                    templist = ["0" + temp[0], temp[1]]
                    temp = templist
                list_id = 0
                if '00:00:00' <= temp[0] <= '00:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '00:05:00' < temp[0] <= '00:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '00:10:00' < temp[0] <= '00:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '00:15:00' < temp[0] <= '00:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '00:20:00' < temp[0] <= '00:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '00:25:00' < temp[0] <= '00:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '00:30:00' < temp[0] <= '00:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '00:35:00' < temp[0] <= '00:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '00:40:00' < temp[0] <= '00:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '00:45:00' < temp[0] <= '00:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '00:50:00' < temp[0] <= '00:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '00:55:00' < temp[0] <= '01:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '01:00:00' < temp[0] <= '01:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '01:05:00' < temp[0] <= '01:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '01:10:00' < temp[0] <= '01:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '01:15:00' < temp[0] <= '01:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '01:20:00' < temp[0] <= '01:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '01:25:00' < temp[0] <= '01:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '01:30:00' < temp[0] <= '01:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '01:35:00' < temp[0] <= '01:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '01:40:00' < temp[0] <= '01:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '01:45:00' < temp[0] <= '01:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '01:50:00' < temp[0] <= '01:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '01:55:00' < temp[0] <= '02:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '02:00:00' < temp[0] <= '02:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '02:05:00' < temp[0] <= '02:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '02:10:00' < temp[0] <= '02:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '02:15:00' < temp[0] <= '02:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '02:20:00' < temp[0] <= '02:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '02:25:00' < temp[0] <= '02:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '02:30:00' < temp[0] <= '02:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '02:35:00' < temp[0] <= '02:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '02:40:00' < temp[0] <= '02:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '02:45:00' < temp[0] <= '02:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '02:50:00' < temp[0] <= '02:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '02:55:00' < temp[0] <= '03:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '03:00:00' < temp[0] <= '03:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '03:05:00' < temp[0] <= '03:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '03:10:00' < temp[0] <= '03:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '03:15:00' < temp[0] <= '03:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '03:20:00' < temp[0] <= '03:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '03:25:00' < temp[0] <= '03:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '03:30:00' < temp[0] <= '03:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '03:35:00' < temp[0] <= '03:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '03:40:00' < temp[0] <= '03:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '03:45:00' < temp[0] <= '03:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '03:50:00' < temp[0] <= '03:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '03:55:00' < temp[0] <= '04:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '04:00:00' < temp[0] <= '04:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '04:05:00' < temp[0] <= '04:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '04:10:00' < temp[0] <= '04:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '04:15:00' < temp[0] <= '04:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '04:20:00' < temp[0] <= '04:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '04:25:00' < temp[0] <= '04:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '04:30:00' < temp[0] <= '04:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '04:35:00' < temp[0] <= '04:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '04:40:00' < temp[0] <= '04:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '04:45:00' < temp[0] <= '04:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '04:50:00' < temp[0] <= '04:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '04:55:00' < temp[0] <= '05:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '05:00:00' < temp[0] <= '05:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '05:05:00' < temp[0] <= '05:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '05:10:00' < temp[0] <= '05:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '05:15:00' < temp[0] <= '05:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '05:20:00' < temp[0] <= '05:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '05:25:00' < temp[0] <= '05:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '05:30:00' < temp[0] <= '05:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '05:35:00' < temp[0] <= '05:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '05:40:00' < temp[0] <= '05:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '05:45:00' < temp[0] <= '05:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '05:50:00' < temp[0] <= '05:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '05:55:00' < temp[0] <= '06:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '06:00:00' < temp[0] <= '06:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '06:05:00' < temp[0] <= '06:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '06:10:00' < temp[0] <= '06:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '06:15:00' < temp[0] <= '06:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '06:20:00' < temp[0] <= '06:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '06:25:00' < temp[0] <= '06:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '06:30:00' < temp[0] <= '06:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '06:35:00' < temp[0] <= '06:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '06:40:00' < temp[0] <= '06:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '06:45:00' < temp[0] <= '06:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '06:50:00' < temp[0] <= '06:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '06:55:00' < temp[0] <= '07:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '07:00:00' < temp[0] <= '07:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '07:05:00' < temp[0] <= '07:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '07:10:00' < temp[0] <= '07:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '07:15:00' < temp[0] <= '07:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '07:20:00' < temp[0] <= '07:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '07:25:00' < temp[0] <= '07:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '07:30:00' < temp[0] <= '07:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '07:35:00' < temp[0] <= '07:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '07:40:00' < temp[0] <= '07:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '07:45:00' < temp[0] <= '07:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '07:50:00' < temp[0] <= '07:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '07:55:00' < temp[0] <= '08:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '08:00:00' < temp[0] <= '08:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '08:05:00' < temp[0] <= '08:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '08:10:00' < temp[0] <= '08:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '08:15:00' < temp[0] <= '08:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '08:20:00' < temp[0] <= '08:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '08:25:00' < temp[0] <= '08:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '08:30:00' < temp[0] <= '08:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '08:35:00' < temp[0] <= '08:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '08:40:00' < temp[0] <= '08:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '08:45:00' < temp[0] <= '08:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '08:50:00' < temp[0] <= '08:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '08:55:00' < temp[0] <= '09:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '09:00:00' < temp[0] <= '09:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '09:05:00' < temp[0] <= '09:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '09:10:00' < temp[0] <= '09:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '09:15:00' < temp[0] <= '09:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '09:20:00' < temp[0] <= '09:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '09:25:00' < temp[0] <= '09:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '09:30:00' < temp[0] <= '09:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '09:35:00' < temp[0] <= '09:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '09:40:00' < temp[0] <= '09:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '09:45:00' < temp[0] <= '09:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '09:50:00' < temp[0] <= '09:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '09:55:00' < temp[0] <= '10:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '10:00:00' < temp[0] <= '10:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '10:05:00' < temp[0] <= '10:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '10:10:00' < temp[0] <= '10:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '10:15:00' < temp[0] <= '10:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '10:20:00' < temp[0] <= '10:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '10:25:00' < temp[0] <= '10:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '10:30:00' < temp[0] <= '10:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '10:35:00' < temp[0] <= '10:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '10:40:00' < temp[0] <= '10:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '10:45:00' < temp[0] <= '10:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '10:50:00' < temp[0] <= '10:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '10:55:00' < temp[0] <= '11:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '11:00:00' < temp[0] <= '11:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '11:05:00' < temp[0] <= '11:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '11:10:00' < temp[0] <= '11:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '11:15:00' < temp[0] <= '11:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '11:20:00' < temp[0] <= '11:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '11:25:00' < temp[0] <= '11:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '11:30:00' < temp[0] <= '11:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '11:35:00' < temp[0] <= '11:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '11:40:00' < temp[0] <= '11:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '11:45:00' < temp[0] <= '11:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '11:50:00' < temp[0] <= '11:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '11:55:00' < temp[0] <= '12:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '12:00:00' < temp[0] <= '12:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '12:05:00' < temp[0] <= '12:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '12:10:00' < temp[0] <= '12:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '12:15:00' < temp[0] <= '12:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '12:20:00' < temp[0] <= '12:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '12:25:00' < temp[0] <= '12:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '12:30:00' < temp[0] <= '12:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '12:35:00' < temp[0] <= '12:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '12:40:00' < temp[0] <= '12:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '12:45:00' < temp[0] <= '12:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '12:50:00' < temp[0] <= '12:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '12:55:00' < temp[0] <= '13:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '13:00:00' < temp[0] <= '13:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '13:05:00' < temp[0] <= '13:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '13:10:00' < temp[0] <= '13:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '13:15:00' < temp[0] <= '13:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '13:20:00' < temp[0] <= '13:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '13:25:00' < temp[0] <= '13:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '13:30:00' < temp[0] <= '13:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '13:35:00' < temp[0] <= '13:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '13:40:00' < temp[0] <= '13:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '13:45:00' < temp[0] <= '13:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '13:50:00' < temp[0] <= '13:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '13:55:00' < temp[0] <= '14:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '14:00:00' < temp[0] <= '14:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '14:05:00' < temp[0] <= '14:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '14:10:00' < temp[0] <= '14:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '14:15:00' < temp[0] <= '14:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '14:20:00' < temp[0] <= '14:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '14:25:00' < temp[0] <= '14:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '14:30:00' < temp[0] <= '14:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '14:35:00' < temp[0] <= '14:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '14:40:00' < temp[0] <= '14:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '14:45:00' < temp[0] <= '14:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '14:50:00' < temp[0] <= '14:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '14:55:00' < temp[0] <= '15:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '15:00:00' < temp[0] <= '15:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '15:05:00' < temp[0] <= '15:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '15:10:00' < temp[0] <= '15:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '15:15:00' < temp[0] <= '15:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '15:20:00' < temp[0] <= '15:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '15:25:00' < temp[0] <= '15:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '15:30:00' < temp[0] <= '15:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '15:35:00' < temp[0] <= '15:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '15:40:00' < temp[0] <= '15:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '15:45:00' < temp[0] <= '15:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '15:50:00' < temp[0] <= '15:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '15:55:00' < temp[0] <= '16:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '16:00:00' < temp[0] <= '16:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '16:05:00' < temp[0] <= '16:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '16:10:00' < temp[0] <= '16:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '16:15:00' < temp[0] <= '16:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '16:20:00' < temp[0] <= '16:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '16:25:00' < temp[0] <= '16:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '16:30:00' < temp[0] <= '16:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '16:35:00' < temp[0] <= '16:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '16:40:00' < temp[0] <= '16:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '16:45:00' < temp[0] <= '16:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '16:50:00' < temp[0] <= '16:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '16:55:00' < temp[0] <= '17:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '17:00:00' < temp[0] <= '17:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '17:05:00' < temp[0] <= '17:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '17:10:00' < temp[0] <= '17:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '17:15:00' < temp[0] <= '17:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '17:20:00' < temp[0] <= '17:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '17:25:00' < temp[0] <= '17:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '17:30:00' < temp[0] <= '17:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '17:35:00' < temp[0] <= '17:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '17:40:00' < temp[0] <= '17:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '17:45:00' < temp[0] <= '17:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '17:50:00' < temp[0] <= '17:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '17:55:00' < temp[0] <= '18:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '18:00:00' < temp[0] <= '18:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '18:05:00' < temp[0] <= '18:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '18:10:00' < temp[0] <= '18:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '18:15:00' < temp[0] <= '18:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '18:20:00' < temp[0] <= '18:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '18:25:00' < temp[0] <= '18:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '18:30:00' < temp[0] <= '18:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '18:35:00' < temp[0] <= '18:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '18:40:00' < temp[0] <= '18:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '18:45:00' < temp[0] <= '18:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '18:50:00' < temp[0] <= '18:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '18:55:00' < temp[0] <= '19:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '19:00:00' < temp[0] <= '19:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '19:05:00' < temp[0] <= '19:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '19:10:00' < temp[0] <= '19:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '19:15:00' < temp[0] <= '19:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '19:20:00' < temp[0] <= '19:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '19:25:00' < temp[0] <= '19:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '19:30:00' < temp[0] <= '19:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '19:35:00' < temp[0] <= '19:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '19:40:00' < temp[0] <= '19:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '19:45:00' < temp[0] <= '19:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '19:50:00' < temp[0] <= '19:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '19:55:00' < temp[0] <= '20:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '20:00:00' < temp[0] <= '20:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '20:05:00' < temp[0] <= '20:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '20:10:00' < temp[0] <= '20:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '20:15:00' < temp[0] <= '20:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '20:20:00' < temp[0] <= '20:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '20:25:00' < temp[0] <= '20:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '20:30:00' < temp[0] <= '20:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '20:35:00' < temp[0] <= '20:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '20:40:00' < temp[0] <= '20:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '20:45:00' < temp[0] <= '20:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '20:50:00' < temp[0] <= '20:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '20:55:00' < temp[0] <= '21:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '21:00:00' < temp[0] <= '21:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '21:05:00' < temp[0] <= '21:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '21:10:00' < temp[0] <= '21:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '21:15:00' < temp[0] <= '21:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '21:20:00' < temp[0] <= '21:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '21:25:00' < temp[0] <= '21:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '21:30:00' < temp[0] <= '21:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '21:35:00' < temp[0] <= '21:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '21:40:00' < temp[0] <= '21:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '21:45:00' < temp[0] <= '21:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '21:50:00' < temp[0] <= '21:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '21:55:00' < temp[0] <= '22:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '22:00:00' < temp[0] <= '22:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '22:05:00' < temp[0] <= '22:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '22:10:00' < temp[0] <= '22:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '22:15:00' < temp[0] <= '22:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '22:20:00' < temp[0] <= '22:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '22:25:00' < temp[0] <= '22:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '22:30:00' < temp[0] <= '22:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '22:35:00' < temp[0] <= '22:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '22:40:00' < temp[0] <= '22:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '22:45:00' < temp[0] <= '22:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '22:50:00' < temp[0] <= '22:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '22:55:00' < temp[0] <= '23:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '23:00:00' < temp[0] <= '23:05:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '23:05:00' < temp[0] <= '23:10:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '23:10:00' < temp[0] <= '23:15:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '23:15:00' < temp[0] <= '23:20:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '23:20:00' < temp[0] <= '23:25:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '23:25:00' < temp[0] <= '23:30:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '23:30:00' < temp[0] <= '23:35:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '23:35:00' < temp[0] <= '23:40:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '23:40:00' < temp[0] <= '23:45:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '23:45:00' < temp[0] <= '23:50:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '23:50:00' < temp[0] <= '23:55:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1

                if '23:55:00' < temp[0] <= '24:00:00':
                    List_set[list_id].append(temp[1])
                    continue
                else:
                    list_id += 1







    print("Below is the statistics result:")

    for i in List_set:
        p = set(i)
        print(len(p))


def test():
    print('TESTING!!!')
    # opt = '2018-03-07'
    # opt1 = '32a51b9cff22ce1794e4947d1aa1496fe1632cfb'
    # opt2 = 'e3e104a4bfd55c0fcaaeeaca158ac099eaf720b5'
    # opt3 = 'ssh://git@stash.arraycomm.com:7999/bnr/nr_phy_b4860.git'
    # opt4 = 'update for 2nd release'
    # modify_cl(opt, opt1, opt2, opt3, opt4)

    # opt = "2018-03-07"
    # opt1 = r'newrelease\FLI\Source\FLI\SC\BasePort\phy_kernel\source\baseport_lib\nr_phy_srs'
    #
    # modify_cl_i(opt, opt1)

    opt = '2018'
    opt1 = '55f8ffa9465601bf13a1bb6d15cb984a910ed186'
    opt2 = 'becc70a2666bc253d39b4707cda2100459880c9f'
    opt3 = 'ssh://git@stash.arraycomm.com:7999/fm/phy_b4xxx.git'



def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hvs", ["version", "help"])
    except getopt.GetoptError:
        print("for help use --help or -h")
        sys.exit(2)
    if args == [] and opts == []:
        usage()
        sys.exit()

    for op, value in opts:
        if op == "-h" or op == "--help":
            usage()
            sys.exit()
        elif op == "--version" or op == "-v":
            version()
            sys.exit()
        elif op == "-s":
            license_statis(argv[1])
        else:
            usage()
            sys.exit()


if __name__ == "__main__":
    # test()
    main(sys.argv[1:])
