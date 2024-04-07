import streamlit as st
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_email(subject, body, receiver):
    
    sender_email = 'Vireo LLC'
    sender_pass = 'Etunat@1738'
    
    message = MIMEMultipart()
    message['from'] = "VIREO LLC"
    message['to'] = receiver
    message['subject'] = subject
    message.attach(MIMEText(body))
    
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender_email, sender_pass)
        smtp.send_message(message)


def community_page():
    st.title("Community")

    if 'events' not in st.session_state:
        st.session_state['events'] = [
            {"name": "Beach Cleanup", "activity": "Cleaning", "date": "2024-04-22", "location": "Santa Monica Beach"},
            {"name": "Tree Planting", "activity": "Planting", "date": "2024-05-05", "location": "Central Park"},
        ]

    tab1, tab2 = st.tabs(["Host an Effort", "Join an Effort"])

    with tab1:
        st.header("Host an Effort:")
        event_name = st.text_input("Event Name", key="new_event_name")
        activity_type = st.selectbox("Activity Type", ["Cleaning", "Planting", "Recycling"], key="new_activity_type")
        event_date = st.date_input("Date", key="new_event_date")
        event_location = st.text_input("Location", key="new_event_location")
        
        if st.button("Host an Effort"):
            new_event = {
                "name": event_name,
                "activity": activity_type,
                "date": event_date.strftime("%Y-%m-%d"),
                "location": event_location,
            }
            st.session_state['events'].append(new_event)
            email_subject = f"New Event Created: {event_name}"
            email_message = (
                f"You have created an event '{event_name}' on {event_date.strftime('%Y-%m-%d')}. "
                f"Activity: {activity_type}, Location: {event_location}. "
                "Thank you for contributing to a better environment!"
            )
            # send_email(email_subject, email_message, 'robiemelaku@gmail.com')
            st.success(f"Event '{event_name}' created successfully!")
            
            

    with tab2:
        st.header("Join an Effort")
        if st.session_state['events']:
            for event in st.session_state['events']:
                st.markdown(f"**{event['name']}**")
                st.markdown(f"- Activity: {event['activity']}")
                st.markdown(f"- Date: {event['date']}")
                st.markdown(f"- Location: {event['location']}")
                if st.button(f"Join {event['name']}", key=event['name']):
                    email_subject = f"Joined Event: {event['name']}"
                    email_message = (
                        f"You have joined the event '{event['name']}' on {event['date']}. "
                        f"Activity: {event['activity']}, Location: {event['location']}. "
                        "Details will be sent to your email. Thank you for participating!"
                    )
                    # send_email(email_subject, email_message, 'robiemelaku@gmail.com')
                    st.success(f"Thanks for joining {event['name']}! Further details will be sent to your email.")
                    
                    
        else:
            st.write("No events available at the moment. Consider creating one!")