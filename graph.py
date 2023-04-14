import os
import sys
import re
import matplotlib.pyplot as plt
import numpy as np
import itertools
import operator
import random


def build_old_dic(f):
    dic = {
        "last_streamID": [],
        "last_uid": [],
        "start_cycle": [],
        "end_cycle": [],

        "L1I_total_cache_accesses": [],
        "L1I_total_cache_misses": [],
        "L1D_total_cache_accesses": [],
        "L1D_total_cache_misses": [],
        "L1C_total_cache_accesses": [],
        "L1C_total_cache_misses": [],
        "L1T_total_cache_accesses": [],
        "L1T_total_cache_misses": [],
        "Total_core__GLOBAL_ACC_R__HIT": [],
        "Total_core__GLOBAL_ACC_R__MSHR_HIT": [],
        "Total_core__GLOBAL_ACC_R__MISS": [],
        "Total_core__GLOBAL_ACC_R__TOTAL": [],
        "Total_core__GLOBAL_ACC_W__HIT": [],
        "Total_core__GLOBAL_ACC_W__MSHR_HIT": [],
        "Total_core__GLOBAL_ACC_W__MISS": [],
        "Total_core__GLOBAL_ACC_W__TOTAL": [],

        "L2_total_cache_accesses": [],
        "L2_total_cache_misses": [],
        "L2__GLOBAL_ACC_R__HIT": [],
        "L2__GLOBAL_ACC_R__MSHR_HIT": [],
        "L2__GLOBAL_ACC_R__MISS": [],
        "L2__GLOBAL_ACC_R__TOTAL": [],
        "L2__GLOBAL_ACC_W__HIT": [],
        "L2__GLOBAL_ACC_W__MSHR_HIT": [],
        "L2__GLOBAL_ACC_W__MISS": [],
        "L2__GLOBAL_ACC_W__TOTAL": [],
    }

    for line in f:
        data = re.findall("\d+", line)
        if "L1I_total_cache_accesses" in line:
            dic["L1I_total_cache_accesses"].append(int(data[1]))
        elif "L1I_total_cache_misses" in line:
            dic["L1I_total_cache_misses"].append(int(data[1]))
        elif "L1D_total_cache_accesses" in line:
            dic["L1D_total_cache_accesses"].append(int(data[1]))
        elif "L1D_total_cache_misses" in line:
            dic["L1D_total_cache_misses"].append(int(data[1]))
        elif "L1C_total_cache_accesses" in line:
            dic["L1C_total_cache_accesses"].append(int(data[1]))
        elif "L1C_total_cache_misses" in line:
            dic["L1C_total_cache_misses"].append(int(data[1]))
        elif "L1T_total_cache_accesses" in line:
            dic["L1T_total_cache_accesses"].append(int(data[1]))
        elif "L1T_total_cache_misses" in line:
            dic["L1T_total_cache_misses"].append(int(data[1]))
        elif "L2_total_cache_accesses" in line:
            dic["L2_total_cache_accesses"].append(int(data[1]))
        elif "L2_total_cache_misses" in line:
            dic["L2_total_cache_misses"].append(int(data[1]))
        elif "GLOBAL" in line:
            if "Total_core_cache_stats_breakdown" in line:
                if "GLOBAL_ACC_R" in line:
                    if "[TOTAL_ACCESS]" in line:
                        dic["Total_core__GLOBAL_ACC_R__TOTAL"].append(int(data[0]))
                    elif "[HIT]" in line:
                        dic["Total_core__GLOBAL_ACC_R__HIT"].append(int(data[0]))
                    elif "[MSHR_HIT]" in line:
                        dic["Total_core__GLOBAL_ACC_R__MSHR_HIT"].append(int(data[0]))
                    elif "[MISS]" in line:
                        dic["Total_core__GLOBAL_ACC_R__MISS"].append(int(data[0]))
                elif "GLOBAL_ACC_W" in line:
                    if "[TOTAL_ACCESS]" in line:
                        dic["Total_core__GLOBAL_ACC_W__TOTAL"].append(int(data[0]))
                    elif "[HIT]" in line:
                        dic["Total_core__GLOBAL_ACC_W__HIT"].append(int(data[0]))
                    elif "[MSHR_HIT]" in line:
                        dic["Total_core__GLOBAL_ACC_W__MSHR_HIT"].append(int(data[0]))
                    elif "[MISS]" in line:
                        dic["Total_core__GLOBAL_ACC_W__MISS"].append(int(data[0]))
            elif "L2_cache_stats_breakdown" in line:
                if "GLOBAL_ACC_R" in line:
                    if "[TOTAL_ACCESS]" in line:
                        dic["L2__GLOBAL_ACC_R__TOTAL"].append(int(data[1]))
                    elif "[HIT]" in line:
                        dic["L2__GLOBAL_ACC_R__HIT"].append(int(data[1]))
                    elif "[MSHR_HIT]" in line:
                        dic["L2__GLOBAL_ACC_R__MSHR_HIT"].append(int(data[1]))
                    elif "[MISS]" in line:
                        dic["L2__GLOBAL_ACC_R__MISS"].append(int(data[1]))
                elif "GLOBAL_ACC_W" in line:
                    if "[TOTAL_ACCESS]" in line:
                        dic["L2__GLOBAL_ACC_W__TOTAL"].append(int(data[1]))
                    elif "[HIT]" in line:
                        dic["L2__GLOBAL_ACC_W__HIT"].append(int(data[1]))
                    elif "[MSHR_HIT]" in line:
                        dic["L2__GLOBAL_ACC_W__MSHR_HIT"].append(int(data[1]))
                    elif "[MISS]" in line:
                        dic["L2__GLOBAL_ACC_W__MISS"].append(int(data[1]))
    return dic


