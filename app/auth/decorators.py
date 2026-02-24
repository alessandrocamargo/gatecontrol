from functools import wraps
from flask_login import current_user
from flask import redirect, url_for, flash, request

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash("Faça login para continuar.", "warning")
            return redirect(url_for("auth.login", next=request.path))

        if current_user.role != "admin":
            flash("Acesso restrito a administradores.", "danger")
            return redirect(url_for("main.home"))

        return f(*args, **kwargs)
    return decorated_function
