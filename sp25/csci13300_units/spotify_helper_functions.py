# millisecond parsing


def msPlayed_to_hms(ms):
    # each hour is 3600 * 1000 ms
    hours = ms // (3600 * 1000)
    # each minute is 60 * 1000 ms
    minutes = (ms % (3600 * 1000)) // (60 * 1000)
    # each second is 1000 ms
    seconds = (ms % (60 * 1000)) // 1000
    milliseconds = ms % 1000
    return (hours, minutes, seconds, milliseconds)


def msPlayed_to_hours(ms):
    return ms / (3600 * 1000)


def pretty_print_hmsms(hmsms):
    # pretty print hours/minutes/seconds/milliseconds
    h, m, s, ms = hmsms
    if h != 0:
        return (
            f"{h} hour"
            + "s" * (h != 1)
            + f", {m} minute"
            + "s" * (m != 1)
            + f", and {round(s + 0.001*ms,3)} second"
            + "s" * (round(s + 0.001 * ms, 3) != 1)
        )
    elif m != 0:
        return (
            f"{m} minute"
            + "s" * (m != 1)
            + f", and {round(s + 0.001*ms,3)} second"
            + "s" * (round(s + 0.001 * ms, 3) != 1)
        )
    elif s != 0:
        return f"{round(s + 0.001*ms,3)} second" + "s" * (round(s + 0.001 * ms, 3) != 1)
    else:
        return f"{ms} millisecond" + "s" * (ms != 1)


def ms_to_pprint(ms):
    hms = msPlayed_to_hms(ms)
    return pretty_print_hmsms(hms)


def replace_msPlayed_with_pprint(old_df):
    df = old_df.copy()
    df["hms"] = df["msPlayed"].apply(msPlayed_to_hms)
    df["times"] = df["hms"].apply(pretty_print_hmsms)
    df.drop(columns=["msPlayed", "hms"], inplace=True)
    return df


# datetime parsing

from datetime import datetime, timedelta, date


def endTime_to_ymdhm_tuple(endTime):
    # convert endTime to a tuple of (year, month, day, hour, minute)
    # endTime is a string of the form  'yyyy-mm-dd hh:mm'
    # (e.g. '2020-11-07 23:40')
    date, time = endTime.split(" ")
    year, month, day = [int(x) for x in date.split("-")]
    hour, minute = [int(x) for x in time.split(":")]
    return (year, month, day, hour, minute)


def ymdhm_to_days(ymdhm):
    # convert tuple of (year, month, day, hour, minute) to days since the year 2000-01-01
    # to be used for plotting and comparisons
    year, month, day, hour, minute = ymdhm
    date_2000 = datetime(year=2000, month=1, day=1)
    listen_date = datetime(year=year, month=month, day=day, hour=hour, minute=minute)
    return (listen_date - date_2000).days


def ymdhm_to_dayfrac(ymdhm):
    # (year, month, day, hour, minute) -> fraction of day
    year, month, day, hour, minute = ymdhm
    return hour / 24.0 + minute / (24.0 * 60.0)


def endTime_to_weekday(endTime):
    # use iso format
    return date.fromisoformat(endTime.split(" ")[0]).weekday()


def ymdhm_to_yearFrac(ymdhm):
    year, month, day, hour, minute = ymdhm
    return (
        date(year=year, month=month, day=day) - date(year=year, month=1, day=1)
    ).days


def add_time_cols(old_df):
    # add columns for day since 2000, time of day, and weekday
    # based on endTime
    df = old_df.copy()
    df["ymdhm"] = df["endTime"].apply(endTime_to_ymdhm_tuple)
    df["dayDiff"] = df["ymdhm"].apply(ymdhm_to_days)
    df["dayFrac"] = df["ymdhm"].apply(ymdhm_to_dayfrac)
    df["weekday"] = df["endTime"].apply(endTime_to_weekday)
    df["yearFrac"] = df["ymdhm"].apply(ymdhm_to_yearFrac)
    df.drop(columns=["ymdhm"], inplace=True)
    return df


# plotting

from matplotlib import pyplot as plt
import numpy as np


def time_plots(old_data):
    data = old_data.copy()
    data = add_time_cols(data)
    plt.rcParams["figure.figsize"] = (14, 7)
    plt.rcParams["figure.dpi"] = 500
    plt.subplot(2, 2, 1)
    data["dayFrac"].hist(bins=100)
    plt.xticks(
        np.arange(0, 1, 0.082), [f"{i}:00" for i in range(0, 25, 2)], rotation=35
    )
    plt.title("Time of Day")
    plt.subplot(2, 2, 2)
    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    plt.bar(weekdays, [data["weekday"].value_counts()[i] for i in range(7)])
    plt.title("Day of Week")
    plt.subplot(2, 2, 3)
    data["dayDiff"].hist(bins=70)
    plt.title("Day since 2000")
    plt.subplot(2, 2, 4)
    data["yearFrac"].hist(bins=100)
    plt.title("Time of Year")
    plt.tight_layout()
    plt.show()


# functions to deal with tracks and artists

import pandas as pd


def prettify_output(tuple_list, col_names):
    # takes list of tuples [(string, (msplayed1, msplayed2))...] and
    # turns it into a df [col_name[0] : col_name[1] : col_name[2]]
    strings = [item[0] for item in tuple_list]
    int_1s = [ms_to_pprint(item[1][0]) for item in tuple_list]
    int_2s = [ms_to_pprint(item[1][1]) for item in tuple_list]
    out = pd.DataFrame()
    out[col_names[0]] = pd.Series(strings)
    out[col_names[1]] = pd.Series(int_1s)
    out[col_names[2]] = pd.Series(int_2s)
    return out


def overlap_users(top_tuple, floor_time=(60 * 60 * 1000)):  # floor_time defaults to 1hr
    # iterate through top tracks and select those found in both user histories
    # returns list of tuples (track, (u1 track time), (u2 track time))
    # sorts list by first user listen time
    u1, u2 = top_tuple
    # row.trackName : row.msPlayed
    u1_dict = {row[0]: row[1][0] for row in u1.iterrows()}
    comparison_dict = []
    for row in u2.iterrows():
        if row[0] in u1_dict and row[1][0] > floor_time:  # if row.trackName in dict
            comparison_dict.append((row[0], (u1_dict[row[0]], row[1][0])))
    # sort
    comparison_dict.sort(key=lambda x: x[1][0], reverse=True)
    return comparison_dict


def get_comparison_histories(old_df, user_1, user_2):
    df = old_df.copy()
    return (df[df["person"] == user_1], df[df["person"] == user_2])


def top_tracks(user_histories):
    u1_history, u2_history = user_histories
    return [
        h.groupby(by="trackName").sum().sort_values(by="msPlayed", ascending=False)
        for h in [u1_history, u2_history]
    ]


def compare_top_tracks(old_df, user_1, user_2, floor_time=(60 * 60 * 1000)):
    out = prettify_output(
        overlap_users(
            top_tracks(get_comparison_histories(old_df, user_1, user_2)),
            floor_time=floor_time,
        ),
        ["track", user_1 + " listen time", user_2 + " listen time"],
    )
    return out


def top_artists(user_histories):
    u1_history, u2_history = user_histories
    return [
        h.groupby(by="artistName").sum().sort_values(by="msPlayed", ascending=False)
        for h in [u1_history, u2_history]
    ]


def compare_top_artists(old_df, user_1, user_2):
    out = prettify_output(
        overlap_users(top_artists(get_comparison_histories(old_df, user_1, user_2))),
        ["artist", user_1 + " listen time", user_2 + " listen time"],
    )
    return out
