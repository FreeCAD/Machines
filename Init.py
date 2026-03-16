# SPDX-License-Identifier: CC-BY-SA-4.0
# SPDX-FileNotice: Part of the Machines addon.

import os
import sys
import FreeCAD

_addon_dir = None
try:
    _addon_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    for _candidate in [
        os.path.join(FreeCAD.getUserAppDataDir(), "Mod", "Machines"),
        os.path.join(FreeCAD.getHomePath(), "Mod", "Machines"),
    ]:
        if os.path.isdir(_candidate):
            _addon_dir = _candidate
            break

if _addon_dir is not None:
    try:
        import Path.Preferences
        Path.Preferences.addAddonAssetPath(_addon_dir)
    except AttributeError:
        _posts_dir = os.path.join(_addon_dir, "posts")
        if os.path.isdir(_posts_dir) and _posts_dir not in sys.path:
            sys.path.insert(0, _posts_dir)
        FreeCAD.Console.PrintLog(
            "Machines addon: Path.Preferences.addAddonAssetPath not available. "
            "Upgrade FreeCAD to enable machine definition discovery.\n"
        )
