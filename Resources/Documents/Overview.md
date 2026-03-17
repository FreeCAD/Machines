<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileNotice: Part of the Machines addon.. -->

# Machines: CNC Machine definitions submitted by the FreeCAD community

<!-- <img width = '300' src = '../Media/Header.webp' /> -->

<div align="center">

CNC Machine definitions submitted by the FreeCAD community

</div>

## About

Version 1.2 of FreeCAD introduced several important improvements to the CAM Workbench, notably **multi-axis operations** and **machine-based postprocessing**.
Both features require an accurate digital representation of your physical CNC machine.

This addon provides a curated collection of community-created machine definitions.

## Machine Definitions (.fcm)

Each machine definition is a JSON file with the `.fcm` extension. It contains:

- Kinematics and axis configuration
- Physical characteristics and working envelope
- The recommended postprocessor
- Configuration options for G-code customization

## How to use this Addon.

*NOTE* This addon has no GUI controls, workbench, or menus.  You will see no change in FreeCAD or the CAM workbench.
Once installed, go to Preferences->CAM->Assets.

Create a new machine.
Expand the 'template' combobox to see all available templates. This addon will provide a new folder populated with the available machine definitions.
Using a contributed template will make a copy which you can further customize to your liking.

## FAQ

### 1) How do I contribute to this collection?

We welcome well-tested machines!
To contribute a machine definition to this collection, visit the repository at https://github.com/FreeCAD/Machines
There you'll find detailed instructions on contributing.

### 2) We are a company/makerspace/club/school. Can we make our machine definitions available in our own addon?

**Yes!** Detailed instructions are also available at the addon repo (link above)

### 3) My machine isn't available here. How do I create it?
Creating machine definitions is documented at [actually not documented yet but coming soon]
