import streamlit as st
import socket
 
# Server details
SERVER_IP = "10.170.104.80"  # Replace with the actual server IP
SERVER_PORT = 8080
 
# Streamlit UI
st.title("🔗 Socket Client with Streamlit")
 
# Text input fields
message1 = st.text_input("Enter first message:")
message2 = st.text_input("Enter second message:")
 
# Submit button
if st.button("Send Message"):
    if message1.strip() and message2.strip():
        final_message = message1 + " " + message2  # Concatenate messages
       
        try:
            # Establish socket connection
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((SERVER_IP, SERVER_PORT))
            st.success(f"✅ Connected to {SERVER_IP}:{SERVER_PORT}")
           
            # Send message to server
            client_socket.send(final_message.encode())
            st.write(f"📤 Sent: {final_message}")
           
            # Receive response from server
            response = client_socket.recv(1024).decode()
           
           
            client_socket.close()
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
    else:
        st.warning("Please enter messages in both fields before submitting.")
