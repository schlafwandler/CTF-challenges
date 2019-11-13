import gdb

baseline = None
decrypted = None
start = None
size = None

class MonitorCodechangeEvent(gdb.Command):
    def __init__ (self):
        super (MonitorCodechangeEvent, self).__init__ ("monitor-codechange-event", gdb.COMMAND_USER)

    def invoke (self, arg, from_tty):
        inf = gdb.inferiors()[0]
        current = inf.read_memory(start,size)

        global baseline
        global decrypted
        for i in range(size):
            if current[i] != baseline[i]:
                decrypted[i] = current[i]

        #gdb.execute("c")
    
class MonitorCodechange(gdb.Command):
    """
    Take a baseline view of memory that can later be used by 'monitor-codechange-event'
    """
    def __init__ (self):
        super (MonitorCodechange, self).__init__ ("monitor-codechange", gdb.COMMAND_USER)

    def invoke (self, arg, from_tty):
        global start
        global size
        start, size = arg.split(" ")
        start = int(start,0)
        size = int(size,0)

        # get baseline
        inf = gdb.inferiors()[0]
        global baseline
        baseline = inf.read_memory(start,size)

        # initialise baseline copy 
        global decrypted
        decrypted = inf.read_memory(start,size)

class MonitorDump(gdb.Command):
    def __init__ (self):
        super (MonitorDump, self).__init__ ("monitor-dump", gdb.COMMAND_USER)
    def invoke (self, arg, from_tty):
        with open(arg,"wb") as f:
            f.write(decrypted.tobytes())

MonitorCodechange()
MonitorCodechangeEvent()
MonitorDump()
