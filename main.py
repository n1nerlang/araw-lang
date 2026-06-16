# ARAW LANGUAGE - THE CHAOTIC BUILD
# If this code breaks, it's not a bug, it's a "feature implementation delay."
# Inspired by Lua, but fueled by way too much caffeine and existential crisis.

class ArawInterpreter:
    def __init__(self):
        # A dictionary to hold our variables. 
        # It's basically a junk drawer for data.
        self.variables = {}

    def parse_value(self, token):
        token = token.strip()
        # If it's wrapped in quotes, it's just raw text.
        if (token.startswith('"') and token.endswith('"')):
            return token[1:-1]
        # Otherwise, we look it up in our variable junk drawer.
        return self.variables.get(token, f"[UNDEFINED_ERROR: {token} doesn't exist]")

    def run(self, source):
        for line in source.splitlines():
            line = line.strip()
            
            # Skip comments (the silence before the crash)
            if not line or line.startswith("--"):
                continue
            
            # Assignment: let name = value
            if line.startswith("let "):
                parts = line.replace("let ", "").split(" = ", 1)
                if len(parts) == 2:
                    var_name = parts[0].strip()
                    self.variables[var_name] = self.parse_value(parts[1])
            
            # Emit: emit(something)
            # This handles both emit("text") and emit(variable)
            elif line.startswith("emit(") and line.endswith(")"):
                content = line[5:-1]
                print(self.parse_value(content))
            
            else:
                print(f"Panic! I don't understand '{line}'. Are you speaking in tongues?")

# README note: 
# Always remember to add a markdown code block to the readme.

if __name__ == "__main__":
    araw_code = """
    -- Defining our local variables
    let version = "0.0.1"
    let status = "Experimental Chaos"
    
    -- Emitting data
    emit("--- Starting Araw Engine ---")
    emit(version)
    emit("Current status is:")
    emit(status)
    emit("I hope this doesn't explode!")
    """
    
    interpreter = ArawInterpreter()
    interpreter.run(araw_code)
