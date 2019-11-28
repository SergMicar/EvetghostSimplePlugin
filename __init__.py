# -*- coding: utf-8 -*-
#
# plugins/SimpleTV/__init__.py
#
# This file is a plugin for EventGhost.
# Copyright (C) 2005-2009 Lars-Peter Voss <bitmonster@eventghost.org>
#
# EventGhost is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License version 2 as published by the
# Free Software Foundation;
#
# EventGhost is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import eg

eg.RegisterPlugin(
    name = "SimpleTV",
    author = "Sergey V. Goncharov",
    version = "1.2." + "$LastChangedRevision: 1080 $".split()[1],
    kind = "program",
    guid = "{2847B12C-FB92-4F9E-A89E-81DD72669DB8}",
    createMacrosOnAdd = False,
    description = (
        'Adds actions to control the <a href="http://iptv.gen12.net">'
        'SimpleTV</a> IPTV multimedia application.'
    ),
    icon = (
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAC7klEQVR42qWTa0iTYRTH/+/uz"
    "uUFs6mo4KXSCDTTFLKiQBGkoiXrgwR9qA8lZhfDxLIiTKQiSUtQKFposmDiJWNpJWiZ2QdXXq"
    "dOy9wcOJ1zbW5urrMxBb/WAz84z3nP8+Phfc5h8J+LWQ8KGhMP+rCE8WwOK4HPFsQJ+NztDpf"
    "J1/LHqnHZecNm69yI08YZq74woaTyFcK5Ifisee2I9kuB3qSBxabH/NIUjHYtDOZZGG2/YHIO"
    "gO0AeFwRfHxYqLlkTJ1Vu9R01MwUKZIaSjM/SIW+/puuNqEbQGxooifOlzOokro8cZmSi5/DD"
    "nXdFZyh7SBT/ia7Jz06J43LESApKgdcNgdq/XvIv53Fjewpz6EShRhlEr0nLmpmsDKLhcd5KK"
    "FtO3OvLUMTsy0hsln1ABUnhhAetAu3WkPRMTKHrot28ARc1H+SIne/HCaLDnfehiGQhdWbEpS"
    "RQM6UtR92sMCDSqvEo5OjCAnYiWe9WWhRKVF1qg8RgfvQPXofB+KuYdKgRE1XFsJFwOUsVJCg"
    "nilu2mFehV6gNS6hUjKOYL9YvOjNQOtgJwqPVCMtJg+Tuh7EhKajf/ohmlSFCBHSq2WikgQyp"
    "vBV8A+ecDlet7SC8mPjEPvHQkaCDnUncnafxvG9so0f2/5diq8zr8FewkppLp5S6iVzXR7Wwx"
    "UupmkXrKjKMdMz+aKx/yg+jrUhOSIB5w4NbAga+tIwY+zDIr1yxXmPoJEpqBPd3RqxVmwwWXA"
    "1ox/hAckkyMTA7w4Ei3iUs8HusoLH+KC2Wwgny4pOGdSKWjwngcLdSEH5T/gt4khXqnnVjjXq"
    "r0A/QMQFHBQbqeeYNaqiNggQAMNfoK+9jXbKvCO63AIqRXTsHkYSEOxKEUchUkwvxedTng5ZL"
    "XAatFjWTmFep4FeO41Zqh8iegnN+iyQG2IizH0jIpDY4pW7l51YJhYJA6Ej5gjbxjB554Lnlb"
    "nhEyzvN/fg2LxDZPMKXZum8V/XX7yzG1mzdIOwAAAAAElFTkSuQmCC"
    ),
)
    
# Changelog:
# ----------
# 2015-01-31
#     * initial version
# 2015-02-11
#     * Add some ACTION MESS.
#     * increased version to 1.1
# 2016-09-21
#     * Fix cyr bug.
#     * increased version to 1.2
# 2016-09-27 rev.1073
#     * Fix "MyTheathre" intersection.
#     * move some "ok" flags to top group
# 2016-09-28 rev.1075
#     * add FavChannel action
# 2016-10-13 rev.1077
#     * add PiP Sound on/off
# 2017-02-12 rev.1079
#     * add FAV_TOGGLE
# 2018-08-12 rev.1080
#     * FAV_TOGGLE changed action ID (for compatibility 0.5)
#     * PiP Sound on/off changed action ID (for compatibility 0.5)

