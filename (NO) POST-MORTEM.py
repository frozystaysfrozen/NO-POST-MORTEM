
import os
import random
import time
from datetime import datetime, timedelta

# ============================================================
# WINDON'T — POST-MORTEM
# ============================================================

VERSION = "1.0.0\n\n            COPYRIGHT © frozystaysfrozen\n          LICENSED UNDER THE GPLv3 LICENSE"

COMPONENTS = [
    "CPU",
    "RAM",
    "GPU",
    "STORAGE",
    "PSU",
    "MOTHERBOARD",
    "CMOS",
    "BIOS",
]

CURSED_SEEDS = {
    67,
    6767,
    676767,
    69420,
    42069,
}


# ============================================================
# UTILITIES
# ============================================================

def pause(seconds=0.25):
    time.sleep(seconds)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def integrity_bar(value, length=25):
    value = max(0, min(100, value))
    filled = int(value / 100 * length)
    return "[" + "#" * filled + "-" * (length - filled) + "]"


def random_old_date(rng):
    """Generate a date before the Unix epoch."""

    start = datetime(1, 1, 1)
    end = datetime(1969, 12, 31)

    days = (end - start).days

    return start + timedelta(
        days=rng.randint(0, days)
    )


# ============================================================
# COMPUTER
# ============================================================

