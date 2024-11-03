import queue
import time

# Initialize an empty queue to represent the ticket counter queue
ticket_queue = queue.Queue()

# Function to simulate customers arriving at the ticket counter
def customer_arrival(ticket_queue, num_customers):
    for customer_id in range(1, num_customers + 1):
        print(f"Customer {customer_id} has arrived and is waiting in line.")
        ticket_queue.put(customer_id)
        time.sleep(0.5)  # Adding a small delay to simulate real-time arrival

# Function to simulate serving customers at the ticket counter
def serve_customers(ticket_queue):
    while not ticket_queue.empty():
        customer_id = ticket_queue.get()  # Serve the customer at the front of the queue
        print(f"Serving Customer {customer_id}.")
        time.sleep(1)  # Adding a delay to simulate the time taken to serve each customer
    print("All customers have been served.")

# Main function to run the simulation
def ticket_counter_simulation(num_customers):
    print("Starting ticket counter simulation...\n")
    customer_arrival(ticket_queue, num_customers)
    print("\nAll customers have arrived. Starting service...\n")
    serve_customers(ticket_queue)
    print("\nTicket counter simulation completed.")

# Run the simulation with a specified number of customers
num_customers = 5
ticket_counter_simulation(num_customers)
