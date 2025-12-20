#day35- Phase 4 Capstone Project
#reading a server log file, filtering error and warning logs into separate files

with open(r"server-log.txt",'r') as logfile:
    lines = logfile.readlines()

    with open(r"errorlines.log", 'a') as res:
     for row in lines:
        if "error" in row.lower():
                res.write(row)

    with open(r"warning.log", 'a') as caution:
        for row in lines:
            if "warning" in row.lower():
                caution.write(row)            