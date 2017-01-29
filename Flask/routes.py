from flask import *
from functools import wraps
import sqlite3

DATABASE = 'Task.db'

app = Flask(__name__)
app.config.from_object(__name__)

app.secret_key = '223wqd8wqhdiwnda8dhqwe2q98ehqwndq'

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('login'))
	return wrap

@app.route('/welcome')
@login_required
def welcome():
	return render_template('home.html')

@app.route('/Logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect (url_for('login'))

@app.route('/tasks')
@login_required
def tasks():
    g.db  = connect_db()
    cur = g.db.execute('select name, due_date, priority, task_id from tasktable where status=1')
    open_tasks = [dict(name=row[0], due_date=row[1], priority=row[2], task_id=row[3]) for row in cur.fetchall()]
    cur = g.db.execute('select name, due_date, priority, task_id from tasktable where status=0')
    closed_tasks = [dict(name=row[0], due_date=row[1], priority=row[2], task_id=row[3]) for row in cur.fetchall()]
    g.db.close()
    return render_template('tasks.html', open_tasks=open_tasks, closed_tasks=closed_tasks)

@app.route('/add', methods=['POST'])
@login_required
def new_task():
    name = request.form['name']
    date = request.form['due_date']
    priority = request.form['priority']
    
    if not date:
       flash("You forgot the task date! Try again.")
       return redirect(url_for('tasks'))
       
    date_check=0
    first_slash=date.find('/')
    second_slash=date.find('/', first_slash+1)
    if int(date[second_slash+1:])<2013 or len(date[second_slash+1:])!=4:
    	date_check+=1
    	
    if int(date[first_slash+1:second_slash])>12 or int(date[first_slash+1:second_slash])<1:
    	date_check+=2
    
    if int(date[:first_slash])>31 or int(date[:first_slash])<1:
    	date_check+=4
    	
    if date_check==1:
    	flash("Please set year according to stardard convention(>2012 and 4 digits).")
    	return redirect(url_for('tasks'))
    elif date_check==2:
    	flash("Enter Month between 1-12.")
    	return redirect(url_for('tasks'))
    elif date_check==4:
        flash("Enter date between 1-31.")
        return redirect(url_for('tasks'))
    elif date_check==3:
    	flash('The Year and Month is not set properly.')
    	return redirect(url_for('tasks'))
    elif date_check==5:
    	flash('The Year and Date is not set properly.')
    	return redirect(url_for('tasks'))
    elif date_check==7:
    	flash('The date, Month and Year is not set properly.')
    	return redirect(url_for('tasks'))
    if not name and not date and not priority:
        flash("You forgot the task name, date, and priority! Try again.")
        return redirect(url_for('tasks'))
        
    elif not name and not date:
        flash("You forgot the task name and date! Try again.")
        return redirect(url_for('tasks'))
    elif not date and not priority:
        flash("You forgot the task date and priority! Try again.")
        return redirect(url_for('tasks'))
    elif not name and not priority:
        flash("You forgot the task name and priority! Try again.")
        return redirect(url_for('tasks'))
    elif not name:
        flash("You forgot the task name! Try again.")
        return redirect(url_for('tasks'))
    elif not priority:
        flash("You forgot the task priority! Try again.")
        return redirect(url_for('tasks'))
    else:
        g.db.execute('insert into tasktable (name, due_date, priority, status) values (?, ?, ?, 1)',
             [request.form['name'], request.form['due_date'], request.form['priority']])
        g.db.commit()
        flash('New entry was successfully posted')
        return redirect(url_for('tasks'))

@app.route('/delete/<int:task_id>',)
@login_required
def delete_entry(task_id):
    g.db  = connect_db()
    cur = g.db.execute('delete from tasktable where task_id='+str(task_id))
    g.db.commit()
    g.db.close()
    flash('The task was deleted')
    return redirect(url_for('tasks'))

@app.route('/complete/<int:task_id>',)
@login_required
def complete(task_id):
    g.db  = connect_db()
    cur = g.db.execute('update tasktable set status = 0 where task_id='+str(task_id))
    g.db.commit()
    g.db.close()
    flash('The task was marked as complete.')
    return redirect(url_for('tasks'))

@app.route('/incomplete/<int:task_id>',)
@login_required
def incomplete(task_id):
    g.db  = connect_db()
    cur = g.db.execute('update tasktable set status = 1 where task_id='+str(task_id))
    g.db.commit()
    g.db.close()
    flash('The task was marked as incomplete.')
    return redirect(url_for('tasks'))


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
			session['logged_in'] = True
			return redirect(url_for('welcome'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
	app.run(debug=True)
