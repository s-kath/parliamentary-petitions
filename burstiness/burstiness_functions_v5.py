
from datetime import date, timedelta
import numpy as np
import matplotlib.pyplot as plt
import random
from datetime import datetime
import pandas as pd

# Get ids of petitions with keyword term of interest
def return_keyword_dates(epets, term, date_field, keyword_field):
    return_dates = []
    for k in epets.keys():
        if epets[k][keyword_field] != None:
            if term in epets[k][keyword_field]:
                return_dates.append(epets[k][date_field])
    
    return_dates.sort()
    
    return return_dates

# Get ids of petitions with term(s) of interest
def return_metadata_theme_dates(epets, term, date_field, theme_field, cflag):
    return_dates = []
    for k in epets.keys():
        if cflag == 'uk' and epets[k][theme_field] != None:
            if term in epets[k][theme_field]:
                return_dates.append(epets[k][date_field])
        else:
            if term == epets[k][theme_field]:
                return_dates.append(epets[k][date_field])
    
    return_dates.sort()
    
    return return_dates

# find inter-event time intervals
def create_ts(dates):
    ts = []
    for i in range(1, len(dates)):
        t = dates[i] - dates[i-1]
        ts.append(t.days)

    return ts

# burstiness parameter
def B_par(ts):
    B = (np.std(ts) - np.mean(ts))/ (np.std(ts) + np.mean(ts)) # change to np.mean (?)
    return B

# memory parameter
def M_par(ts):
    t_t = ts[:-1]
    m1 = np.mean(t_t) # change to mean(?)
    sd1 = np.std(t_t, ddof=1)

    t_t1 = ts[1:]
    m2 = np.mean(t_t1)
    sd2 = np.std(t_t1, ddof=1)

    M = sum(((t_t[i] -m1)*(t_t1[i] -m2)/(sd1*sd2)) for i in range(len(t_t)))/len(t_t)
    
    return M

# shuffle time-intervals
def shuffle_ints(ts, N, seed_in = None):
    Ms = []

    if seed_in == None:
        random.seed(N)
    else:
        random.seed(seed_in)

    for n in range(N):
        x = ts.copy()
        random.shuffle(x)

        M = M_par(x)

        Ms.append(M)
        
    return Ms

# create full range of dates 
def create_daterange(min_date, max_date):
    date_range = [min_date + timedelta(days=x) for x in range((max_date - min_date).days)]

    date_range.append(max_date)

    date_range.sort()

    return date_range

# create full range of dates 
def create_daterange2(epets, date_field, min_date, max_date):
    date_range = [epets[k][date_field] for k in epets.keys() if min_date <= epets[k][date_field] <= max_date]
    date_range = list(set(date_range))
    date_range.sort()

    return date_range

# sampling dates for B 
def random_samp_Bs(date_range, samp_length, N, seed_in = None):
    Bs = []

    min_max = [date_range[0], date_range[-1]] # want the min and max date in each sample

    if seed_in == None:
        random.seed(N)
    else:
        random.seed(seed_in)

    for i in range(N):
        samp_full = random.choices(date_range, k = samp_length) # sample with replacement
        samp_full.extend(min_max)
        samp_full.sort() # make sure sampled dates are in chronological order
        
        B = B_par(create_ts(samp_full))

        Bs.append(B)

    return Bs

# sampling dates for B 
def random_samp_Bs_ignore(date_range, samp_length, N, seed_in = None):
    Bs = []

    min_max = [date_range[0], date_range[-1]] # want the min and max date in each sample

    # remove min and max date from list of sample-able dates as we are including them by force in each sample
    date_range2 = date_range.copy()
    date_range2.pop(0)
    date_range2.pop(-1)

    if seed_in == None:
        random.seed(N)
    else:
        random.seed(seed_in)
        
    for i in range(N):
        samp_full = random.choices(date_range2, k = samp_length) # sample with replacement
        samp_full.extend(min_max)
        samp_full.sort() # make sure sampled dates are in chronological order
        
        B = B_par(create_ts(samp_full))

        Bs.append(B)

    return Bs

# Find p-value for B/M
def find_pval(Xs, x_in):
    # prop = sum(val > x_in for val in Xs)/len(Xs)
    prop = sum(val >= x_in for val in Xs)/len(Xs) ## <- greater than or equal???
    return prop

