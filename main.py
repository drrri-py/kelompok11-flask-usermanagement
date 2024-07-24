from flask import Flask, flash, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SECRET_KEY"] = '2a831d6c294e7d8703f0be6a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://fid2:12345@localhost:3306/pbo2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = 'filesystem'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
Session(app)

# User Class
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(255), nullable=False)
    lname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    edu = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Integer, default=0, nullable=False)

    def __repr__(self):
        return f'User("{self.id}","{self.fname}","{self.lname}","{self.email}","{self.edu}","{self.username}","{self.status}")'

# Admin Class
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'Admin("{self.username}","{self.id}")'
    
#ganti username dan password untuk sigup admin baru    
#def create_admin_user():
#    with app.app_context():
#        admin = Admin(username='fid', password=bcrypt.generate_password_hash('1234').decode('utf-8'))
#        db.session.add(admin)
#        db.session.commit()
    
#create_admin_user()

# Main index route
@app.route('/')
def index():
    return render_template('index.html', title="")

# Admin login route
@app.route('/admin/', methods=["POST", "GET"])
def adminIndex():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == "" or password == "":
            flash('Please fill all fields', 'danger')
            return redirect('/admin/')
        else:
            admin = Admin.query.filter_by(username=username).first()
            if admin and bcrypt.check_password_hash(admin.password, password):
                session['admin_id'] = admin.id
                session['admin_name'] = admin.username
                flash('Login Successfully', 'success')
                return redirect('/admin/dashboard')
            else:
                flash('Invalid Username or Password', 'danger')
                return redirect('/admin/')
    else:
        return render_template('admin/index.html', title="Admin Login")

# Admin dashboard route
@app.route('/admin/dashboard')
def adminDashboard():
    if not session.get('admin_id'):
        return redirect('/admin/')
    
    totalUser = User.query.count()
    totalApprove = User.query.filter_by(status=1).count()
    NotTotalApprove = User.query.filter_by(status=0).count()
    
    return render_template('admin/dashboard.html', title="Admin Dashboard", totalUser=totalUser, totalApprove=totalApprove, NotTotalApprove=NotTotalApprove)

# Admin get all users route
@app.route('/admin/get-all-user', methods=["POST", "GET"])
def adminGetAllUser():
    if not session.get('admin_id'):
        return redirect('/admin/')
    
    if request.method == "POST":
        search = request.form.get('search')
        users = User.query.filter(User.username.like('%' + search + '%')).all()
    else:
        users = User.query.all()
    
    return render_template('admin/all-user.html', title='Approve User', users=users)

# Admin approve user route
@app.route('/admin/approve-user/<int:id>')
def adminApprove(id):
    if not session.get('admin_id'):
        return redirect('/admin/')
    
    User.query.filter_by(id=id).update(dict(status=1))
    db.session.commit()
    flash('User Approved Successfully', 'success')
    return redirect('/admin/get-all-user')

# Change admin password route
@app.route('/admin/change-admin-password', methods=["POST", "GET"])
def adminChangePassword():
    admin = Admin.query.get(1)
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == "" or password == "":
            flash('Please fill all fields', 'danger')
            return redirect('/admin/change-admin-password')
        else:
            # Generate hashed password with bcrypt
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            
            # Update admin password in the database
            admin.password = hashed_password
            db.session.commit()
            flash('Admin Password updated successfully', 'success')
            return redirect('/admin/change-admin-password')
    
    return render_template('admin/admin-change-password.html', title='Admin Change Password', admin=admin)

# Admin logout route
@app.route('/admin/logout')
def adminLogout():
    if not session.get('admin_id'):
        return redirect('/admin/')
    
    session['admin_id'] = None
    session['admin_name'] = None
    return redirect('/')

# User login route
@app.route('/user/', methods=["POST", "GET"])
def userIndex():
    if session.get('user_id'):
        return redirect('/user/dashboard')
    
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            if user.status == 0:
                flash('Your account is not approved by Admin', 'danger')
                return redirect('/user/')
            else:
                session['user_id'] = user.id
                session['username'] = user.username
                flash('Login Successfully', 'success')
                return redirect('/user/dashboard')
        else:
            flash('Invalid Email or Password', 'danger')
            return redirect('/user/')
    
    return render_template('user/index.html', title="User Login")

# User registration route
@app.route('/user/signup', methods=['POST', 'GET'])
def userSignup():
    if session.get('user_id'):
        return redirect('/user/dashboard')
    
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        username = request.form.get('username')
        edu = request.form.get('edu')
        password = request.form.get('password')
        
        if fname == "" or lname == "" or email == "" or password == "" or username == "" or edu == "":
            flash('Please fill all fields', 'danger')
            return redirect('/user/signup')
        
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists', 'danger')
            return redirect('/user/signup')
        
        hashed_password = bcrypt.generate_password_hash(password, 10)
        new_user = User(fname=fname, lname=lname, email=email, username=username, edu=edu, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully. Admin will approve your account soon.', 'success')
        return redirect('/user/')
    
    return render_template('user/signup.html', title="User Signup")

# User dashboard route
@app.route('/user/dashboard')
def userDashboard():
    if not session.get('user_id'):
        return redirect('/user/')
    
    user = User.query.get(session['user_id'])
    return render_template('user/dashboard.html', title="User Dashboard", user=user)

# User logout route
@app.route('/user/logout')
def userLogout():
    if not session.get('user_id'):
        return redirect('/user/')
    
    session['user_id'] = None
    session['username'] = None
    return redirect('/user/')

# User change password route
@app.route('/user/change-password', methods=["POST", "GET"])
def userChangePassword():
    if not session.get('user_id'):
        return redirect('/user/')
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if email == "" or password == "":
            flash('Please fill all fields', 'danger')
            return redirect('/user/change-password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            hashed_password = bcrypt.generate_password_hash(password, 10)
            user.password = hashed_password
            db.session.commit()
            flash('Password changed successfully', 'success')
            return redirect('/user/change-password')
        else:
            flash('Invalid Email', 'danger')
            return redirect('/user/change-password')
    
    return render_template('user/change-password.html', title="Change Password")

# User update profile route
@app.route('/user/update-profile', methods=["POST", "GET"])
def userUpdateProfile():
    if not session.get('user_id'):
        return redirect('/user/')
    
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        username = request.form.get('username')
        edu = request.form.get('edu')
        
        if fname == "" or lname == "" or email == "" or username == "" or edu == "":
            flash('Please fill all fields', 'danger')
            return redirect('/user/update-profile')
        
        user.fname = fname
        user.lname = lname
        user.email = email
        user.username = username
        user.edu = edu
        db.session.commit()
        session['username'] = username
        flash('Profile updated successfully', 'success')
        return redirect('/user/dashboard')
    
    return render_template('user/update-profile.html', title="Update Profile", user=user)

if __name__ == "__main__":
    app.run(debug=True)