def build_dic(f):
    dic = {
        "last_streamID": [],
        "last_uid": [],
        "start_cycle": [],
        "end_cycle": [],

        "L1I_total_cache_accesses": [],
        "L1I_total_cache_misses": [],
        "L1D_total_cache_accesses": [],
        "L1D_total_cache_misses": [],
        "L1C_total_cache_accesses": [],
        "L1C_total_cache_misses": [],
        "L1T_total_cache_accesses": [],
        "L1T_total_cache_misses": [],
        "Total_core__GLOBAL_ACC_R__HIT": [],
        "Total_core__GLOBAL_ACC_R__MSHR_HIT": [],
        "Total_core__GLOBAL_ACC_R__MISS": [],
        "Total_core__GLOBAL_ACC_R__TOTAL": [],
        "Total_core__GLOBAL_ACC_W__HIT": [],
        "Total_core__GLOBAL_ACC_W__MSHR_HIT": [],
        "Total_core__GLOBAL_ACC_W__MISS": [],
        "Total_core__GLOBAL_ACC_W__TOTAL": [],

        "L2_total_cache_accesses": [],
        "L2_total_cache_misses": [],
        "L2__GLOBAL_ACC_R__HIT": [],
        "L2__GLOBAL_ACC_R__MSHR_HIT": [],
        "L2__GLOBAL_ACC_R__MISS": [],
        "L2__GLOBAL_ACC_R__TOTAL": [],
        "L2__GLOBAL_ACC_W__HIT": [],
        "L2__GLOBAL_ACC_W__MSHR_HIT": [],
        "L2__GLOBAL_ACC_W__MISS": [],
        "L2__GLOBAL_ACC_W__TOTAL": [],
    }

    for line in f:
        data = re.findall("\d+", line)
        if "last_streamID" in line:
            dic["last_streamID"].append(int(data[0]))
            dic["last_uid"].append(int(data[1]))
            dic["start_cycle"].append(int(data[2]))
            dic["end_cycle"].append(int(data[3]))
        elif "L1I_total_cache_accesses" in line:
            dic["L1I_total_cache_accesses"].append(int(data[1]))
        elif "L1I_total_cache_misses" in line:
            dic["L1I_total_cache_misses"].append(int(data[1]))
        elif "L1D_total_cache_accesses" in line:
            dic["L1D_total_cache_accesses"].append(int(data[1]))
        elif "L1D_total_cache_misses" in line:
            dic["L1D_total_cache_misses"].append(int(data[1]))
        elif "L1C_total_cache_accesses" in line:
            dic["L1C_total_cache_accesses"].append(int(data[1]))
        elif "L1C_total_cache_misses" in line:
            dic["L1C_total_cache_misses"].append(int(data[1]))
        elif "L1T_total_cache_accesses" in line:
            dic["L1T_total_cache_accesses"].append(int(data[1]))
        elif "L1T_total_cache_misses" in line:
            dic["L1T_total_cache_misses"].append(int(data[1]))
        elif "L2_total_cache_accesses" in line:
            dic["L2_total_cache_accesses"].append(int(data[1]))
        elif "L2_total_cache_misses" in line:
            dic["L2_total_cache_misses"].append(int(data[1]))
        elif "GLOBAL" in line:
            if "Total_core_cache_stats_breakdown" in line:
                if "GLOBAL_ACC_R" in line:
                    if "[TOTAL_ACCESS]" in line:
                        dic["Total_core__GLOBAL_ACC_R__TOTAL"].append(int(data[1]))
                    elif "[HIT]" in line:
                        dic["Total_core__GLOBAL_ACC_R__HIT"].append(int(data[1]))
                    elif "[MSHR_HIT]" in line:
                        dic["Total_core__GLOBAL_ACC_R__MSHR_HIT"].append(int(data[1]))
                    elif "[MISS]" in line:
                        dic["Total_core__GLOBAL_ACC_R__MISS"].append(int(data[1]))
                elif "GLOBAL_ACC_W" in line:
                    if "[TOTAL_ACCESS]" in line:
                        dic["Total_core__GLOBAL_ACC_W__TOTAL"].append(int(data[1]))
                    elif "[HIT]" in line:
                        dic["Total_core__GLOBAL_ACC_W__HIT"].append(int(data[1]))
                    elif "[MSHR_HIT]" in line:
                        dic["Total_core__GLOBAL_ACC_W__MSHR_HIT"].append(int(data[1]))
                    elif "[MISS]" in line:
                        dic["Total_core__GLOBAL_ACC_W__MISS"].append(int(data[1]))
            elif "L2_cache_stats_breakdown" in line:
                if "GLOBAL_ACC_R" in line:
                    if "[TOTAL_ACCESS]" in line:
                        dic["L2__GLOBAL_ACC_R__TOTAL"].append(int(data[2]))
                    elif "[HIT]" in line:
                        dic["L2__GLOBAL_ACC_R__HIT"].append(int(data[2]))
                    elif "[MSHR_HIT]" in line:
                        dic["L2__GLOBAL_ACC_R__MSHR_HIT"].append(int(data[2]))
                    elif "[MISS]" in line:
                        dic["L2__GLOBAL_ACC_R__MISS"].append(int(data[2]))
                elif "GLOBAL_ACC_W" in line:
                    if "[TOTAL_ACCESS]" in line:
                        dic["L2__GLOBAL_ACC_W__TOTAL"].append(int(data[2]))
                    elif "[HIT]" in line:
                        dic["L2__GLOBAL_ACC_W__HIT"].append(int(data[2]))
                    elif "[MSHR_HIT]" in line:
                        dic["L2__GLOBAL_ACC_W__MSHR_HIT"].append(int(data[2]))
                    elif "[MISS]" in line:
                        dic["L2__GLOBAL_ACC_W__MISS"].append(int(data[2]))
    return dic


