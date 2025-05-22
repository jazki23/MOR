import streamlit as st
import os

# Tutorial steps with relative image paths
steps = [
    {
        "title": "Step 1: Open the GCash App",
        "content": "Ensure the GCash app is installed on your smartphone. Log in using your registered mobile number and 4-digit MPIN.",
        "image": "images/step1.png"
    },
    {
        "title": "Step 2: Access the 'Send Money' Feature",
        "content": "On the app’s home screen, tap on the ‘Send’ or ‘Send Money’ button.",
        "image": "images/step2.png"
    },
    {
        "title": "Step 3: Choose Express Send",
        "content": "GCash offers several options for sending money:\n- Express Send\n- Send via QR\n- Send to Bank",
        "image": "images/step3.png"
    },
    {
        "title": "Step 4: Enter the Recipient registered GCash Mobile Number",
        "content": "For Express Send: Input the recipient’s GCash mobile number.\nFor Send via QR: Scan a QR code.\nFor Send to Bank: Provide bank details.",
        "image": "images/step4.png"
    },
    {
        "title": "Step 5: Review Transaction Details",
        "content": "Verify recipient details, amount, and service fees before confirming.",
        "image": "images/step5.png"
    },
    {
        "title": "Step 6: Transaction Confirmation",
        "content": "You will be prompted to enter your 6-digit code to authenticate the transaction.",
        "image": "images/step6.png"
    },
    {
        "title": "Step 7: Receive Authentication Code",
        "content": "You'll receive a text message from GCash containing the authentication code.",
        "image": "images/step7.png"
    },
    {
        "title": "Step 8: Save/Share the Receipt",
        "content": "You can screenshot or download the receipt for your records.",
        "image": "images/step8.png"
    },
]

def display_step(step):
    st.subheader(step['title'])
    st.write(step['content'])

    image_path = step.get('image')
    if image_path:
        if os.path.exists(image_path):
            st.image(image_path, use_column_width=True)
        else:
            st.warning(f"Image not found: {image_path}")

def app():
    if 'current_step' not in st.session_state:
        st.session_state.current_step = 0

    st.title("GCash Tutorial")

    display_step(steps[st.session_state.current_step])

    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        if st.button("Previous") and st.session_state.current_step > 0:
            st.session_state.current_step -= 1

    with col3:
        if st.button("Next") and st.session_state.current_step < len(steps) - 1:
            st.session_state.current_step += 1

    st.write(f"Step {st.session_state.current_step + 1} of {len(steps)}")

if __name__ == "__main__":
    app()
