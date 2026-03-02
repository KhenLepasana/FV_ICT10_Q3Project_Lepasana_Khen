from pyscript import document, window

def register_user(e):
    username = document.getElementById("username").value.strip()
    password = document.getElementById("password").value

    username_length = len(username)
    password_length = len(password)

    result = document.getElementById("message")

    # require both fields
    if username == "" or password == "":
        result.innerHTML = "❌ All fields are required."
        result.style.color = "red"
        return

    # username length
    if username_length < 7:
        result.innerHTML = "❌ Username must be at least 7 characters."
        result.style.color = "red"
        return

    # password length
    if password_length < 10:
        result.innerHTML = "❌ Password must be at least 10 characters."
        result.style.color = "red"
        return

    # check for at least one number and at least one letter
    has_number = any(c.isdigit() for c in password)
    has_letter = any(c.isalpha() for c in password)

    if not has_number and not has_letter:
        result.innerHTML = "❌ Password must have at least one number and one letter"
        result.style.color = "red"
        return

    if not has_number:
        result.innerHTML = "❌ Password must have at least one number"
        result.style.color = "red"
        return

    if not has_letter:
        result.innerHTML = "❌ Password must have at least one letter"
        result.style.color = "red"
        return

    else:   
        result.innerHTML = f"✅ Account created successfully, {username}!"
        result.style.color = "green"

        # redirect after success
        window.location.href = "teamchecker.html"