def process_old_dic(d):
    dic = {}
    for k, v in d.items():
        temp = []
        if len(v) > 0:
            temp.append(v[0])
            for i in range(1, len(v)):
                temp.append(v[i] - v[i - 1])
        dic[k] = temp
    return dic


def process_dic(d):
    dic = {}
    last_streamID = d["last_streamID"]

    skip = 4
    for k, v in d.items():
        if skip > 0:
            dic[k] = v
            skip -= 1
            continue
        temp = []
        for i in range(len(v)):
            updated = False
            for j in range(i - 1, -1, -1):
                if last_streamID[j] == last_streamID[i]:
                    temp.append(v[i] - v[j])
                    updated = True
                    break
            if not updated:
                temp.append(v[i])
        dic[k] = temp
    return dic


def get_sums(d):
    skip = 4
    sums = {}
    for k, v in d.items():
        if skip > 0:
            skip -= 1
            continue
        s = 0
        for i in range(len(v)):
            s += v[i]
        sums[k] = s
    return sums


def print_dict(d):
    for k, v in d.items():
        print(k, v)
    print()


def print_dicts(da, db, dc):
    print("************tip_serialized************")
    print_dict(da)
    print("************clean************")
    print_dict(db)
    print("************tip************")
    print_dict(dc)


def plot2(a, b, c, la, lb, title):
    ind = np.arange(2)
    plt.figure(figsize=(10, 5))
    width = 0.2

    plt.bar(ind, a, width, label='tip_serialized')
    plt.bar(ind + width, b, width, label='curr')
    plt.bar(ind + 2 * width, c, width, label='tip')

    plt.xlabel('Code')
    plt.ylabel('Counts')
    plt.title(title)

    plt.xticks(ind + width, (la, lb))

    plt.legend(loc='best')
    plt.show()


