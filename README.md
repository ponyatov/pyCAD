# ![](doc/logo.png) `pyCAD`
## 2D CAD for Electronics Design /Python/

github: https://github.com/ponyatov/pyCAD/tree/seek

- Copyright (C) 2020-2025 Dmitry Ponyatov <<dponyatov@gmail.com>> MIT
- Copyright (C) 2025 DeepSeek Chat (AI contributions)

## 🎨 Generic 2D CAD Capabilities
- **Precision Drawing Tools**
  - Primitive shapes (Line, Arc, Circle, Rectangle, Polygon)
  - Bézier curves/paths with control point editing
  - Dimensioning (Aligned, Angular, Radial, Leader)
  - Hatching/gradient fills with pattern libraries
  - Offset/pathing with variable tolerance
  - Layer stack with blend modes (16+ color palette)
  - Snap-to-grid/magnetic snapping (endpoint, midpoint, intersection)

## 🏗️ 2.5D Mechanical Design (3D Printing and CNC Milling)
- **Extrusion Tools**
  - Linear/tapered extrusion with draft angles
  - Path extrusion along vectors/splines
  - Parametric lofting between profiles

- **Fastener Systems**
  - Threaded hole wizard (ISO/ANSI standards)
  - Heat-set insert cavities
  - Snap-fit joint generator

- **Enclosure Design**
  - PCB auto-housing with configurable clearance
  - Ventilation pattern designer (hex/hole arrays)
  - Cable pass-through manager

## 🔌 Electronics-Specific Features
- **Schematic Capture**
  - KiCAD-compatible symbol libraries
  - Netlist generation with design rule checks
  - SPICE simulation integration (ngspice/XYCE)

- **PCB Design**
  - Interactive Dynamic Routing
  - Cross-Board Cabling
  - Gerber X2/Excellon import/export
  - 3D viewer with STEP model integration
  - Copper pour manager with thermal relief

## 💻 Embedded Development
- **Code Toolchain**
  - ARM/AVR GCC project templates
  - Linker script visualizer (memory map)
  - CMake/Makefile generator

- **Debugging**
  - GDB integration with register monitoring
  - Serial terminal with protocol decoding
  - Logic analyzer waveform viewer
