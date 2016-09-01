import datetime
import time as t
import json
import os
from analyzer import check_cross_against_schedule, check_training_or_testing_against_schedule
import http_poster

def add_param(param, program, ard_val, schedule_a):
    if param == "program":
        return program
    if param == "datetime":
        date_handler = lambda obj: (
            obj.isoformat()
            if isinstance(obj, datetime.datetime)
            or isinstance(obj, datetime.date)
            else None)
        return str(json.dumps(datetime.datetime.now(), default=date_handler))
    if param == 'ard_sensor':
        return ard_val
    if param == 'correct?':
        if check_cross_against_schedule(ard_val, schedule_a) == "correct":
            return True
        elif check_cross_against_schedule(ard_val, schedule_a) == "incorrect":
            return False 
        elif check_cross_against_schedule(ard_val, schedule_a) == "off":
            return None
    if param == 'training?':
        if check_training_or_testing_against_schedule(schedule_a) == "testing":
            return True
        if check_training_or_testing_against_schedule(schedule_a) == "training":
            return False
        if check_training_or_testing_against_schedule(schedule_a) == "off":
            return None
        
class Data_handler():
    def __init__(self, experiment, schedule_a, schedule_b):
        self.save_file_name = experiment.save_file_name
        self.save_model = experiment.save_model
        self.program_name = experiment.program
        self.line_to_save = []
        self.schedule_a = schedule_a

    def ard_grab_and_tag_data(self, arduino_sensor):
        self.line_to_save = []
        val_from_ard= arduino_sensor.read()
        if val_from_ard:
            for item in self.save_model:
                self.line_to_save.append(add_param(item, self.program_name, val_from_ard, self.schedule_a))
            self.line_to_save = {"exp_name": self.line_to_save[0],
                                     "box":self.line_to_save[1],
                                     "datetime" : self.line_to_save[2],
                                     "correct":self.line_to_save[3],
                                     "testing":self.line_to_save[4]}
            http_poster.post_data(self.line_to_save)    
            print self.line_to_save
        t.sleep(0.1)
            
