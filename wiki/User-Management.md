# User Management

IT Tasker supports multiple user accounts with simple username/password authentication.

## Default Account

On first run, a default admin account is created:

| Username | Password |
|---|---|
| `admin` | `admin123` |

> **⚠️ Change this password immediately** after first login.

## Managing Users

Navigate to **Users** in the sidebar to view, add, or remove user accounts.

### Adding a User

1. Go to the **Users** page
2. Enter a **Username** and **Password** in the "Add User" form
3. Click **Create User**

Usernames must be unique. There is no email or role system — all users have the same access level.

### Deleting a User

1. Go to the **Users** page
2. Click the **Delete** button next to the user
3. Confirm the deletion

> You cannot delete your own account while logged in.

## Changing Your Password

1. Navigate to **Change Password** in the sidebar
2. Enter your **Current Password**
3. Enter and confirm your **New Password** (minimum 6 characters)
4. Click **Change Password**

## Authentication Details

- Passwords are hashed using Werkzeug's `generate_password_hash` (PBKDF2 by default)
- Sessions are managed by Flask-Login with a configurable `SECRET_KEY`
- The "Remember Me" option on the login page extends the session
- All pages except the login page require authentication
