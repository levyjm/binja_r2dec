import os
import r2pipe
from binaryninja import show_html_report, PluginCommand
from pygments import highlight
from pygments.lexers import CLexer
from pygments.formatters import HtmlFormatter
from pygments.styles.native import NativeStyle

def show_output(bv, func_name, decompiled):
    lexer = CLexer()
    style = NativeStyle()
    style.background_color = '#272811'
    formatter = HtmlFormatter(full=True, style='native', noclasses=True)
    colored_code = highlight(decompiled, lexer, formatter)
    bv.show_html_report('Decompiled ' + func_name, colored_code)

def run_plugin(bv, addr):
    func_start = addr.start
    
    #r2_path = '/home/username/bin/'
    #os.environ["PATH"] += os.pathsep + r2_path

    try:
        r2 = r2pipe.open(bv.file.original_filename)
        r2.cmd('aaa')
        r2.cmd('s ' + str(func_start))
        decompiled_func = r2.cmd('pdd')
        if decompiled_func.startswith('Error: no data available'):
            r2.cmd('af @ ' + str(func_start))
            decompiled_func = r2.cmd('pdd')
        show_output(bv, addr.symbol.name, decompiled_func)
        r2.quit()
    except Exception as err:
        if str(err) == "ERROR: Cannot find radare2 in PATH":
            print("Please add the location of your radare2 binary to your PATH variable")
        else:
            print(err)

PluginCommand.register_for_function(
  "Decompile function",
  "Decompile function using r2dec", run_plugin)

