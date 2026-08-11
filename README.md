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
  Your computer's clock may decide that the current year is somewhere between 2023 and the Bronze Age.

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

## Roadmap

### 1.0.0 - Base Game

- [x] Procedural hardware generation
- [x] Seeds
- [x] Hardware failures (for everything except motherboard)
- [x] Salvage + Repair system
- [x] Inspection
- [x] Kernel panics
- [x] Terminal interface
- [ ] Fairness (will never be implemented)

### 1.0.1 - we need some color, and coolant, and a bit of conversion (ccc)

- [x] A neat .exe file so that you don't need Python anymore
- [ ] Color in the terminal
- [ ] AIO/fans errors
- [ ] Temperature in decimals
- [ ] Put you into a freezer thats inhabited with eldritch horrors (for cooling purposes)

### 1.0.2 - Cursed stuff and cursed curse-meter regulations and more cursed randomness

- [ ] A new shitload of cursed seeds
- [ ] Random things that can happen to make the game less fair (e.g. the PSU exploding and ending your run if the voltage is too high)
- [ ] Difficulty settings (probably)
- [ ] Get you a girlfriend (which will never happen)

### 1.0.3 - Quality of Life, or Quantity of Death
- [ ] RTC Fixing
- [ ] Proper leap-year handling
- [ ] Diagnostics consistency
- [ ] Realistic month lengths
- [ ] Command aliases (e.g. '?' for 'help' and 'diagnostics' for 'diag')
- [ ] Version and credits information command
- [x] Shove an asparagus down your esophagus /j
- [ ] And more...

### 1.1.0 - To be announced
- [x] To be announced

## License

(NO) POST-MORTEM is free and open-source software licensed under the GNU General Public License v3.0 (GPLv3).

You are free to use, study, modify, and redistribute this software, provided that your redistribution complies with the terms of the GPLv3.

See [LICENSE](https://github.com/frozystaysfrozen/NO-POST-MORTEM/blob/main/LICENSE) for more information

Copyright (C) frozystaysfrozen

The (C) is mine now >:3 /j
