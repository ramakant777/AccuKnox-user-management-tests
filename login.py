from playwright.sync_api import sync_playwright
import time
import random


def generate_employee_id(prefix="EMP", length=6):
    numbers = "".join([str(random.randint(0, 9)) for _ in range(length)])
    return f"{prefix}{numbers}"


url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
user = "Admin"
passw = "admin123"

first_name = "Ramakant"
last_name = "Jangir"

employee_id = generate_employee_id()
employee_name = "Ramakant Jangir"
username = "Rama123"
password = "Rama@123"
role = "ESS"
status = "Enabled"
new_role = "Admin"
new_status = "Disabled"
new_username = "Rama_123"
new_password = "Rama123@"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(url)
    page.fill("input[name='username']", user)
    page.fill("input[name='password']", passw)
    page.click("button[type='submit']")
    page.wait_for_selector("h6:has-text('Dashboard')", timeout=10000)

    page.click("a[href='/web/index.php/pim/viewPimModule']")
    page.wait_for_url(
        "https://opensource-demo.orangehrmlive.com/web/index.php/pim/*", timeout=10000
    )
    page.wait_for_selector("button:has-text('Add')", timeout=10000)

    page.wait_for_selector("button:has-text('Add')", timeout=10000, state="visible")
    count = page.locator("button:has-text('Add')").count()
    print(f"Found {count} 'Add' buttons")
    page.locator("button:has-text('Add')").first.click()

    page.fill("input[name='firstName']", first_name)
    page.fill("input[name='lastName']", last_name)
    page.fill("label:has-text('Employee Id') >> xpath=../..//input", employee_id)
    page.click("button[type='submit']")

    page.wait_for_selector(".oxd-toast-content--success", timeout=10000)

    page.click("a[href='/web/index.php/admin/viewAdminModule']")
    page.wait_for_selector("h6:has-text('User Management')", timeout=10000)

    page.click("button:has-text('Add')")
    page.wait_for_selector("h6:has-text('Add User')", timeout=10000)

    page.click(".oxd-select-text-input >> nth=0")
    page.click("div[role='option']:has-text('ESS')")
    page.fill("input[placeholder='Type for hints...']", employee_name)
    page.wait_for_selector(
        f"div[role='option']:has-text('{first_name} {last_name}')", timeout=10000
    )
    page.click(f"div[role='option']:has-text('{first_name} {last_name}')")
    page.click(".oxd-select-text-input >> nth=1")
    page.click("div[role='option']:has-text('Enabled')")
    page.fill("label:has-text('Username') >> xpath=../..//input", username)
    page.fill("label:has-text('Password') >> xpath=../..//input", password)
    page.fill("label:has-text('Confirm Password') >> xpath=../..//input", password)
    page.click("button[type='submit']")
    time.sleep(9)

    page.fill("label:has-text('Username') >> xpath=../..//input", username)
    page.fill("input[placeholder='Type for hints...']", employee_name)
    page.wait_for_selector(
        "div[role='option']:has-text('Ramakant Jangir')", timeout=10000
    )
    page.click("div[role='option']:has-text('Ramakant Jangir')")
    page.click(".oxd-select-wrapper >> nth=0")
    page.click(f"div[role='option']:has-text('{role}')")
    page.click(".oxd-select-wrapper >> nth=1")
    page.click(f"div[role='option']:has-text('{status}')")
    page.click("button:has-text('Search')")

    page.wait_for_selector("div.oxd-table", timeout=10000)
    page.wait_for_selector("div.oxd-table-row", timeout=10000)
    row_count = page.locator("div.oxd-table-body > div").count()
    print(f"Found {row_count} matching user(s)")

    page.click("i.bi-pencil-fill")
    page.wait_for_selector("h6:has-text('Edit User')", timeout=10000)

    page.click(".oxd-select-wrapper >> nth=0")
    page.click(f"div[role='option']:has-text('{new_role}')")
    page.click(".oxd-select-wrapper >> nth=1")
    page.click(f"div[role='option']:has-text('{new_status}')")
    page.fill("label:has-text('Username') >> xpath=../..//input", new_username)

    page.click(
        "div:has(label:has-text('Change Password ?')) input[type='checkbox']",
        force=True,
    )

    page.wait_for_selector(
        "label:has-text('Password') >> xpath=../..//input[@type='password']",
        timeout=10000,
    )
    page.fill(
        "label:has-text('Password') >> xpath=../..//input[@type='password']",
        new_password,
    )

    page.wait_for_selector(
        "label:has-text('Confirm Password') >> xpath=../..//input[@type='password']",
        timeout=10000,
    )
    page.fill(
        "label:has-text('Confirm Password') >> xpath=../..//input[@type='password']",
        new_password,
    )

    page.click("button[type='submit']")
    page.wait_for_selector(".oxd-toast-content--success", timeout=10000)

    page.click("a[href='/web/index.php/admin/viewAdminModule']")
    page.wait_for_selector("h6:has-text('User Management')", timeout=10000)
    page.fill("label:has-text('Username') >> xpath=../..//input", new_username)
    page.click("button:has-text('Search')")

    page.wait_for_selector("div.oxd-table-body > div", timeout=10000)
    row_count = page.locator("div.oxd-table-body > div").count()
    print(f"Found {row_count} matching user(s)")
    page.click("i.bi-pencil-fill")
    page.wait_for_selector("h6:has-text('Edit User')", timeout=10000)
    page.wait_for_timeout(1000)

    current_role = page.locator(".oxd-select-text-input >> nth=0").text_content()
    current_status = page.locator(".oxd-select-text-input >> nth=1").text_content()
    current_username = page.locator(
        "label:has-text('Username') >> xpath=../..//input"
    ).input_value()

    assert current_role.strip() == new_role
    assert current_status.strip() == new_status
    assert current_username.strip() == new_username
    print("All user details validated successfully!")

    page.click("a[href='/web/index.php/pim/viewPimModule']")
    page.wait_for_url(
        "https://opensource-demo.orangehrmlive.com/web/index.php/pim/*", timeout=10000
    )

    page.fill("input[placeholder='Type for hints...']", employee_name)
    page.wait_for_selector(
        f"div[role='option']:has-text('{first_name} {last_name}')", timeout=10000
    )
    page.click(f"div[role='option']:has-text('{first_name} {last_name}')")
    page.click("button:has-text('Search')")

    page.wait_for_selector("div.oxd-table-row", timeout=10000)
    page.click("i.bi-trash")
    page.wait_for_selector("button:has-text('Yes, Delete')", timeout=10000)
    page.click("button:has-text('Yes, Delete')")

    page.wait_for_selector(".oxd-toast-content--success", timeout=10000)
    time.sleep(6)
    browser.close()
