from functools import wraps
from flask_login import current_user
from flask import redirect, url_for, flash

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for("auth.login"))
        
        if current_user.role != "admin":
            flash("Acesso restrito a administradores.", "error")
            return redirect(url_for("main.home"))
        
        return f(*args, **kwargs)
    return decorated_function