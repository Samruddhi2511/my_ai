from agent import agent

print("AI DB Agent running successfully.\n")

while True:
    q = input("Ask: ")

    if q.lower() == "exit":
        break

    agent.print_response(q)