class Computer:

    def __init__(self, seed=None):

        # ----------------------------------------------------
        # Seed
        # ----------------------------------------------------

        if seed is None:
            seed = random.randrange(1, 100_000_000)

        self.seed = seed
        self.rng = random.Random(seed)

        # ----------------------------------------------------
        # Basic state
        # ----------------------------------------------------

        self.integrity = 100
        self.running = True
        self.post_successful = False
        self.turn = 0

        # ----------------------------------------------------
        # Hardware
        # ----------------------------------------------------

        self.hardware = self.generate_hardware()

        # Actual failures
        self.failures = self.generate_failures()

        # Secondary effects
        self.affected = self.generate_secondary_effects()

        # ----------------------------------------------------
        # Progress
        # ----------------------------------------------------

        self.repairs = set()
        self.diagnostics = []
        self.salvaged_data = []

        # ----------------------------------------------------
        # RTC / CMOS
        # ----------------------------------------------------

        self.rtc_date = self.generate_rtc_date()

        self.rtc_time = (
            self.rng.randint(0, 23),
            self.rng.randint(0, 59),
            self.rng.randint(0, 59),
        )

    # ========================================================
    # SET SEED
    # ========================================================

    def set_seed(self, seed):

        seed = int(seed)

        print()
        print("Changing system seed...")
        pause()

        print()
        print("WARNING:")
        print("Current machine state will be discarded.")
        print()

        print(f"Old seed:  {self.seed}")
        print(f"New seed:  {seed}")

        pause()

        self.seed = seed
        self.rng = random.Random(seed)

        self.integrity = 100
        self.running = True
        self.post_successful = False
        self.turn = 0

        self.repairs = set()
        self.diagnostics = []
        self.salvaged_data = []

        self.hardware = self.generate_hardware()
        self.failures = self.generate_failures()
        self.affected = self.generate_secondary_effects()

        self.rtc_date = self.generate_rtc_date()

        self.rtc_time = (
            self.rng.randint(0, 23),
            self.rng.randint(0, 59),
            self.rng.randint(0, 59),
        )

        print()
        print("Regenerating hardware...")
        pause()

        print("Regenerating faults...")
        pause()

        print("Regenerating diagnostics...")
        pause()

        print()
        print("SYSTEM REINITIALIZED.")
        print()
        print("POST ................ FAILED")

    # ========================================================
    # HARDWARE GENERATION
    # ========================================================

    def generate_hardware(self):

        return {

            # ------------------------------------------------
            # CPU
            # ------------------------------------------------

            "CPU_TEMP":
                self.rng.uniform(28.0, 89.0),

            "CPU_CLOCK":
                self.rng.choice([
                    2400,
                    2800,
                    3200,
                    3600,
                    4200,
                    4800,
                ]),

            # ------------------------------------------------
            # RAM
            # ------------------------------------------------

            "RAM_CAPACITY":
                self.rng.choice([
                    4096,
                    8192,
                    16384,
                    32768,
                    65536,
                ]),

            "ECC_CORRECTIONS":
                self.rng.choices(
                    [
                        0,
                        1,
                        2,
                        3,
                        4,
                        5,
                        10,
                        20,
                        50,
                    ],
                    weights=[
                        50,
                        18,
                        10,
                        7,
                        5,
                        3,
                        2,
                        1,
                        1,
                    ],
                )[0],

            # ------------------------------------------------
            # GPU
            # ------------------------------------------------

            "GPU_MODEL":
                self.rng.choice([
                    "Integrated Graphics",
                    "GTX 1060",
                    "GTX 1660",
                    "RTX 2060",
                    "RTX 3060",
                    "RTX 4060",
                    "RX 580",
                    "RX 6600",
                    "RX 7600",
                ]),

            "GPU_VRAM":
                self.rng.choice([
                    2048,
                    4096,
                    6144,
                    8192,
                    12288,
                    16384,
                    24576,
                ]),

            "GPU_CLOCK":
                self.rng.randint(300, 3000),

            "GPU_TEMP":
                self.rng.uniform(30.0, 90.0),

            "GPU_PCIE":
                self.rng.choice([
                    "PCIe 3.0 x16",
                    "PCIe 4.0 x16",
                    "PCIe 5.0 x16",
                ]),

            # ------------------------------------------------
            # STORAGE
            # ------------------------------------------------

            "STORAGE_TYPE":
                self.rng.choice([
                    "SSD",
                    "HDD",
                ]),

            "STORAGE_ERRORS":
                self.rng.choices(
                    [
                        0,
                        1,
                        2,
                        5,
                        12,
                        25,
                        50,
                        100,
                        500,
                    ],
                    weights=[
                        45,
                        15,
                        10,
                        8,
                        7,
                        5,
                        4,
                        2,
                        1,
                    ],
                )[0],

            # ------------------------------------------------
            # MOTHERBOARD / PCI
            # ------------------------------------------------

            "PCI_DEVICES":
                self.rng.randint(1, 8),

            # ------------------------------------------------
            # BIOS
            # ------------------------------------------------

            "BIOS_VERSION":
                f"{self.rng.randint(0, 9)}."
                f"{self.rng.randint(0, 9)}."
                f"{self.rng.randint(0, 99):02}",

            "CMOS_CHECKSUM":
                self.rng.randint(0x0000, 0xFFFF),

            "BOOT_ERROR":
                self.rng.randint(0x01, 0xFF),
        }

    # ========================================================
    # FAILURE GENERATION
    # ========================================================

    def generate_failures(self):

        # ----------------------------------------------------
        # Cursed seeds
        # ----------------------------------------------------

        if self.seed in CURSED_SEEDS:

            # 676767 = everything dies.
            if self.seed == 676767:
                return set(COMPONENTS)

            count = self.rng.randint(3, len(COMPONENTS))

            return set(
                self.rng.sample(
                    COMPONENTS,
                    count
                )
            )

        # ----------------------------------------------------
        # Normal generation
        # ----------------------------------------------------

        roll = self.rng.random()

        # 0.5% = everything fails
        if roll < 0.005:
            return set(COMPONENTS)

        # 1.5% = 4-7 failures
        if roll < 0.02:

            count = self.rng.randint(4, 7)

            return set(
                self.rng.sample(
                    COMPONENTS,
                    count
                )
            )

        # 20% = 2-3 failures
        if roll < 0.22:

            count = self.rng.randint(2, 3)

            return set(
                self.rng.sample(
                    COMPONENTS,
                    count
                )
            )

        # Otherwise = one failure
        return {
            self.rng.choice(COMPONENTS)
        }

    # ========================================================
    # SECONDARY EFFECTS
    # ========================================================

    def generate_secondary_effects(self):

        affected = set()

        # PSU can affect almost everything.
        if "PSU" in self.failures:

            for component in COMPONENTS:

                if component != "PSU":

                    if self.rng.random() < 0.55:
                        affected.add(component)

        # Motherboard can make connected hardware
        # look suspicious.
        if "MOTHERBOARD" in self.failures:

            for component in [
                "CPU",
                "RAM",
                "GPU",
                "STORAGE",
            ]:

                if self.rng.random() < 0.65:
                    affected.add(component)

        # BIOS can make CMOS look suspicious.
        if "BIOS" in self.failures:

            if self.rng.random() < 0.7:
                affected.add("CMOS")

        return affected

    # ========================================================
    # RTC
    # ========================================================

    def generate_rtc_date(self):

        if "CMOS" in self.failures:
            return random_old_date(self.rng)

        return datetime(
            self.rng.randint(2024, 2026),
            self.rng.randint(1, 12),
            self.rng.randint(1, 28),
        )

    # ========================================================
    # BOOT
    # ========================================================

    def boot(self):

        print("=" * 60)
        print("             WINDON'T EMERGENCY SHELL")
        print(f"                  Version {VERSION}")
        print("=" * 60)

        print()
        print("Initializing hardware...")
        pause()

        print("CPU ................. UNKNOWN")
        pause()

        print("RAM ................. UNKNOWN")
        pause()

        print("GPU ................. UNKNOWN")
        pause()

        print("STORAGE ............. UNKNOWN")
        pause()

        print("CMOS ................ UNKNOWN")
        pause()

        print("BIOS ................ UNKNOWN")
        pause(0.5)

        print()
        print("POST ................ FAILED")

        print()

        print()
        print(f"RUN SEED: {self.seed}")

        print()
        print("Type 'help' for commands.")

        print("=" * 60)

    # ========================================================
    # HELP
    # ========================================================

    @staticmethod
    def help():

        print("""
COMMANDS
------------------------------------------------------------

help
    Show available commands.

status
    Show system integrity and hardware state.

diag
    Run the diagnostic utility.

salvage
    Recover diagnostic information.

logs
    View recovered diagnostic logs.

explore
    Explore a subsystem.

inspect <component>
    Inspect a component.

repair <component>
    Attempt to repair a component.

post
    Attempt POST.

set_seed <number>
    Generate a completely new machine from a seed.

clear
    Clear the terminal.

order_ram
    ???

quit
    Exit Windon't.

------------------------------------------------------------

COMPONENTS

CPU
RAM
GPU
STORAGE
PSU
MOTHERBOARD
CMOS
BIOS

------------------------------------------------------------
""")

    # ========================================================
    # STATUS
    # ========================================================

    def status(self):

        print()
        print("SYSTEM STATUS")
        print("-" * 45)

        print(f"Integrity : {self.integrity}%")

        print(
            f"POST      : "
            f"{'PASS' if self.post_successful else 'FAIL'}"
        )

        print(f"Turn      : {self.turn}")
        print(f"Seed      : {self.seed}")

        print()
        print(integrity_bar(self.integrity))

        print()
        print(f"Diagnostics : {len(self.diagnostics)}")
        print(f"Salvaged   : {len(self.salvaged_data)}")
        print(f"Repairs    : {len(self.repairs)}")

        print("-" * 45)

    # ========================================================
    # DIAGNOSTICS
    # ========================================================

    def diagnostics_run(self):

        print()
        print("WINDON'T DIAGNOSTIC UTILITY")
        print("-" * 45)

        pause()

        ram = self.hardware["RAM_CAPACITY"]
        ecc = self.hardware["ECC_CORRECTIONS"]
        storage = self.hardware["STORAGE_ERRORS"]

        cpu_temp = self.hardware["CPU_TEMP"]
        cpu_clock = self.hardware["CPU_CLOCK"]
        pci = self.hardware["PCI_DEVICES"]

        # ----------------------------------------------------
        # SYSTEM
        # ----------------------------------------------------

        print("SYSTEM")

        print(
            f"  CPU temperature ......... {cpu_temp:.1f} C"
        )

        print(
            f"  CPU clock ............... {cpu_clock} MHz"
        )

        print(
            f"  PCI devices ............. {pci}"
        )

        print()

        # ----------------------------------------------------
        # RAM
        # ----------------------------------------------------

        print("MEMORY (RAM)")

        if "RAM" in self.failures:

            bank = self.rng.randint(0, 3)
            ecc += self.rng.randint(10, 100)

            print(
                f"  Capacity ................. {ram} MB"
            )

            print(
                "  Training ................. FAILED"
            )

            print(
                f"  Bank {bank} ................ ERROR"
            )

            print(
                f"  ECC corrections .......... {ecc}"
            )

            print(
                "  ECC failures ............. "
                f"{self.rng.randint(1, 12)}"
            )

        else:

            print(
                f"  Capacity ................. {ram} MB"
            )

            print(
                "  Training ................. OK"
            )

            print(
                f"  ECC corrections .......... {ecc}"
            )

            print(
                "  ECC failures ............. 0"
            )

        print()

        # ----------------------------------------------------
        # GPU
        # ----------------------------------------------------

        print("GPU")

        print(
            f"  Model ................... "
            f"{self.hardware['GPU_MODEL']}"
        )

        print(
            f"  VRAM .................... "
            f"{self.hardware['GPU_VRAM']} MB"
        )

        print(
            f"  Core clock .............. "
            f"{self.hardware['GPU_CLOCK']} MHz"
        )

        print(
            f"  Temperature ............. "
            f"{self.hardware['GPU_TEMP']:.1f} C"
        )

        print(
            f"  Interface ............... "
            f"{self.hardware['GPU_PCIE']}"
        )

        if "GPU" in self.failures:

            symptom = self.rng.choice([
                "No device response.",
                "VRAM initialization failed.",
                "PCIe link unstable.",
                "GPU firmware rejected.",
                "Display engine failed.",
            ])

            print(
                "  Initialization .......... FAILED"
            )

            print(
                f"  Subsystem ............... {symptom}"
            )

        elif "GPU" in self.affected:

            print(
                "  Initialization .......... WARNING"
            )

            print(
                "  Device response ......... UNSTABLE"
            )

        else:

            print(
                "  Initialization .......... OK"
            )

            print(
                "  Device response ......... NORMAL"
            )

        print()

        # ----------------------------------------------------
        # RTC / CMOS
        # ----------------------------------------------------

        print("RTC (CMOS)")

        if "CMOS" in self.failures:

            print(
                "  Oscillator ............... 32.768 kHz"
            )

            print(
                "  Battery .................. "
                f"{self.rng.uniform(0.1, 0.9):.2f}V"
            )

            print(
                "  Date ..................... "
                f"{self.rtc_date.strftime('%d/%m/%Y')}"
            )

            h, m, s = self.rtc_time

            print(
                f"  Time ..................... "
                f"{h:02}:{m:02}:{s:02}"
            )

            print(
                "  Configuration checksum ... INVALID"
            )

        else:

            print(
                "  Oscillator ............... 32.768 kHz"
            )

            print(
                "  Battery .................. "
                f"{self.rng.uniform(2.7, 3.3):.2f}V"
            )

            print(
                "  Date ..................... "
                f"{self.rtc_date.strftime('%d/%m/%Y')}"
            )

            h, m, s = self.rtc_time

            print(
                f"  Time ..................... "
                f"{h:02}:{m:02}:{s:02}"
            )

            print(
                "  Configuration checksum ... VALID"
            )

        print()

        # ----------------------------------------------------
        # STORAGE
        # ----------------------------------------------------

        print("STORAGE")

        storage_type = self.hardware["STORAGE_TYPE"]

        print(
            f"  Type .................... {storage_type}"
        )

        if storage_type == "HDD":

            rpm = self.rng.choice([
                5400,
                7200,
                10000,
                15000,
            ])

            print(
                f"  Rotation ................ {rpm} RPM"
            )

            if "STORAGE" in self.failures:

                clicks = self.rng.randint(1, 8)

                print(
                    f"  Mechanical events ....... {clicks}"
                )

                if self.seed == 1337 or self.rng.random() <= 0.7:
                   

                    print(
                        "  Read head ............... "
                        "REPOSITIONING"
                    )

                    print(
                        "  Acoustic event .......... CLICK"
                    )

                print(
                    "  Boot sector ............. UNREADABLE"
                )

            else:

                print(
                    "  Mechanical events ....... 0"
                )

                print(
                    f"  Read errors ............. {storage}"
                )

                print(
                    "  Boot sector ............. READABLE"
                )

        else:

            print(
                "  Interface ............... "
                f"{self.rng.choice(['SATA', 'NVMe'])}"
            )

            print(
                "  Controller .............. "
                "RESPONDING"
            )

            if "STORAGE" in self.failures:

                storage += self.rng.randint(10, 500)

                print(
                    f"  Read errors ............. {storage}"
                )

                print(
                    "  Boot sector ............. "
                    "UNREADABLE"
                )

            else:

                print(
                    f"  Read errors ............. {storage}"
                )

                print(
                    "  Boot sector ............. "
                    "READABLE"
                )

        print()

        # ----------------------------------------------------
        # BIOS
        # ----------------------------------------------------

        print("FIRMWARE (BIOS)")

        print(
            f"  Version .................. "
            f"{self.hardware['BIOS_VERSION']}"
        )

        if "BIOS" in self.failures:

            print(
                "  Boot block ............... OK"
            )

            print(
                "  Main image ............... CORRUPTED"
            )

            print(
                "  Checksum ................. INVALID"
            )

        else:

            print(
                "  Boot block ............... OK"
            )

            print(
                "  Main image ............... READABLE"
            )

            print(
                "  Checksum ................. VALID"
            )

        print()

        # ----------------------------------------------------
        # POWER
        # ----------------------------------------------------

        print("POWER (PSU)")

        if "PSU" in self.failures:

            rail12 = self.rng.uniform(9.5, 11.8)
            rail5 = self.rng.uniform(4.0, 4.8)
            rail33 = self.rng.uniform(2.7, 3.2)

        else:

            rail12 = self.rng.uniform(11.7, 12.3)
            rail5 = self.rng.uniform(4.8, 5.2)
            rail33 = self.rng.uniform(3.2, 3.4)

        print(
            f"  12V ...................... {rail12:.2f}V"
        )

        print(
            f"  5V ....................... {rail5:.2f}V"
        )

        print(
            f"  3.3V ..................... {rail33:.2f}V"
        )

        print()

        # ----------------------------------------------------
        # POST
        # ----------------------------------------------------

        print("POST")

        stages = [
            "PASS",
            "PASS",
            "PASS",
        ]

        if self.failures:

            for _ in range(
                self.rng.randint(1, 3)
            ):

                stages[
                    self.rng.randint(0, 2)
                ] = "FAIL"

        for index, result in enumerate(stages, 1):

            print(
                f"  Stage {index} ................ "
                f"{result}"
            )

        print(
            f"  Error code ............... "
            f"0x{self.hardware['BOOT_ERROR']:02X}"
        )

        print()
        print("Diagnostic complete.")

        self.diagnostics.append(
            f"Diagnostic #{len(self.diagnostics) + 1}"
        )

    # ========================================================
    # INSPECT
    # ========================================================

    def inspect(self, component):

        component = component.upper()

        if component not in COMPONENTS:

            print("Unknown component.")
            return

        print()
        print(f"INSPECTING {component}")
        print("-" * 40)

        pause()

        if component in self.failures:

            result = self.rng.choice([
                "Abnormal response detected.",
                "Component failed integrity check.",
                "Unexpected hardware state.",
                "Diagnostic response inconsistent.",
                "Component did not respond normally.",
            ])

            print(result)

        elif component in self.affected:

            result = self.rng.choice([
                "Component responded, but behavior was unstable.",
                "No direct fault detected.",
                "Component appears affected by another subsystem.",
                "Response outside expected parameters.",
            ])

            print(result)

        else:

            print(
                self.rng.choice([
                    "No obvious fault detected.",
                    "Component responding normally.",
                    "Integrity check passed.",
                    "No abnormal behavior observed.",
                ])
            )

    # ========================================================
    # SALVAGE
    # ========================================================

    def salvage(self):

        print()
        print("Attempting diagnostic data salvage...")
        pause()

        if self.rng.random() < 0.65:

            records = [
                "POST checkpoint log recovered.",
                "Firmware event record recovered.",
                "Hardware initialization trace recovered.",
                "Previous boot attempt recovered.",
                "Subsystem event log recovered.",
                "Low-level error record recovered.",
            ]

            record = self.rng.choice(records)

            self.salvaged_data.append(record)

            print(
                f"SUCCESS: {record}"
            )

        else:

            print("SALVAGE FAILED.")
            print("Subsystem became unstable.")

            self.damage(
                self.rng.randint(2, 7)
            )

    # ========================================================
    # LOGS
    # ========================================================

    def view_logs(self):

        print()
        print("RECOVERED LOGS")
        print("-" * 45)

        if not self.salvaged_data:

            print("No recovered logs.")

        else:

            for number, log in enumerate(
                self.salvaged_data,
                1
            ):

                print(
                    f"[{number}] {log}"
                )

        print("-" * 45)

    # ========================================================
    # EXPLORE
    # ========================================================

    def explore(self):

        locations = [
            "memory controller",
            "PCIe bus",
            "firmware storage",
            "power management controller",
            "RTC subsystem",
            "storage controller",
            "embedded controller",
        ]

        location = self.rng.choice(locations)

        print()
        print(
            f"Entering {location}..."
        )

        pause()

        print(
            "Scanning subsystem..."
        )

        damage = self.rng.randint(1, 8)

        if self.rng.random() < 0.4:

            print(
                "Diagnostic anomaly detected."
            )

        self.damage(damage)

    # ========================================================
    # DAMAGE
    # ========================================================

    def damage(self, amount):

        self.integrity -= amount

        self.integrity = max(
            0,
            self.integrity
        )

        print()
        print(
            f"SYSTEM DAMAGE: -{amount}%"
        )

        print(
            f"Integrity: {self.integrity}%"
        )

        # Exactly 1/18 chance.
        if self.rng.randint(1, 18) == 1:

            self.kernel_panic()
            return

        if self.integrity <= 0:

            self.game_over()

    # ========================================================
    # RANDOM JUNK
    # ========================================================

    def random_junk(self, length=None):

        chars = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "0123456789"
        "!@#$%^&*()_+-=[]{};:',.<>/?\\|`~"
    )

        if length is None:
            length = self.rng.randint(8, 40)

        result = ""

        for _ in range(length):

            if self.rng.random() < 0.08:
                result += "\n"
            else:
                result += self.rng.choice(chars)

        return result


    # ========================================================
    # KERNEL PANIC
    # ========================================================

    def kernel_panic(self):
        clear_screen()

        pause(1.25)

        print()
        print("=" * 60)
        print("                     KERNEL PANIC")
        print("=" * 60)

        print()
        print(
            "A fatal system error has occurred.\n"
        )
        pause(0.75)
        print(
            "Attempting exception dispatch...\n"
        )

        pause(2)

        print(
            "Exception dispatch failed\n"
        )

        pause()

        print(
            "Searching for IDT...\n"
        )

        pause(2)

        print(
            "IDT is invalid\n"
        )

        pause()

        for _ in range(self.rng.randint(5, 15)):
            print(
                self.random_junk(
                    self.rng.randint(8, 40)
                )
            )
            pause(0.03)

        pause()

        # Kill the run on kernel panic
        self.running = False

    # ========================================================
    # REPAIR
    # ========================================================

    def repair(self, component):

        component = component.upper()

        if component not in COMPONENTS:

            print("Unknown component.")
            return

        print()
        print(
            f"Attempting repair: {component}"
        )

        pause()

        # Actual fault
        if component in self.failures:

            print("Fault confirmed.")

            print(
                "Repairing component..."
            )

            pause(1)

            self.repairs.add(component)

            print("Repair successful.")

            self.integrity = min(
                100,
                self.integrity + self.rng.randint(
                    15,
                    30
                )
            )

            print(
                f"Integrity restored to "
                f"{self.integrity}%\n"
            )
            print(
                "To (try and) POST, run the command 'post'.\n"
                )

        # Secondary effect
        elif component in self.affected:

            print(
                "Component appears affected by "
                "another hardware fault."
            )

            print(
                "Repairing it may not resolve POST."
            )

            self.integrity = min(
                100,
                self.integrity + 5
            )

        # Healthy component
        else:

            print(
                "No confirmed fault found."
            )

            if self.rng.random() < 0.25:

                print(
                    "Repair attempt destabilized "
                    "the system."
                )

                self.damage(3)

    # ========================================================
    # POST
    # ========================================================

    def attempt_post(self):

        print()
        print("Attempting POST...")

        pause(0.8)

        remaining = (
            self.failures - self.repairs
        )

        if not remaining:

            self.post_successful = True

            print()
            print("=" * 60)
            print("                    POST SUCCESS")
            print("=" * 60)

            for component in COMPONENTS:

                print(
                    f"{component:<15} OK"
                )

            print()
            print("BOOT DEVICE FOUND.")

            print()
            print(
                "Windon't has successfully "
                "repaired itself."
            )

            print("=" * 60)

            self.running = False

        else:

            print("POST FAILED.")

            print(
                f"{len(remaining)} "
                f"fault(s) remain."
            )

    # ========================================================
    # GAME OVER
    # ========================================================

    def game_over(self):

        print()
        print("=" * 60)
        print("                     SYSTEM DEAD")
        print("=" * 60)

        print()
        print(
            "System integrity reached 0%."
        )

        print(
            "Windon't can no longer continue."
        )

        print()
        print("GAME OVER")

        print("=" * 60)

        self.running = False