def plot3(a, b, c, la, lb, lc, title):
    ind = np.arange(3)
    plt.figure(figsize=(10, 5))
    width = 0.2

    plt.bar(ind, a, width, label='tip_serialized')
    plt.bar(ind + width, b, width, label='curr')
    plt.bar(ind + 2 * width, c, width, label='tip')

    plt.xlabel('Code')
    plt.ylabel('Counts')
    plt.title(title)

    plt.xticks(ind + width, (la, lb, lc))

    plt.legend(loc='best')
    plt.show()


def plot4(a, b, c, la, lb, lc, ld, title):
    ind = np.arange(4)
    plt.figure(figsize=(10, 5))
    width = 0.2

    plt.bar(ind, a, width, label='tip_serialized')
    plt.bar(ind + width, b, width, label='curr')
    plt.bar(ind + 2 * width, c, width, label='tip')

    plt.xlabel('Code')
    plt.ylabel('Counts')
    plt.title(title)

    plt.xticks(ind + width, (la, lb, lc, ld))

    plt.legend(loc='best')
    plt.show()


def process_timelines(data, title):
    data_sets = {}
    for tup in data:
        if tup[0] not in data_sets:
            data_sets[tup[0]] = []
        data_sets[tup[0]].append(tup[1])

    data_array = []
    labels = []
    for key in sorted(data_sets.keys()):
        labels.append("Stream_" + str(key))
        data_array.append(data_sets[key])

    plot_timeline(data_array, labels, title)


def plot_timeline(data_sets, labels, title):
    # Create the figure and axis objects
    fig, ax = plt.subplots()

    # Loop over each data set
    y_positions = []
    x_min = float('inf')
    x_max = -float('inf')
    for i, data in enumerate(data_sets):
        # Compute the position and width of each bar segment
        positions = []
        widths = []
        colors = []
        for segment in data:
            positions.append(segment[0])
            widths.append(segment[1] - segment[0])
            colors.append(segment[2] if len(segment) > 2 else None)  # Use None as default color if segment doesn't have a color

        # Add the y position of the current data set
        y_positions.append(i)

        # Compute the minimum and maximum x values of the current data set
        x_min = min(x_min, min(positions))
        x_max = max(x_max, max(positions) + max(widths))

        # Draw the bar segments
        for j, (position, width, color) in enumerate(zip(positions, widths, colors)):
            if color is not None:
                ax.barh(y=i, width=width, left=position, height=0.5, color=color)
            else:
                ax.barh(y=i, width=width, left=position, height=0.5, color=(random.random(), random.random(), random.random()))

    ax.set_yticks(y_positions)
    ax.set_yticklabels(labels)
    padding = (x_max - x_min) * 0.05
    ax.set_xlim(x_min - padding, x_max + padding)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='x')
    ax.set_title(title)
    plt.show()


