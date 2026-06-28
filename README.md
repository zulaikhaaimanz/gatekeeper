# GateKeeper

GateKeeper is a login monitoring system developed using Python and Flask. It analyzes login attempts and identifies potentially suspicious authentication activities based on basic security checks. The application automatically captures session details and presents a security report through a clean and responsive dashboard.

---

## Features

* Monitor login attempts
* Detect suspicious authentication activity
* Automatic IP address detection
* Browser detection
* Login timestamp generation
* Safe and Suspicious login classification
* Risk level indication
* Security recommendations
* Responsive and modern dashboard interface

---

## Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript
* Visual Studio Code

---

## How It Works

The user enters a username and password to simulate a login attempt. The application automatically retrieves session information such as the IP address, browser, and current timestamp.

The login attempt is then evaluated based on simple security checks, including:

* Password length
* Presence of uppercase letters
* Presence of numeric characters
* Network type

Based on these checks, the system classifies the login attempt as either **Safe Login** or **Suspicious Login** and displays the associated risk level along with the reasons for the decision.

---

## Project Structure

```
gatekeeper
│
├── app.py
├── README.md
├── requirements.txt
│
├── templates
│   └── index.html
│
└── static
    ├── style.css
    └── script.js
```

---

## Installation

1. Install the required package:

```
pip install -r requirements.txt
```

2. Run the application:

```
python app.py
```

3. Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Future Improvements

* Multi-factor authentication simulation
* Login history database
* Email alerts for suspicious logins
* Device recognition
* Location-based authentication
* User account management

---

## Author

**Zulaikha Aiman**

B.Tech Computer Science and Engineering

CMR University