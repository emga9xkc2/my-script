#!/usr/bin/env vpython3
import os
import gc
d = "~/appdata/roaming"
roaming = os.path.abspath(os.path.expanduser(d))
top = os.path.join(os.getcwd(),  "bin")
top = roaming + r"\nightowl\cef\bin"
# os.chdir(top)

# cefdataroot = os.path.join(os.getcwd(), "bin-cefdata")
cefdataroot = top + "\\bin-cefdata\\"
for fname in (
    cefdataroot,
    os.path.join(cefdataroot, "root"),
    os.path.join(cefdataroot, "root", "cache"),
    os.path.join(cefdataroot, "user-data"),
):
    if not os.path.isdir(fname):
        os.mkdir(fname)

import ctypes as ct
from . import libcefdef

libcefdef.LoadLibrary(os.path.join(top, "libcef" + libcefdef.dllext))
from . import libcef as cef


c_byte_p = ct.POINTER(ct.c_byte)
debug2 = False

def CefMainArgs(argv):
    argb = [ct.create_string_buffer(s.encode("ascii")) for s in argv[1:]]
    ubp = ct.POINTER(ct.c_ubyte)
    cargv = (ubp * (len(argb) + 1))()
    for i in range(len(argb)):
        v = argb[i]
        cargv[i] = ct.cast(v, ubp)
    cargv[len(argb)] = None
    data = cef.cef_main_args_t()
    data.argc = len(argb)
    data.argv = ct.cast(cargv, ct.POINTER(ubp))
    return data, (argb, cargv)


class App(cef.cef_app_t):
    def __init__(self, switches=None):
        super().__init__()
        self.bph = cef.cef_browser_process_handler_t()
        self.switches = switches

    def py_on_before_command_line_processing(self, this, processType, commandLine):
        if debug2:
            print("App.OnBeforeCommandLineProcessing")
        #v = processType
        #print('\tprocessType==',v, bool(v))
        #v = processType.contents
        #if v is not None:
        #    v = v.ToString()
        #print("processType=", v)
        def showcl():
            cl = commandLine.contents
            #print('\tcl.valid=', cl.is_valid(cl))
            if cl.is_valid(cl):
                s = cl.get_command_line_string(cl)
                s = ct.cast(s, ct.POINTER(cef.cef_string_userfree_t))
                v = s.contents.ToString(True)
                if debug2:
                    print("\tcommandLine=", v)
                s.contents.Free()
        # self.switches = True
        if self.switches:
            cl = commandLine.contents
            def cladd(s1, s2=None):
                # print('cladd', s1, '*', s2)

                s1 = cef.cef_string_t(s1)
                if s2 is None:
                    cl.append_switch(cl, s1)
                else:
                    s2 = cef.cef_string_t(s2)
                    cl.append_switch_with_value(cl, s1, s2)
            for sw in self.switches:
                if type(sw) == str:  
                    if "=" in sw:
                        sw = sw.split("=")  
                        cladd(sw[0], sw[1])          
                    else:        
                        cladd(sw)
                else:
                    cladd(sw[0], sw[1])

        #cladd("enable-media-stream")
        #cladd("autoplay-policy", "no-user-gesture-required")
        #cladd("enable-media-stream")
        #cladd("disable-dev-shm-usage") # https://github.com/GoogleChrome/puppeteer/issues/1834
        #cladd("enable-begin-frame-scheduling") # https://bitbucket.org/chromiumembedded/cef/issues/1368

        # Optimize for no gpu usage
        #cladd("disable-gpu")
        #cladd("disable-gpu-compositing")

        #cladd("remote-debugging-port", "9921")
        # cladd("force-device-scale-factor", "1")

        showcl()
        return None

    # def OnRegisterCustomSchemes(self, this, registrar):
    def py_on_register_custom_schemes(self, this, registar):
        if debug2:
            print("App.OnRegisterCustomSchemes", registar)
        return None

    # def GetResourceBundleHandler(self, this):
    def py_get_resource_bundle_handler(self, this):
        return None
        print("App.GetResourceBundleHandler")

    # def GetBrowserProcessHandler(self, this):
    def py_get_browser_process_handler(self, this):
        if debug2:
            print("App.GetBrowserProcessHandler")
        v = ct.addressof(self.bph)
        return v

    # def GetRenderProcessHandler(self, this):
    def py_get_render_process_handler(self, this):
        if debug2:
            print("App.GetRenderProcessHandler")
        return None


class AppSetup:
    def __init__(self, app, *args, logfile ="cef.log"):
        if not logfile:
            logfile = "cef.log"
        if not logfile.endswith(".log"):
            logfile = logfile + ".log"
        if debug2:
            print("*" * 20, "AppSetup")
        if libcefdef.win:
            mainArgs = cef.cef_main_args_t()
            mainArgs.instance = ct.windll.kernel32.GetModuleHandleA(None)
            mainArgsB = None
        else:
            mainArgs, mainArgsB = CefMainArgs(args)

        # command_line = libcef.command_line_create()
        # command_line.contents._init_from_string(command_line, cef_string_t("--show-fps-counter"))

        settings = cef.cef_settings_t()
        settings.size = ct.sizeof(cef.cef_settings_t)
        # settings.no_sandbox = 1
        settings.browser_subprocess_path = cef.cef_string_t(
            os.path.normpath(os.path.join(top, "cefclient"))
#            os.path.normpath(os.path.join(os.getcwd(), "build", "pyhelper"))
        )
        # settings.framework_dir_path = 
        settings.chrome_runtime = 0
        # settings.multi_threaded_message_loop = 1
        # settings.external_message_pump = 1
        # settings.windowless_rendering_enabled = 1
        # command_line_args_disabled
        # cache_path
        #settings.resources_dir_path = cef.cef_string_t(os.path.normpath(os.path.join(top, 'Resources')))
        settings.locales_dir_path = cef.cef_string_t(os.path.normpath(os.path.join(top, 'locales')))
        settings.remote_debugging_port = 20480
        settings.root_cache_path = cef.cef_string_t(os.path.join(cefdataroot, "root"))
        settings.cache_path = cef.cef_string_t(os.path.join(cefdataroot, "root", "cache"))
        settings.user_data_path = cef.cef_string_t(os.path.join(cefdataroot, "user-data"))
        settings.log_file = cef.cef_string_t(os.path.join(cefdataroot, logfile))
        settings.log_severity = cef.LOGSEVERITY_DEBUG
        #settings.log_severity = cef.LOGSEVERITY_DEFAULT
        settings.uncaught_exception_stack_size = 200

        self.mainArgs = mainArgs
        self.mainArgsB = mainArgsB
        self.settings = settings
        self.app = app

    def ShowSettings(self):
        if debug2:
            print('*'*20, 'settings:')
        for fname, ftype in self.settings._fields_:
            v = getattr(self.settings, fname)
            if ftype == cef.cef_string_t:
                v = str(v)
            if debug2:
                print('    {} = {}'.format(fname, v))

    def Execute(self):
        if debug2:
            print('cef.cef_execute_process', self.mainArgs, self.app, None)
        rc = cef.cef_execute_process(self.mainArgs, self.app, None)
        if debug2:
            print("libcef.execute_process rc=", rc)
        if rc != -1:
            return rc
        if debug2:
            print("libcef.initialize")
        cef.cef_initialize(self.mainArgs, self.settings, self.app, None)
        if debug2:
            print("/libcef.initialize")

    def Cleanup(self):
        if debug2:
            print("finish")
        gc.collect()
        if debug2:
            print("libcef.shutdown")
        cef.cef_shutdown()
        if debug2:
            print("done")
