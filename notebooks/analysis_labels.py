import pandas as pd
import numpy as np
import datetime as dt

def get_labels_per_party(data_mps: pd.DataFrame,
                         dates,
                         ids_mps,
                         TOPIC: str,
                         normalization: bool) -> pd.DataFrame:
    
    df = data_mps[(data_mps.user_id.isin(ids_mps)) & (data_mps.label==TOPIC)][['datetime', 'party']]

    parties = data_mps.party.unique()

    labels_per_party = np.zeros((len(dates), len(parties)))
    df_labels = pd.DataFrame(labels_per_party, columns = parties)
    df_labels.loc[:, ('datetime')] = dates

    for day in dates:
        dict_dummy = df[df.datetime == day]['party'].value_counts().to_dict()
        for (key, value) in dict_dummy.items():
            df_labels.loc[df_labels.datetime==day, (key)] = value
            
    if normalization:
        df_labels.loc[1:, (parties)] = df_labels[parties].div(df_labels[parties].sum(axis=1), axis=0).loc[1:, :]
    return df_labels

def get_labels_per_day(dates: np.ndarray, 
                       data: pd.DataFrame,
                       TOTAL: str,
                       normalization: bool = True) -> np.ndarray:

    labels_per_day = np.zeros((len(dates), TOTAL))
    for (idx_day, day) in enumerate(dates):
        d = data[data.date==day].label.value_counts().to_dict()
        for key in d.keys():
            if key == -1:
                labels_per_day[idx_day, 0] = d[key]
            if key > 0:
                labels_per_day[idx_day, int(key)] = d[key]
                
    if normalization:
        labels_per_day = np.apply_along_axis(lambda x: x/sum(x), 1, labels_per_day[1:, 1:])
        
    return labels_per_day

def cluster_dates(n_days:int, 
                  sorted_dates: np.ndarray, 
                  format_date: str = '%d/%m/%Y', 
                  type_dt: bool = True) -> np.ndarray:

    delta = dt.timedelta(days=n_days)

    start_date = dt.datetime.strptime(sorted_dates[0], format_date)
    end_date = dt.datetime.strptime(sorted_dates[-1], format_date)

    new_dates = []

    next_date = start_date + delta
    while next_date < end_date:
        new_dates.append(next_date)
        next_date = next_date + delta

    new_dates.append(end_date)
    
    if not type_dt:
        new_dates = [dt.datetime.strftime(date, format_date) for date in new_dates]

    return np.array(new_dates)

def cluster_labels(dates: np.ndarray, 
                   new_dates: np.ndarray,
                   labels_per_day: np.ndarray,
                   ABSTAIN: bool = True,
                   format_date: str = '%d/%m/%Y',
                   normalization: bool = True) -> np.ndarray:
    
    new_labels = np.zeros((len(new_dates), labels_per_day.shape[1]))
    
    dates_formatted = np.array([dt.datetime.strptime(date, format_date) for date in dates])
    start_date = dates_formatted[0]

    for (idx_date, date) in enumerate(new_dates):
        idx = np.where((dates_formatted >= start_date) & (dates_formatted < date))[0]
        new_labels[idx_date, :] = labels_per_day[idx, :].sum(axis=0)
        start_date = date

    if normalization:
        if ABSTAIN:
            new_labels = np.apply_along_axis(lambda x: x/sum(x), 1, new_labels[:, 1:])
        else:
            new_labels = np.apply_along_axis(lambda x: x/sum(x), 1, new_labels)
    return new_labels