def load_schedule(file_to_load):
    import cPickle as pickle
    with open(file_to_load, 'r') as loadfile:
        unpickled_schedule = pickle.load(loadfile)
        return unpickled_schedule


def view_schedule(file_to_load):
    from datetime import datetime,timedelta
    schedule = load_schedule(file_to_load)['schedule_mat']
    schedule_list = []
    for idx,val in enumerate(schedule):
        try:
            if schedule[idx][1] != schedule[idx-1][1]:
                sec = timedelta(seconds = val[0])
                d = datetime(1,1,1) + sec
                schedule_list.append(["%d:%d" % (d.hour, d.minute),val[1]])
        except:
            break
    for item in schedule_list:
        print item