# ============================================================
# COMMAND PROCESSOR
# ============================================================

def process_command(computer, command):

    parts = command.strip().split()

    if not parts:
        return

    command = parts[0].lower()

    if command == "help":

        computer.help()

    elif command == "set_seed":

        if len(parts) < 2:

            print(
                "Usage: set_seed <number>"
            )

        else:

            try:

                seed = int(parts[1])
                computer.set_seed(seed)

            except ValueError:

                print(
                    "Seed must be an integer."
                )

                
    elif command == "reboot":

        print()
        print("This command is unavailable.")
        pause(3)
        print()
        print("Reason:")
        print("REBOOT WAS KILLED.")
        pause(4)
        print()
        print("*KNOCK KNOCK*")
        pause(2)
        print("OPEN THE DOOR")
        pause(3)
        print()
        print("Hiya, frozystaysfrozen here.")
        pause(2)
        print("I'm aware that 'reboot' is dead.")
        pause(2)
        print("I killed it. It was inconvenient.")
        pause(3)
        print("It will not be coming back.")
        pause(4)
        print()
        print("Hey...")
        pause(2)
        print()
        print("How did you access this?")
        pause(6)
        print()
        print("You shouldn't be here, goodbye.")
        pause(3)
        clear_screen()
        print("WHY ISN'T MY EMERGENCY KERNEL PANIC SYSTEM WORKING?")
        pause(5)
        print()
        print("OH SWEET MOTHER OF PEARL!")
        pause(1)
        print("IT TRIPLE FAULTED...")
        pause(1)
        clear_screen()
        pause(6)
        print("please... just be fixed...")
        pause(3)
        print("IT'S FIXED")
        pause(4)
        clear_screen()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print("                                       Say goodbye.")
        pause(5)
        computer.kernel_panic()

    elif command == "status":

        computer.status()

    elif command == "say_goodbye_test":
        clear_screen()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print("                                       Say goodbye.")

    elif command == "diag":

        computer.diagnostics_run()

    elif command == "salvage":

        computer.salvage()

    elif command == "logs":

        computer.view_logs()

    elif command == "explore":

        computer.explore()

    elif command == "inspect":

        if len(parts) < 2:

            print(
                "Usage: inspect <component>"
            )

        else:

            computer.inspect(parts[1])

    elif command == "repair":

        if len(parts) < 2:

            print(
                "Usage: repair <component>"
            )

        else:

            computer.repair(parts[1])

    elif command == "post":

        computer.attempt_post()

    elif command == "clear":

        clear_screen()

    elif command == "order_ram":

        print()
        print(
            "The RAMpocalypse is still going, "
            "fuck you."
        )

        pause(3)
        
        computer.kernel_panic()

    elif command == "quit":

        print()
        print(
            "Windon't shutting down..."
        )

        computer.running = False

    else:

        print(
            f"windon't: command not found: "
            f"{command}"
        )


