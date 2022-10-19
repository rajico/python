table = {
    (): 'print("wait")’,
    ('food',): 'print("eat")’,
    ('water',): 'print("drink")',
        }
past_percepts = []
while True:
current_percept = random.choice([
’’, 'food', 'water’])
eval(table_driven_agent_program(
table, current_percept, past_percepts))
print(past_percepts)
time.sleep(1)