import os
from binaryninja import *
import r2pipe

def run_plugin(bv, addr):
    func_start = addr.start
    
    #r2_path = '/home/ur_name_lols/bin/'
    #os.environ["PATH"] += os.pathsep + r2_path

    try:
        r2 = r2pipe.open(bv.file.original_filename)
        r2.cmd('aaa')
        r2.cmd('s ' + str(func_start))
        decompiled_func = r2.cmd('pdd')
        bv.show_html_report('Decompiled ' + addr.symbol.name, decompiled_func)
        r2.quit()
    except Exception as err:
        if str(err) == "ERROR: Cannot find radare2 in PATH":
            print("Please add the location of your radare2 binary to your PATH variable")
        else:
            print(err)

PluginCommand.register_for_function(
  "Decompile function",
  "Decompile function using r2dec", run_plugin)