import _winreg
from eg.WinApi import FindWindow, SendMessageTimeout
from win32api import ShellExecute

process_name = "tv.exe"
process_path = "C:\Program Files (x86)\simpleTV"
Win_Class = "VSG_simple_tv_Prog00_H3B"
WM_EXECUTE_ACTION_MESS = 1056

class MsgAction(eg.ActionClass):
    def __call__(self):
        try:
             hWnd = eg.plugins.Window.FindWindow(process_name, None, None, None, None, None, False, 0.0, 0)
             return eg.plugins.Window.SendMessage(WM_EXECUTE_ACTION_MESS, self.value, 0, 0)
        except:
            raise self.Exceptions.ProgramNotRunning



class ExeAction(eg.ActionClass):
    def __call__(self):
        try:
            ShellExecute(0, None, process_name, self.value, process_path, 0)
            return True
        except:
            raise self.Exceptions.ProgramNotFound


MyActionList = (
(eg.ActionGroup, 'GroupCommon', 'Common Functions  (ok)', None,
  (
    (MsgAction, 'PausePlay',                 'Pause/Play',                                  None, 54),
    (MsgAction, 'PauseExlusive',             'Pause Exlusive',                              None, 121), # from up to v0.4.8 b8
    (MsgAction, 'PlayExlusive',              'Play Exlusive',                               None, 120), # from up to v0.4.8 b8
    (MsgAction, 'Forward',                   'Forward /Increase Speed/',                    None, 55),  #SHORTCUT_FF
    (MsgAction, 'ForwardHighSpeed',          'Forward High Speed',                          None, 82),  #SHORTCUT_FF High Speed
    (MsgAction, 'Rewind',                    'Rewind /Decrease Speed/ - only to 0.25',      None, 56),  #SHORTCUT_RW
    (MsgAction, 'NormalSpeed',               'Normal Speed',                                None, 75),
    (MsgAction, 'JumpForward',               'Jump Forward',                                None, 57),
    (MsgAction, 'JumpLongForward',           'Jump Forward long',                           None, 59),
    (MsgAction, 'JumpBack',                  'Jump Back',                                   None, 58),
    (MsgAction, 'JumpLongBack',              'Jump Back long',                              None, 60),
    (MsgAction, 'Play',                      'Play (restart play)',                         None, 63),
    (MsgAction, 'Stop',                      'Stop',                                        None, 11),
    (MsgAction, 'ChannelUp',                 'Channel UP',                                  None, 103),
    (MsgAction, 'ChannelDown',               'Channel DOWN',                                None, 102),
    (MsgAction, 'PiPCannelUp',               'PiP Cannel UP',                               None, 9),
    (MsgAction, 'PiPCannelDown',             'PiP Cannel DOWN',                             None, 8),
    (MsgAction, 'PageChannelUp',             'Page OSD Channel UP',                         None, 77),
    (MsgAction, 'PageChannelDown',           'Page OSD Channel DOWN',                       None, 78),
    (MsgAction, 'ChannelListOSD',            'Channel List on OSD on/off',                  None, 6),
    (MsgAction, 'FavChannel',                'Favorite Channel on/off',                     None, 95),
	(MsgAction, 'FavToggle',                 'Favorite Toggle',                             None, 133), # добавить/удалить канал из фаворитов
    (MsgAction, 'ChannelTechInfo',           'Channel tech. Info on OSD',                   None, 65),
    (MsgAction, 'PrevChannel',               'Switch to Previous Channel',                  None, 2),
    (MsgAction, 'RefreshPlaylist',           'Refresh Playlist - ?',                        None, 115),  # нет реакции, нужно уточнять, может не замечаю
  )
),
(eg.ActionGroup, 'GroupCursor', 'Cursor keys  (ok)', None,
  (
    (MsgAction, 'Right',                     'Cursor Right',                                None, 0),
    (MsgAction, 'Left',                      'Cursor Left',                                 None, 1),
    (MsgAction, 'Up',                        'Cursor Up',                                   None, 3),
    (MsgAction, 'Down',                      'Cursor Down',                                 None, 4),
    (MsgAction, 'Enter',                     'Enter',                                       None, 5),
    (MsgAction, 'Escape',                    'Escape/Return',                               None, 37),
  )
),
(eg.ActionGroup, 'GroupScreen', 'Screen control', None,
  (
    (MsgAction, 'BrightnessUp',              'Brightness Up - ok',                          None, 19),
    (MsgAction, 'BrightnessDown',            'Brightness Down - ok',                        None, 20),
    (MsgAction, 'ContrastUp',                'Contrast Up - ok',                            None, 21),
    (MsgAction, 'ContrastDown',              'Contrast Down - ok',                          None, 22),
    (MsgAction, 'SaturationUp',              'Saturation Up - ok',                          None, 23),
    (MsgAction, 'SaturationDown',            'Saturation Down - ok',                        None, 24),
    (MsgAction, 'HueUp',                     'Hue Up - ok 1/2',                             None, 25),   # работает ок, но через раз
    (MsgAction, 'HueDown',                   'Hue Down - ok 1/2',                           None, 26),   # работает ок, но через раз
    (MsgAction, 'GammaUp',                   'Gamma Up - ok 1/2',                           None, 27),   # работает ок, но через раз
    (MsgAction, 'GammaDown',                 'Gamma Down - ok 1/2',                         None, 28),   # работает ок, но через раз
	(MsgAction, 'SharpUp',                   'SharpUp - ok 1/2',                            None, 70),   # работает ок, но через раз
    (MsgAction, 'SharpDown',                 'Sharp Down - ok 1/2',                         None, 71),   # работает ок, но через раз
    (MsgAction, 'Crop',                      'Crop - ok',                                   None, 41),
    (MsgAction, 'Format',                    'Format - ok',                                 None, 17),
    (MsgAction, 'Deinterlacing',             'Deinterlacing  - ok',                         None, 16),
   )
),
(eg.ActionGroup, 'GroupWindowControl', 'Window controls  (ok)', None,
  (
    (MsgAction, 'Minimize',                  'Minimize TV window (toggle)',                 None, 73),
	(MsgAction, 'ToTray',                    'TV to tray',                                  None, 32),
    (MsgAction, 'TVWindowOverAll',           'TV window over all (toggle)',                 None, 74),
    (MsgAction, 'FullScreen',                'Full Screen (toggle)',                        None, 14),
  )
),
(eg.ActionGroup, 'GroupREC', 'Rec', None,
  (
    (MsgAction, 'QRecord',                   'QRec current channel (trigger start/stop if configure) - ok', None, 15),
    (MsgAction, 'QRecordPiP',                'QRec PiP channel (only start) - ok',          None, 42),
	(MsgAction, 'RecordDump',                'Rec current channel (trigger start/stop if configure) - ok', None, 106),
	(MsgAction, 'ShowCurrentRec',            'Show Current Rec on OSD',                     None, 84),   #Duplicated in "OSD"
	(MsgAction, 'StopLastRec',               'Stop Last Rec',                               None, 86),
    (MsgAction, 'Snapshot',                  'Snapshot - ok',                               None, 83),
  )
),
(eg.ActionGroup, 'GroupPiP', 'Picture in Picture Functions  (ok)', None,
  (
    (MsgAction, 'PiP',                       'PiP on/off',                                  None, 7),
	(MsgAction, 'PiPSwap',                   'Swap: PiP <-> Main screen',                   None, 10),
	(MsgAction, 'PiPSound',                  'PiP Sound on/off (switch)',                   None, 132),
    (MsgAction, 'MultiPiP',                  'Multi PiP on/off',                            None, 64),
    (MsgAction, 'PiPpos',                    'Set PiP position (lu-ru-rd-ld-center)',       None, 33),
    (MsgAction, 'PiPZoomUp',                 'Zoom UP PiP',                                 None, 66),
    (MsgAction, 'PiPZoomDown',               'Zoom DOWN PiP',                               None, 67),
    (MsgAction, 'KEY_PREVIEW_PIP',           'KEY_PREVIEW_PIP - ?',                         None, 119), # нет реакции, нужно уточнять, может не замечаю
  )
),
(eg.ActionGroup, 'GroupOSD', 'OSD Channel/Functions', None,
  (
    (MsgAction, 'Showtime',                  'Showtime - ok',                               None, 31),
    (MsgAction, 'InfoCurProgram',            'Info Current Program - ok',                   None, 36),
    (MsgAction, 'TeleGuideCurProgram',       'TeleGuide Current Program - ok',              None, 38),
    (MsgAction, 'ShowCurrentRec',            'Show Current Rec on OSD',                     None, 84), #Duplicated in "REC"
	(MsgAction, 'CurChanOptionOSD',          'Show Current Channel Option on OSD - ok',     None, 96),
	(MsgAction, 'AudioTrackOptionOSD',       'Show AudioTrack Option on OSD - ok',          None, 88),
    (MsgAction, 'VideoTrackOptionOSD',       'Show VideoTrack Option on OSD - ok',          None, 89),
    (MsgAction, 'SubTitlesTrackOptionOSD',   'Show SubTitlesTrack Option on OSD - ok',      None, 90),
    (MsgAction, 'DeinterlaceTrackOptionOSD', 'Show DeinterlaceTrack Option on OSD - ok',    None, 91),
    (MsgAction, 'CropTrackOptionOSD',        'Show CropTrack Option on OSD - ok',           None, 92),
    (MsgAction, 'FromatTrackOptionOSD',      'Show FormatTrack Option on OSD - ok',         None, 93),
    (MsgAction, 'Home',                      'Home - ?',                                    None, 80),
    (MsgAction, 'End',                       'End - ?',                                     None, 81),
  )
),
(eg.ActionGroup, 'GroupSound', 'Sound (ok)', None,
  (
    (MsgAction, 'Mute',                      'Mute - ok',                                   None, 13), #SHORTCUT_MUTE
    (MsgAction, 'VolumeUP',                  'Volume UP - ok',                              None, 61),
    (MsgAction, 'VolumeDOWN',                'Volume DOWN - ok',                            None, 62),
	(MsgAction, 'SoundStereoType',           'SoundStereoType (Toggle) - ?',                None, 97), # нет реакции, нужно уточнять, может не замечаю
	
  )
),
(eg.ActionGroup, 'GroupPowerControl', 'Power control', None,
  (
    (ExeAction, 'StartSimpleTV',             'Start SimpleTV - to develop',                 None, 0),
    (MsgAction, 'ExitSimpleTV',              'Exit SimpleTV - ok',                          None, 12), #SHORTCUT_EXIT
    (MsgAction, 'TimerSleep',                'SleepTimer set - ok',                         None, 98),
    (MsgAction, 'SleepNow',                  'do Sleep now - ok',                           None, 68),
    (MsgAction, 'TimerSleepExit',            'SleepTimer (Exit from SimpleTV only - ok',    None, 107),
    (MsgAction, 'KEY_REBOOT_COMP',           'KEY_REBOOT_COMP',                             None, 113),
    (MsgAction, 'KEYSHUTDOWN',               'KEYSHUTDOWN',                                 None, 85),
	
  )
),
(eg.ActionGroup, 'GroupNumpad', 'NumPad (ok)', None,
  (
    (MsgAction, 'Number0',                   'KeyNumber 0',                                 None, 43),
    (MsgAction, 'Number1',                   'KeyNumber 1',                                 None, 44),
    (MsgAction, 'Number2',                   'KeyNumber 2',                                 None, 45),
	(MsgAction, 'Number3',                   'KeyNumber 3',                                 None, 46),
	(MsgAction, 'Number4',                   'KeyNumber 4',                                 None, 47),
	(MsgAction, 'Number5',                   'KeyNumber 5',                                 None, 48),
	(MsgAction, 'Number6',                   'KeyNumber 6',                                 None, 49),
	(MsgAction, 'Number7',                   'KeyNumber 7',                                 None, 50),
	(MsgAction, 'Number8',                   'KeyNumber 8',                                 None, 51),
	(MsgAction, 'Number9',                   'KeyNumber 9',                                 None, 52),
	(MsgAction, 'DigAmount',                 'Digit amount' ,                               None, 53),
  )
),
(eg.ActionGroup, 'GroupExtWin', 'ExtWin', None, #Все команды находящиеся в группе открываются в отдельном окне
  (
    (MsgAction, 'OPTIONS',                   'Options - ok',                                None, 69),  # настройки тех. информация о потоке
    (MsgAction, 'MEDIAINFO',                 'Media|Channel Info - ok',                     None, 114), # тех. информация о потоке
	(MsgAction, 'KEY_TOGGLE_MEDIATYPE',      'KEY_TOGGLE_MEDIATYPE',                        None, 114),
	(MsgAction, 'OpenFile',                  'Open File - ok',                              None, 104),
    (MsgAction, 'OpenURL',                   'Open URL - ok',                               None, 105),
  )
),
(eg.ActionGroup, 'GroupOther', 'Other', None,
  (
    (MsgAction, 'CTRL_PRESS',                'Press CONTROL key - ?',                       None, 1),
    (MsgAction, 'SHIFT_PRESS',               'Press SHIFT key - ?',                         None, 2),
    (MsgAction, 'ControlPanel',              'On/Off Control Panel - ok',                   None, 72),
    (MsgAction, 'UpdateAllProg',             'EPG.Update TVguide for all channels - ok',    None, 39),
    (MsgAction, 'UpdateOneProg',             'EPG.Update TVguide for current channel - ok', None, 40),

    
    (MsgAction, 'KEY_TOGGLE_SHORT_PROGRAMM', 'KEY_TOGGLE_SHORT_PROGRAMM',                   None, 76),
    (MsgAction, 'KEYVIDEOTRACKTOGGLE',       'KEYVIDEOTRACKTOGGLE',                         None, 87),
	
    (MsgAction, 'KEY_OSD_TOGGLE_QPROG',      'KEY_OSD_TOGGLE_QPROG',                        None, 94),

    (MsgAction, 'KEY_ADD_BOOKMARK',          'KEY_ADD_BOOKMARK',                            None, 99),
    (MsgAction, 'KEY_SHOW_BOOKMARK_OSD',     'KEY_SHOW_BOOKMARK_OSD',                       None, 100),
    (MsgAction, 'KEY_SHOW_EXTFILTER_OSD',    'KEY_SHOW_EXTFILTER_OSD',                      None, 101),
    (MsgAction, 'KEY_OSD_MULTIADRESS_SHOW',  'KEY_OSD_MULTIADRESS_SHOW - ?',                None, 108), # нет реакции, нужно уточнять, может не замечаю
    (MsgAction, 'KEY_TOGGLE_PLAY_MODE',      'KEY_TOGGLE_PLAY_MODE',                        None, 109),
    (MsgAction, 'KEY_TOGGLE_PLAY_MODE_STOP_ON_ERROR', 'KEY_TOGGLE_PLAY_MODE_STOP_ON_ERROR', None, 110),
    (MsgAction, 'KEY_OPEN_FROM_CLIPBOARD',   'KEY_OPEN_FROM_CLIPBOARD',                     None, 112),
    (MsgAction, 'KEY_CHAPTER_SHOW_OSD',      'KEY_CHAPTER_SHOW_OSD',                        None, 116),
    (MsgAction, 'KEY_CHAPTER_NEXT',          'KEY_CHAPTER_NEXT',                            None, 117),
    (MsgAction, 'KEY_CHAPTER_PREV',          'KEY_CHAPTER_PREV',                            None, 118),
    (MsgAction, 'KEY_STRACK',                'KEY_STRACK',                                  None, 18),
    (MsgAction, 'KEYMAS_UP',                 'KEYMAS_UP',                                   None, 29),
    (MsgAction, 'KEYMAS_DOWN',               'KEYMAS_DOWN',                                 None, 30),
    (MsgAction, 'KEY_COMPACT_MODE',          'KEY_COMPACT_MODE - ?',                        None, 34),  # нет реакции, нужно уточнять, может не замечаю
    (MsgAction, 'KEY_SHOW_CANNEL',           'KEY_SHOW_CANNEL - ?',                         None, 35),  # нет реакции, нужно уточнять, может не замечаю
  )
),
                )

			
class SimpleTV(eg.PluginClass):

    def __init__(self):
        self.AddActionsFromList(MyActionList)


    def __start__(self):
		  print "SimpleTV window messages plug-in is started!"
##        try:
##            key = _winreg.OpenKey(
##                _winreg.HKEY_LOCAL_MACHINE,
##                "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\SimpleTV"
##            )
##            self.myTVPath, dummy = _winreg.QueryValueEx(key, "InstallLocation")
##        except WindowsError:
##            self.PrintError("SimpleTV installation path not found!")
##            self.myTVPath = ""