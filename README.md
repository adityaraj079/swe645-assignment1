# SWE645 – Homework Assignment 1

**Author:** Aditya Raj  
**Course:** SWE645 – Software Engineering for the World Wide Web  

---

## Project Overview

This project is developed as part of **SWE645 Homework Assignment 1**.  
It demonstrates a simple web application consisting of a homepage and a student survey page built using **HTML5** and **Bootstrap**.

The project is deployed using two AWS-based approaches:

1. **Static website hosting on Amazon S3**
2. **Dynamic hosting using a Flask application on an AWS EC2 instance**

---


### EC2 Details
- Instance Type: `t3.micro`
- Operating System: Ubuntu
- Web Framework: Flask
- Port Used: `5000`

## Steps to Deploy Flask Application on EC2

### Step 1: Launch EC2 Instance
- Choose **Ubuntu (20.04 or later)**
- Select instance type: `t3.micro`
- Configure Security Group:
  - Allow SSH (Port 22)
  - Allow Custom TCP (Port 5000)

---

### Step 2: Connect to EC2

### Step 3: Update System and Install Dependencies
```sudo apt update```
```sudo apt upgrade -y```
```sudo apt install python3 python3-pip python3-venv -y```

### Step 4: Clone the Repository
``` git clone https://github.com/<YOUR_GITHUB_USERNAME>/<REPOSITORY_NAME>.git```
```cd <REPOSITORY_NAME>```

### Step 5: Create Virtual Environment (Optional but Recommended)
```python3 -m venv venv```
```source venv/bin/activate```

### Step 6: Install Flask
``` pip install flask ```

### Step 7: Run the Flask Server
``` python3 app.py ```

#### Access the application
``` http://<EC2-PUBLIC-IP>:5000```

