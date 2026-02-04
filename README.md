# SliceItUp
Client-server pizza ordering application with GUI and real-time order tracking.

## Project Description
SliceItUp is a client-server pizza ordering application with a GUI that allows users to create orders, select pizza size, type, toppings, payment method, and delivery address.  
The server handles orders, generates delivery time, and tracks the status of pending and delivered orders in real-time.

---

## Features

### Client
- GUI for inputting order details
- Fields: First Name, Last Name, Address, Phone Number, Notes
- Pizza selection: Vegetariana, Capricciosa, Quatro Stagione, Fungi, Pršuto
- Toppings: Ketchup, Mayonnaise, Oregano (multiple selections allowed)
- Pizza size: 25 cm, 32 cm, 50 cm
- Payment method: Cash or Card
- Sends order to server and receives estimated delivery time

### Server
- Receives orders from client
- Generates delivery time (10–50 minutes)
- Tracks pending and delivered orders
- Displays remaining time for each pending order

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/aleksandrajjovanovic/SliceItUp.git

3. Install dependencies:
```bash
pip install -r requirements.txt

3.Run the server and client:
```bash
# Run server
python server.py
# Run client
python client.py
```bash
