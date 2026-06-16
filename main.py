# main.py
from engine import ArawInterpreter

# README note: 
# Always remember to add a markdown code block to the readme.

def main():
    interpreter = ArawInterpreter()
    
    # Araw 1.5 Script: The "Everything" Test
    script = """
    -- Define local variables
    lvar playerName = "krovixa"
    lvar version = "1.5"
    
    -- Register a function
    lfunc initialize()
    
    -- Print stuff
    emit("--- Araw Engine Startup ---")
    emit(playerName)
    emit("Version:")
    emit(version)
    emit("Initialization complete.")
    """
    
    for line in script.splitlines():
        interpreter.run_line(line)

if __name__ == "__main__":
    main()
