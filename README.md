## (NO) POST-MORTEM
The cursed PC diagnostics game where fixing one thing can break four other things.

And your CMOS battery predates the fall of the Roman Empire.

And your RAM is split in irregular quarters.

Well, if that isn't your style: you're a simpleton. 

We all need some chaos in our lives

## Features

* **Procedurally generated PCs**
  Every run generates different hardware, failures, diagnostics, temperatures, firmware versions, and other questionable decisions.

* **Seeded runs**
  Use seeds to reproduce specific machines. Some seeds are intentionally cursed.

* **Hardware diagnostics**
  Inspect the CPU, RAM, GPU, storage, PSU, motherboard, CMOS, and BIOS to figure out what went catastrophically wrong.

* **Hardware failures**
  Components can fail independently, while other components can become affected by the resulting hardware chaos.

* **GPU diagnostics**
  Check GPU model, VRAM, clock speed, temperature, PCIe interface, and initialization status.

* **HDD diagnostics**
  HDDs have rotational speeds, mechanical events, read errors, and, under sufficiently terrible circumstances, **clicking**.

* **CMOS/RTC corruption**
  Your computer's clock may decide that the current year is somewhere between 2026 and the Bronze Age.

* **Salvage system**
  Recover fragments of diagnostic information from a system that probably shouldn't still be talking to you.

* **Recovered logs**
  View whatever diagnostic records survived the computer's increasingly desperate attempts to die.

* **Subsystem exploration**
  Explore internal hardware subsystems. There is a non-zero chance that doing this makes everything worse.

* **Repairs**
  Attempt to repair faulty components and restore system integrity.

* **POST system**
  Repair the machine and attempt to pass POST. Fixing the wrong thing may accomplish approximately nothing.

* **System integrity**
  Your machine has an integrity percentage. Because apparently computers needed health bars.

* **Kernel panics**
  Sometimes the system simply gives up and throws a kernel panic.

* **Random corruption**
  Kernel panics can produce completely illegible garbage because apparently the emergency error handler also had a bad day.

* **The `reboot` command**
  It is dead.
  **Do not reboot.**

* **The `order_ram` command**
  No.

* **Cursed events**
  Some machines are simply beyond reasonable explanation.

* **Terminal-based interface**
  Currently powered by Python, `print()`, `input()`, and an irresponsible quantity of `pause()` calls.

