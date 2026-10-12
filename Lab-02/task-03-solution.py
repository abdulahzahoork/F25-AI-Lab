class ClassroomAgent:
    def __init__(self):
        self.previous_mode = None

    def act(self, temp, occupied):
        # Preserve the teacher's original rule order and thresholds.
        if not occupied:
            target_mode = "ECO"
        elif temp > 26:
            target_mode = "COOL"
        elif temp < 20:
            target_mode = "WARM"
        else:
            target_mode = "IDLE"

        # Send a command only when the target mode changes.
        send_command = target_mode != self.previous_mode

        # Remember the current target for the next percept.
        self.previous_mode = target_mode

                # Return both values.
        return target_mode, send_command


agent = ClassroomAgent()

percepts = [
    (29, True),   # initial COOL
    (29, True),   # repeated COOL
    (20, True),   # exact lower boundary -> IDLE
    (26, True),   # exact upper boundary -> IDLE again
    (19, True),   # transition to WARM
    (29, False),  # empty room overrides temperature -> ECO
]

print("Step | Previous | Percept       | Target | Command?")
for step, percept in enumerate(percepts, 1):
    previous = agent.previous_mode
    target, send = agent.act(*percept)
    outcome = "SEND" if send else "NO COMMAND"
    print(f"{step:>4} | {str(previous):<8} | {str(percept):<13} | {target:<6} | {outcome}")
