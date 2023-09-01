import sys
from openpyxl import Workbook
import json
import time
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
                print(f"parts 0: <{parts[0]}>")
                if "id" in parts[0]:
                    pass
                elif "\"date\"" == parts[0].strip():
                    st = ':'.join(part for part in parts[1:])
                    sts = st.strip(",.\t\n")
                    parts_list.append(sts)
                    print(f"Date: <{sts}>")
                elif "\"owner\"" == parts[0].strip():
                    st = ':'.join(part for part in parts[1:])
                    sts = st.strip(",.\t\n")
                    parts_list.append(sts)
                    print(f"Owner: <{sts}>")
                elif "\"name\"" == parts[0].strip():
                    st = ':'.join(part for part in parts[1:])
                    sts = st.strip(",.\t\n")
                    parts_list.append(sts)
                    print(f"name: <{sts}>")
                elif "\"desc\"" == parts[0].strip():
                    st = ':'.join(part for part in parts[1:])
                    sts = st.strip(",.\t\n")
                    parts_list.append(sts)
                    print(f"desc: <{sts}>")
                elif "\"t\"" == parts[0].strip():
                    st = ':'.join(part for part in parts[1:])
                    sts = st.strip(",.\t\n")
                    parts_list.append(sts)
                    print(f"t: <{sts}>")
                elif "\"se\"" == parts[0].strip():
                    st = ':'.join(part for part in parts[1:])
                    sts = st.strip(",.\t\n")
                    parts_list.append(sts)
                    print(f"se: <{sts}>")
                    print(f"parts_list: <{parts_list}>")
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
    


if __name__ == "__main__":
    sel_dict, msg_dict = get_raw_data()
    #print(f"sel_dict: {sel_dict}")
    #print(f"msg_dict: {msg_dict}")
    for k,v in sel_dict.items():
        print(f"Key: {k}: Value {v}")
        time.sleep(1)



