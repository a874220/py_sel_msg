import sys
from openpyxl import Workbook
import json
import time
import datetime
import pdb


def get_raw_data():

    sel_dict = {}
    msg_dict = {}

    if len(sys.argv) < 3:
        print("Usage: py_sel_msg <sel_js_file> <msg_js_file>")
        sys.exit(1)
    else:
        #pdb.set_trace()
        print(f"Input sel: {sys.argv[1]}, Input msg: {sys.argv[2]}")
        with open(sys.argv[1], 'r') as sel:
            id = 0
            parts_list = []
            for line in sel:
                parts = line.split(':')
                #print(f"parts 0: <{parts[0]}>")
                if "id" in parts[0]:
                    pass
                elif "\"date\"" == parts[0].strip():
                    st = ':'.join(part for part in parts[1:])
                    sts = st.strip(",.\t\n")
                    parts_list.append(sts)
                    #print(f"Date: <{sts}>")
                elif "\"owner\"" == parts[0].strip():
                    st = ':'.join(part for part in parts[1:])
                    sts = st.strip(",.\t\n")
                    parts_list.append(sts)
                    #print(f"Owner: <{sts}>")
                elif "\"name\"" == parts[0].strip():
                    st = ':'.join(part for part in parts[1:])
                    sts = st.strip(",.\t\n")
                    parts_list.append(sts)
                    #print(f"name: <{sts}>")
                elif "\"desc\"" == parts[0].strip():
                    st = ':'.join(part for part in parts[1:])
                    sts = st.strip(",.\t\n")
                    parts_list.append(sts)
                    #print(f"desc: <{sts}>")
                elif "\"t\"" == parts[0].strip():
                    st = ':'.join(part for part in parts[1:])
                    sts = st.strip(",.\t\n")
                    parts_list.append(sts)
                    #print(f"t: <{sts}>")
                elif "\"se\"" == parts[0].strip():
                    st = ':'.join(part for part in parts[1:])
                    sts = st.strip(",.\t\n")
                    parts_list.append(sts)
                    #print(f"se: <{sts}>")
                    #print(f"parts_list: <{parts_list}>")
                    sel_dict[id] = parts_list
                    parts_list = []
                    id += 1
                    continue
                    #print(st.rstrip(),end=" ")
                else:
                    #print("\n") 
                    pass 

        with open(sys.argv[2], 'r') as msg:
            id = 0
            parts_list = []
            for line in msg:
                parts = line.split(':')
                if "id" in parts[0]:
                    pass
                elif "date" in parts[0]:
                    st = ':'.join(part for part in parts[1:])
                    parts_list.append(st.strip(",'\t\n"))
                    #print(st.rstrip(),end=" ")
                elif "event_type" in parts[0]:
                    st = ':'.join(part for part in parts[1:])
                    parts_list.append(st.strip(",.\t\n"))
                    #print(st.rstrip(),end="")
                elif "desc" in parts[0]:
                    st = ':'.join(part for part in parts[1:])
                    parts_list.append(st.strip(",.\t\n"))
                    msg_dict[id] = parts_list
                    parts_list = []
                    id += 1
                    continue
                    #print(st.rstrip(),end=" ")
                else:
                    #print("\n") 
                    pass 
                
    return sel_dict, msg_dict


def fix_json(jfile):
    print("fix json called")
    #line_num = 0
    #for line in jfile.readlines():
    #    line_num = line_num + 1
    #    if line_num == 1 and "g_data0" in line:
    #        print(f"Line: {line}")
    #        i=0
    #        for c in line:
    #            if c != '{':
    #                i = i+1
    #            else:
    #                break
    #        print(f"i seems to be {i}")
    #        break
    #            
    

def get_datetime(val_list):
    newt = val_list[0].strip("\"")
    return datetime.datetime.strptime(newt, '%Y-%m-%d %H:%M:%S')


if __name__ == "__main__":
    sel_dict, msg_dict = get_raw_data()
    #print(f"sel_dict: {sel_dict}")
    #print(f"msg_dict: {msg_dict}")
    print(f"Sel entries: {len(sel_dict.items())}")
    print(f"Msg entries: {len(msg_dict.items())}")
    sel_iter =  iter(sel_dict.values())
    msg_iter =  iter(msg_dict.values())
    current_sel_val = next(sel_iter)
    current_msg_val = next(msg_iter)
    print(f"Sel 0: {current_sel_val}")
    print(f"Msg 0: {current_msg_val}")
    current_sel_time = get_datetime(current_sel_val)
    current_msg_time = get_datetime(current_msg_val)
    print(f"Sel 0 dt: {current_sel_time}")
    print(f"Msg 0 dt: {current_msg_time}")
    loop_sel = True
    loop_msg = True
    while loop_sel or loop_msg:
        if loop_sel and loop_msg:
            if current_sel_time <= current_msg_time:
                print("sel time less than msg time")
                while current_sel_time <= current_msg_time:
                    print(f"current_sel_val: {current_sel_val}")
                    try: 
                        current_sel_val = next(sel_iter)
                        current_sel_time = get_datetime(current_sel_val)
                    except StopIteration:
                        loop_sel = False
                        print("No more sel values")
                        break
            else:
                print("sel time greater than msg time")
                while current_msg_time < current_sel_time:
                    print(f"current_msg_val: {current_msg_val}")
                    try:
                        current_msg_val = next(msg_iter)
                        current_msg_time = get_datetime(current_msg_val)
                    except StopIteration:
                        loop_msg = False
                        print("No more msg values")
                        break
        elif loop_sel and not loop_msg:
            while loop_sel:
                try: 
                    current_sel_val = next(sel_iter)
                    current_sel_time = get_datetime(current_sel_val)
                    print(f"current_sel_val: {current_sel_val}")
                except StopIteration:
                    loop_sel = False
                    print("No more sel values")
                    break
        elif not loop_sel and loop_msg:
            while loop_msg:
                try: 
                    current_msg_val = next(msg_iter)
                    current_msg_time = get_datetime(current_msg_val)
                    print(f"current_msg_val: {current_msg_val}")
                except StopIteration:
                    loop_msg = False
                    print("No more msg values")
                    break
        else:
            break