if __name__ == '__main__':
    p = os.path.dirname(os.path.realpath(__file__))
    pa = p + sys.argv[1]
    pb = p + sys.argv[2]
    pc = p + sys.argv[3]
    try:
        fa = open(pa, mode='r')
        da = build_dic(fa)
        fa.close()
        fb = open(pb, mode='r')
        db = build_old_dic(fb)
        fb.close()
        fc = open(pc, mode='r')
        dc = build_dic(fc)
        fc.close()
    except:
        print("Invalid Input File")
        exit(1)

    # raw data extraction
    print_dicts(da, db, dc)

    da = process_dic(da)
    db = process_old_dic(db)
    dc = process_dic(dc)

    # per stream per kernel stats
    print_dicts(da, db, dc)

    sa = get_sums(da)
    sb = get_sums(db)
    sc = get_sums(dc)

    # real sum of each kind of stats
    print_dicts(sa, sb, sc)


    a = [sa["Total_core__GLOBAL_ACC_R__HIT"], sa["Total_core__GLOBAL_ACC_R__MSHR_HIT"], sa["Total_core__GLOBAL_ACC_R__MISS"], sa["Total_core__GLOBAL_ACC_R__TOTAL"]]
    b = [sb["Total_core__GLOBAL_ACC_R__HIT"], sb["Total_core__GLOBAL_ACC_R__MSHR_HIT"], sb["Total_core__GLOBAL_ACC_R__MISS"], sb["Total_core__GLOBAL_ACC_R__TOTAL"]]
    c = [sc["Total_core__GLOBAL_ACC_R__HIT"], sc["Total_core__GLOBAL_ACC_R__MSHR_HIT"], sc["Total_core__GLOBAL_ACC_R__MISS"], sc["Total_core__GLOBAL_ACC_R__TOTAL"]]
    plot4(a, b, c, "Total_core__GLOBAL_ACC_R__HIT", "Total_core__GLOBAL_ACC_R__MSHR_HIT", "Total_core__GLOBAL_ACC_R__MISS", "Total_core__GLOBAL_ACC_R__TOTAL", "L1 Cache Reads")


    a = [sa["Total_core__GLOBAL_ACC_W__HIT"], sa["Total_core__GLOBAL_ACC_W__MSHR_HIT"], sa["Total_core__GLOBAL_ACC_W__MISS"], sa["Total_core__GLOBAL_ACC_W__TOTAL"]]
    b = [sb["Total_core__GLOBAL_ACC_W__HIT"], sb["Total_core__GLOBAL_ACC_W__MSHR_HIT"], sb["Total_core__GLOBAL_ACC_W__MISS"], sb["Total_core__GLOBAL_ACC_W__TOTAL"]]
    c = [sc["Total_core__GLOBAL_ACC_W__HIT"], sc["Total_core__GLOBAL_ACC_W__MSHR_HIT"], sc["Total_core__GLOBAL_ACC_W__MISS"], sc["Total_core__GLOBAL_ACC_W__TOTAL"]]
    plot4(a, b, c, "Total_core__GLOBAL_ACC_W__HIT", "Total_core__GLOBAL_ACC_W__MSHR_HIT", "Total_core__GLOBAL_ACC_W__MISS", "Total_core__GLOBAL_ACC_W__TOTAL", "L1 Cache Writes")


    a = [sa["L2__GLOBAL_ACC_R__HIT"], sa["L2__GLOBAL_ACC_R__MSHR_HIT"], sa["L2__GLOBAL_ACC_R__MISS"], sa["L2__GLOBAL_ACC_R__TOTAL"]]
    b = [sb["L2__GLOBAL_ACC_R__HIT"], sb["L2__GLOBAL_ACC_R__MSHR_HIT"], sb["L2__GLOBAL_ACC_R__MISS"], sb["L2__GLOBAL_ACC_R__TOTAL"]]
    c = [sc["L2__GLOBAL_ACC_R__HIT"], sc["L2__GLOBAL_ACC_R__MSHR_HIT"], sc["L2__GLOBAL_ACC_R__MISS"], sc["L2__GLOBAL_ACC_R__TOTAL"]]
    plot4(a, b, c, "L2__GLOBAL_ACC_R__HIT", "L2__GLOBAL_ACC_R__MSHR_HIT", "L2__GLOBAL_ACC_R__MISS", "L2__GLOBAL_ACC_R__TOTAL", "L2 cache Reads")


    a = [sa["L2__GLOBAL_ACC_W__HIT"], sa["L2__GLOBAL_ACC_W__MSHR_HIT"], sa["L2__GLOBAL_ACC_W__MISS"], sa["L2__GLOBAL_ACC_W__TOTAL"]]
    b = [sb["L2__GLOBAL_ACC_W__HIT"], sb["L2__GLOBAL_ACC_W__MSHR_HIT"], sb["L2__GLOBAL_ACC_W__MISS"], sb["L2__GLOBAL_ACC_W__TOTAL"]]
    c = [sc["L2__GLOBAL_ACC_W__HIT"], sc["L2__GLOBAL_ACC_W__MSHR_HIT"], sc["L2__GLOBAL_ACC_W__MISS"], sc["L2__GLOBAL_ACC_W__TOTAL"]]
    plot4(a, b, c, "L2__GLOBAL_ACC_W__HIT", "L2__GLOBAL_ACC_W__MSHR_HIT", "L2__GLOBAL_ACC_W__MISS", "L2__GLOBAL_ACC_W__TOTAL", "L2 cache Writes")


    timelines = list(zip(da["last_streamID"], [(s, e) for s, e in zip(da["start_cycle"], da["end_cycle"])]))
    process_timelines(timelines, "Serialized Timelines")


    timelines = list(zip(dc["last_streamID"], [(s, e) for s, e in zip(dc["start_cycle"], dc["end_cycle"])]))
    process_timelines(timelines, "Tip Timeline")
