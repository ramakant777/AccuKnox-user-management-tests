# AccuKnox-user-management-tests
QA Testing Manual and Automations

# OrangeHRM Automation Test Suite with Playwright (Python)

This repository contains an automated end-to-end test suite for the [OrangeHRM Open Source Demo](https://opensource-demo.orangehrmlive.com/) web application using **Playwright in Python**.

The script performs a complete flow including:

- User login
- Employee creation
- User creation
- Editing user details (role, status, username, password)
- Validating updated details
- Deleting the employee

All actions are performed on the live demo site without any local dependencies other than Python and Playwright.

---

## Technologies Used

| Tool/Technology              | Version                                                                  |
| ---------------------------- | ------------------------------------------------------------------------ |
| Programming Language         | Python 3.8+                                                              |
| Browser Automation Framework | Playwright                                                               |
| Playwright Version           | v1.45.0                                                                  |
| Web Application              | [OrangeHRM Open Source Demo](https://opensource-demo.orangehrmlive.com/) |

---

## Features Covered

| Feature             | Description                                                                 |
| ------------------- | --------------------------------------------------------------------------- |
| **Login**           | Logs into the system using valid credentials                                |
| **Add Employee**    | Navigates to PIM module and adds a new employee with auto-generated ID      |
| **Create User**     | Goes to Admin > User Management and creates a new user with role and status |
| **Edit User**       | Modifies user role, status, username, and password                          |
| **Validation**      | Validates that the updated user details are correctly reflected             |
| **Delete Employee** | Deletes the created employee from the PIM module                            |

## 🔧 Setup Instructions

### Step 1: Clone the Repository

```bash
Step 1:
git clone https://github.com/your-username/orangehrm-playwright-test.git
cd orangehrm-playwright-test

Step 2: Create and Activate Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate    # On Windows use: venv\Scripts\activate

Step 3: Install Dependencies

pip install playwright
playwright install

How to Run the Tests
To execute the automation script:

python login.py

```