# Check if p-value is significant
def check_pval_sig(pval, sig):
    if pval < sig:
        return 1
    else:
        return 0

# Check if p-value is significant after applying a Bonferroni correction
def check_pval_sig_bonf(pval, sig, m):
    new_sig = sig/m
    if pval < new_sig:
        return 1
    else:
        return 0

# burstiness pipeline for keywords
def keyword_theme_df_create2(epets, t_list, date_field, keyword_field, N = 10000, sig = 0.05):
    theme_BM_dict = {'theme': [], 
               'count': [],
               'B':[], 
               'B-pval-samp': [],
               'B-samp-flag': [],
               'B-samp-flag-bonf': [],
               'M': [], 
               'M-pval-shuffle': [],  
               'M-shuffle-flag': [],
               'M-shuffle-flag-bonf': [],
               'dates': [],
               'interevent-times':[]}
    
    m = len(t_list)

    for k in t_list: # k = one keyword
        return_dates = return_keyword_dates(epets, k, date_field, keyword_field)
        ts = create_ts(return_dates)
        B = B_par(ts)
        M = M_par(ts)
        
        
        theme_BM_dict['theme'].append(k)
        theme_BM_dict['count'].append(len(return_dates))
        theme_BM_dict['B'].append(B)
        theme_BM_dict['M'].append(M)

        theme_BM_dict['dates'].append([x.strftime("%Y-%m-%d") for x in return_dates])
        theme_BM_dict['interevent-times'].append(ts)
        
        
        Ms_shuffle = shuffle_ints(ts, return_dates[0], N)
        shuffle_pval = find_pval(Ms_shuffle, M)
        
        theme_BM_dict['M-pval-shuffle'].append(shuffle_pval)
        
        theme_BM_dict['M-shuffle-flag'].append(check_pval_sig(shuffle_pval, sig))

        theme_BM_dict['M-shuffle-flag-bonf'].append(check_pval_sig_bonf(shuffle_pval, sig, m))

        date_range = create_daterange(return_dates[0], return_dates[-1])
        b_date_samp_n = len(return_dates) - 2
        Bs_samp = random_samp_Bs(date_range, b_date_samp_n , N)
        Bs_pval_samp = find_pval(Bs_samp, B)
        Bs_samp_flag = check_pval_sig(Bs_pval_samp, sig)

        theme_BM_dict['B-pval-samp'].append(Bs_pval_samp)
        theme_BM_dict['B-samp-flag'].append(Bs_samp_flag)
        theme_BM_dict['B-samp-flag-bonf'].append(check_pval_sig_bonf(Bs_pval_samp, sig, m))
    
    return pd.DataFrame(theme_BM_dict)

# burstiness piepline for metadata themes
def metadata_theme_df_create2(epets, t_list, date_field, theme_field, cflag, N = 10000, sig = 0.05):
    theme_BM_dict = {'theme': [], 
               'count': [],
               'B':[], 
               'B-pval-samp': [],
               'B-samp-flag': [],
               'B-samp-flag-bonf': [],
               'M': [], 
               'M-pval-shuffle': [], 
               'M-shuffle-flag': [],
               'M-shuffle-flag-bonf': [],
               'dates': [],
               'interevent-times':[]}
    
    m = len(t_list)

    for k in t_list:
        return_dates = return_metadata_theme_dates(epets, k, date_field, theme_field, cflag)
        ts = create_ts(return_dates)
        B = B_par(ts)
        M = M_par(ts)
        
        theme_BM_dict['theme'].append(k)
        theme_BM_dict['count'].append(len(return_dates))
        theme_BM_dict['B'].append(B)
        theme_BM_dict['M'].append(M)

        theme_BM_dict['dates'].append([x.strftime("%Y-%m-%d") for x in return_dates])
        theme_BM_dict['interevent-times'].append(ts)

        
        Ms_shuffle = shuffle_ints(ts, return_dates[0], N)
        shuffle_pval = find_pval(Ms_shuffle, M)
        
        theme_BM_dict['M-pval-shuffle'].append(shuffle_pval)
        
        theme_BM_dict['M-shuffle-flag'].append(check_pval_sig(shuffle_pval, sig))

        theme_BM_dict['M-shuffle-flag-bonf'].append(check_pval_sig_bonf(shuffle_pval, sig, m))

        date_range = create_daterange(return_dates[0], return_dates[-1])
        b_date_samp_n = len(return_dates) - 2
        Bs_samp = random_samp_Bs(date_range, b_date_samp_n , N)
        Bs_pval_samp = find_pval(Bs_samp, B)
        Bs_samp_flag = check_pval_sig(Bs_pval_samp, sig)

        theme_BM_dict['B-pval-samp'].append(Bs_pval_samp)
        theme_BM_dict['B-samp-flag'].append(Bs_samp_flag)
        theme_BM_dict['B-samp-flag-bonf'].append(check_pval_sig_bonf(Bs_pval_samp, sig, m))
    
    return pd.DataFrame(theme_BM_dict)


