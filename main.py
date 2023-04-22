import glob
import pandas as pd
import matplotlib.pyplot as plt


def process_csv_data():
    files = glob.glob("data-dump/*.csv")
    content = []
    bin_size = 10

    valid_event_types = ["green", "light", "round", "squirrel"]
    print("Start reading CSV files....")

    for filename in files:
        df = pd.read_csv(filename)
        content.append(df)

    print(len(content), " files are imported!")
    # converting content to data frame
    df = pd.concat(content)

    # requirement: The device_id and event_type should be treated as case-insensitive
    # convert the values to lower case
    df['device_id'] = df['device_id'].astype(str).str.lower()
    df['event_type'] = df['event_type'].astype(str).str.lower()

    # find invalid event_type and save it to a cvs file
    invalid_event_type = df.loc[~df['event_type'].isin(valid_event_types)]
    invalid_event_type.to_csv('invalid_event_type.cvs')
    print("Invalid rows detected and saved to invalid_event_type.cvs")
    # print(invalid_event_type.to_string())

    # only select valid event_types
    df = df.loc[df['event_type'].isin(valid_event_types)]
    df_his = df
    # print(df_his.to_string())

    # Requirement 1: We want to know the min, max, and mean of the count of each event type per device_id.
    df = df.groupby(['device_id', 'event_type'])["event_type"].count().reset_index(name="event_type_count")
    df = df.groupby('device_id')['event_type_count'].agg(['min', 'max', 'mean']).reset_index()

    # save the result to a CVS file
    df.to_csv('event_type_agg_by_device_id.cvs')
    print("The statics number of each event type per device_id is saved to "
          "event_type_agg_by_device_id.cvs")

    # Requirement 2:Histogram data for the counts of squirrel event_type emitted by devices.
    df_his.loc[df_his['event_type'].isin(['squirrel'])]

    # Convert UTC float time to timestamp
    df_his['timestamp_date'] = pd.to_datetime(df_his['timestamp'], unit='s')
    # print(df_his.to_string())
    df_his.hist(column='timestamp_date', bins=bin_size)
    plt.savefig('histogram_squirrel.pdf')
    print("Histogram data for the counts of squirrel event_type is saved to histogram_squirrel.pdf")


if __name__ == '__main__':
    process_csv_data()
