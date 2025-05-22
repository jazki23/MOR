
import streamlit as st

# List of tutorial steps
steps = [
    {
        "title": "Step 1: Open the GCash App",
        "content": "Ensure the GCash app is installed on your smartphone. Log in using your registered mobile number and 4-digit MPIN."
    },
    {
        "title": "Step 2: Access the 'Send Money' Feature",
        "content": "On the app’s home screen, tap on the ‘Send’ or ‘Send Money’ button."
    },
    {
        "title": "Step 3: Choose the Transfer Method",
        "content": "GCash offers several options for sending money:\n- **Express Send**\n- **Send via QR**\n- **Send to Bank**"
    },
    {
        "title": "Step 4: Enter Recipient Details",
        "content": "For Express Send: Input the recipient’s GCash mobile number.\nFor Send via QR: Scan a QR code.\nFor Send to Bank: Provide bank details."
    },
    {
        "title": "Step 5: Review Transaction Details",
        "content": "Verify recipient details, amount, and service fees before confirming."
    },
    {
        "title": "Step 6: Enter Your MPIN",
        "content": "You will be prompted to enter your 4-digit MPIN to authenticate the transaction."
    },
    {
        "title": "Step 7: Transaction Confirmation",
        "content": "Once successful, a confirmation screen will appear, and you’ll receive a text message."
    },
    {
        "title": "Step 8: Save/Share the Receipt",
        "content": "You can screenshot or download the receipt for your records."
    },
]

# Set up the Streamlit layout
def display_step(step_index):
    """Display the step title and content"""
    step = steps[step_index]
    st.header(step['title'])
    st.write(step['content'])

def app():
    # Streamlit title
    st.title("GCash Transaction Tutorial")

    # Store the current step number
    if 'current_step' not in st.session_state:
        st.session_state.current_step = 0  # Start from the first step

    # Display the current step
    display_step(st.session_state.current_step)

    # Buttons for navigating between steps
    col1, col2 = st.columns(2)

    with col1:
        if st.session_state.current_step > 0:
            if st.button("Previous"):
                st.session_state.current_step -= 1

    with col2:
        if st.session_state.current_step < len(steps) - 1:
            if st.button("Next"):
                st.session_state.current_step += 1
        else:
            if st.button("Finish"):
                st.session_state.current_step = 0  # Reset to first step or end the tutorial
                st.success("You have completed the tutorial!")

    # Add a footer or progress indicator
    st.write(f"Step {st.session_state.current_step + 1} of {len(steps)}")

if __name__ == "__main__":
    app()
