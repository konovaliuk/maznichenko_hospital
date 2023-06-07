from flask import render_template, url_for, redirect, request, flash
from flask_login import current_user, login_user, logout_user, LoginManager, login_required
from model.models import *
from controller.app import app
from services import *
from services.illness_services import IllnessServices

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

user_services = UserServices()
illness_services = IllnessServices()
feedback_serv = FeedbackServices()


@login_manager.user_loader
def load_user(user_id):
    try:
        return user_services.get_user(user_id)
    except:
        return None


@app.route('/home')
def home():
    return render_template('home.html', user=current_user)


@app.route("/", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['submit_btn'] == 'login':
            user = User(login=request.form['login'], password=request.form['password'])
            user = user_services.sign_in(user)
            if user == False:
                error = 'Invalid credentials'
            else:
                login_user(user, remember=True, force=True)
                return redirect(url_for('home'))

        elif request.form['submit_btn'] == 'register':
            user = user_services.register(
                User(login=request.form['login'], password=request.form['password'], role=request.form['role']))
            if not user:
                error = 'Invalid credentials'
            else:
                login_user(user, remember=True, force=True)
                return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/create_request', methods=['GET', 'POST'])
@login_required
def create_request():
    error = 'Wrong user role'
    if current_user.role == 1:
        new_request = Illness(request.form['name'], request.form['model'], request.form['description'],
                              request.form['status'],
                              current_user.id, request.form['price'])
        if illness_services.add_request(new_request):
            error = None
        else:
            error = 'Invalid data'
    return render_template('create_request.html', error=error)


@app.route('/choose_requests', methods=['GET', 'POST'])
@login_required
def choose_requests():
    error = None
    if current_user.role == 2:  # admin
        data = illness_services.show_by_status('pending')
        if not data:
            error = 'No requests so far'
    elif current_user.role == 3:  # master
        data = illness_services.show_by_status('accepted')
        if not data:
            error = 'No accepted requests so far'
    else:
        data = illness_services.show_by_status('accepted')
    return render_template('requests.html', data=data, error=error)


@app.route('/process_choice', methods=['POST'])
def process_choice():
    selected_rows = request.form.getlist('row_ids[]')
    if current_user.role == 2:  # admin
        for id in selected_rows:
            illness_services.update_status(id, 'accepted')
    if current_user.role == 3:  # master
        for id in selected_rows:
            illness_services.update_status(id, 'in-work')
            feedback_serv.take_request(Feedback(request_id=id, master_id=current_user.id))
    # Process the selected rows as needed
    return 'Selected rows: ' + ', '.join(selected_rows)


@app.route('/my_illness')
def my_requests():
    data = []
    error = None
    if current_user.role == 1:
        data = illness_services.get_by_id(current_user.id)
        if not data:
            error = 'No illness by you so far'
    if current_user.role == 3:
        requests_id = feedback_serv.get_requests_id(current_user.id)
        for id in requests_id:
            data.append(illness_services.get_by_id(id[0]))
        if not data:
            error = 'No taken requests yet'
    return render_template('my_requests.html', data=data, error=error, role=current_user.role)


@app.route('/make_feedback', methods=['GET', 'POST'])
@login_required
def make_feedback():
    error = None
    data = None
    if current_user.role == 1:  # get completed requests by current user without feedback
        data = user_services.get_no_feedback(current_user.id)
        if data is None:
            error = 'No completed requests'
    return render_template('make_feedback.html', data=data, error=error)


@app.route('/process_table', methods=['POST'])
def process_table():
    feedbacks = request.form.getlist('feedbacks[]')
    row_ids = request.form.getlist('row_ids[]')

    for feedback, row_id in zip(feedbacks, row_ids):
        feedback_serv.add_feedback(row_id, feedback)

    return 'Form submitted successfully!'
