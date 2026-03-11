class bcolors:
    # --- Standard Colors ---
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # --- Bright/High Intensity Colors ---
    BRIGHT_BLACK = "\033[90m"  # Often looks like Dark Grey
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

    # --- Background Colors ---
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    # --- Text Styles ---
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    REVERSED = "\033[7m"  # Swaps foreground and background

    @classmethod
    def get_color_code(cls, name: str) -> str:
        name = name.upper()
        return getattr(bcolors, name) if hasattr(bcolors, name) else "WHITE"


# Usage
# print(bcolors.YELLOW + "Warning: This is a warning message." + bcolors.ENDC)
# print(f"{bcolors.BRIGHT_MAGENTA}Success: This is a success message!{bcolors.ENDC}")