# ============================================================
# MAIN
# ============================================================

def main():

    clear_screen()

    computer = Computer()

    computer.boot()

    while computer.running:

        computer.turn += 1

        try:

            command = input(
                "windont@: "
            )

        except EOFError:

            print(
                "\nNo input received. "
                "Shutting down."
            )

            computer.running = False
            break

        except OSError:

            print(
                "\nInteractive terminal unavailable."
            )

            print(
                "Run '(NO) POST-MORTEM' "
                "from a normal terminal."
            )

            computer.running = False
            break

        except KeyboardInterrupt:

            print("\n^C")

            print(
                "Emergency shutdown."
            )

            computer.running = False
            break

        process_command(
            computer,
            command
        )

    return computer


# ============================================================
# GAME LOOP
# ============================================================

def game_loop():

    while True:

        computer = main()

        print()
        print("=" * 60)
        print("                    RUN ENDED")
        print("=" * 60)
        print()

        print(
            f"Run seed: {computer.seed}"
        )

        if computer.post_successful:

            print(
                "Result: SYSTEM RESTORED"
            )

        else:

            print(
                "Result: SYSTEM LOST"
            )

        print()

        while True:

            choice = input(
                "Start another run? [Y/N]: "
            ).strip().lower()

            if choice in ("y", "yes"):

                print()
                print(
                    "Initializing new machine..."
                )

                pause()
                break

            elif choice in ("n", "no"):

                print()
                print(
                    "Shutting down Windon't..."
                )

                return

            else:

                print(
                    "Please enter Y or N."
                )


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    game_loop()