def burstiness_df_create(epets, t_list, date_field, term_field, cflag, N = 10000, sig = 0.05):
    BM_dict = {'term': [], 
               'count': [],
               'B':[], 
               'B-pval-samp': [],
               'B-samp-flag': [],
               'B-samp-flag-bonf': [],
               'B-pval-samp-obsdates': [],
               'B-samp-flag-obsdates': [],
               'B-samp-flag-bonf-obsdates': [],
               'M': [], 
               'M-pval-shuffle': [], 
               'M-shuffle-flag': [],
               'M-shuffle-flag-bonf': [],
               'dates': [],
               'interevent-times':[]}
    
    m = len(t_list) # number of tests being performed

    for k in t_list:

        print(k)

        if term_field == 'burstiness_keywords':
            return_dates = return_keyword_dates(epets, k, date_field, term_field)
        elif term_field == 'metadata_theme':
            return_dates = return_metadata_theme_dates(epets, k, date_field, term_field, cflag)

        ts = create_ts(return_dates)
        B = B_par(ts)
        M = M_par(ts)
        
        BM_dict['term'].append(k)
        BM_dict['count'].append(len(return_dates))
        BM_dict['B'].append(B)
        BM_dict['M'].append(M)

        BM_dict['dates'].append([x.strftime("%Y-%m-%d") for x in return_dates])
        BM_dict['interevent-times'].append(ts)

        print(len(ts))

        Ms_shuffle = shuffle_ints(ts, N, len(ts))
        shuffle_pval = find_pval(Ms_shuffle, M)
        BM_dict['M-pval-shuffle'].append(shuffle_pval)
        BM_dict['M-shuffle-flag'].append(check_pval_sig(shuffle_pval, sig))
        BM_dict['M-shuffle-flag-bonf'].append(check_pval_sig_bonf(shuffle_pval, sig, m))

        # CHECK ABOUT THIS:
        # date_range = create_daterange(return_dates[0], return_dates[-1])
        date_range = create_daterange(min(return_dates), max(return_dates))
        # print(min(return_dates))
        # print(max(return_dates))
        b_date_samp_n = len(return_dates) - 2
        Bs_samp = random_samp_Bs(date_range, b_date_samp_n , N, len(date_range))
        Bs_pval_samp = find_pval(Bs_samp, B)
        BM_dict['B-pval-samp'].append(Bs_pval_samp)
        BM_dict['B-samp-flag'].append(check_pval_sig(Bs_pval_samp, sig))
        BM_dict['B-samp-flag-bonf'].append(check_pval_sig_bonf(Bs_pval_samp, sig, m))


        # date_range = create_daterange2(epets, date_field, return_dates[0], return_dates[-1])
        date_range = create_daterange2(epets, date_field,  min(return_dates), max(return_dates))
        b_date_samp_n = len(return_dates) - 2
        Bs_samp = random_samp_Bs(date_range, b_date_samp_n , N, len(date_range))
        Bs_pval_samp = find_pval(Bs_samp, B)
        BM_dict['B-pval-samp-obsdates'].append(Bs_pval_samp)
        BM_dict['B-samp-flag-obsdates'].append(check_pval_sig(Bs_pval_samp, sig))
        BM_dict['B-samp-flag-bonf-obsdates'].append(check_pval_sig_bonf(Bs_pval_samp, sig, m))
    
    return pd.DataFrame(BM_dict)