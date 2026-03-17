<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileNotice: Part of the Machines addon. -->

<div align="center">

# Machines: CNC Machine definitions submitted by the FreeCAD community

<!-- <img width="360" src="./Resources/Media/Header.webp" alt="Machines Header" /> -->

</div>

## About

Version 1.2 of FreeCAD introduced several important improvements to the CAM Workbench, notably **multi-axis operations** and **machine-based postprocessing**. 
Both features require an accurate digital representation of your physical CNC machine.

This addon provides a curated collection of community-created machine definitions available through the FreeCAD Addon Manager.

## Machine Definitions (.fcm)

Each machine definition is a JSON file with the `.fcm` extension. It contains:

- Kinematics and axis configuration
- Physical characteristics and working envelope
- The recommended postprocessor
- Configuration options for G-code customization

## FAQ

### 1) How do I contribute to this collection?

1. Create and test your machine definition in FreeCAD.
2. Fork this repository.
3. Place your `.fcm` file in the appropriate directory under 'machines'.
4. Open a Pull Request.

We welcome well-tested machines!

### 2) We want to make our own addon with just machines for our customers/users/students.  Can we make our machine definitions available in our own addon?

**Yes!** Fork this repository, customize the branding and content and curate the machines in 'machines' to your liking.  To make it available to your users, you have two choices:

1) You can publish it as your own addon through the FreeCAD Addon Manager

2) Provide your users the URL to the repo (github, gitlab, private, etc).  This can be added to the addon manager using the regular tools.

### 3) My machine isn't available here. How do I create it?

FreeCAD includes built-in tools for defining machines in the CAM workbench. Create the `.fcm` file (either through the UI or by editing JSON), test it thoroughly, and then consider submitting it back to the community.

### 4) None of the available postprocessors does what I need.

You have multiple paths forward:

- Enhance an existing postprocessor and submit a Pull Request to the [FreeCAD project](https://github.com/FreeCAD/FreeCAD)
- Develop a new postprocessor for the official FreeCAD repository
- Create a custom postprocessor and release it as a community addon
- Keep your postprocessor private for internal use

## Installation

**Recommended method:**

1. In FreeCAD, open **Tools → Addon Manager**
2. Search for "**Machines**"
3. Click **Install**

After installation (and a possible restart), your machines will be available in the CAM Job setup.

---

**Questions or suggestions?** Please open an [issue](https://github.com/FreeCAD/Machines/issues) on GitHub.
