# engine.py
# The core Araw dispatch system. 
# It's basically a fancy switch-case that thinks it's better than you.

class ArawInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        
        # Central Dictionary: Add new keywords here!
        self.command_map = {
            "lvar": self.handle_lvar,
            "emit": self.handle_emit,
            "lfunc": self.handle_lfunc,
        }

    def handle_lvar(self, args):
        # Handles: lvar name = value
        if " = " in args:
            name, val = [part.strip() for part in args.split(" = ", 1)]
            # Clean up the value
            clean_val = val.strip('"')
            self.variables[name] = clean_val

    def handle_emit(self, args):
        # Handles: emit(variable) or emit("string")
        content = args.strip("() ")
        # If it's a variable, get it; otherwise, just print the literal
        print(self.variables.get(content, content.strip('"')))

    def handle_lfunc(self, args):
        # Handles: lfunc name()
        func_name = args.split("(")[0].strip()
        self.functions[func_name] = "REGISTERED"
        print(f"System: Function '{func_name}' has been trapped in the registry.")

    def run_line(self, line):
        line = line.strip()
        if not line or line.startswith("--"):
            return

        # Special case: 'emit(' doesn't have a space after 'emit'
        if line.startswith("emit("):
            self.handle_emit(line[5:])
            return

        # Standard command parsing
        parts = line.split(" ", 1)
        cmd = parts[0]
        args = parts[1] if len(parts) > 1 else ""

        if cmd in self.command_map:
            self.command_map[cmd](args)
        else:
            print(f"Error: '{cmd}' is a figment of your imagination.")
