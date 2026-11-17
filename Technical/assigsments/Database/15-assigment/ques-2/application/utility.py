def check_user(conn,id):
    cur = conn.cursor()
    cur.execute('select emp_id from employee_pdbc ')
    emp_ids=cur.fetchall()
    cur.close()
    ids = [e[0] for e  in emp_ids]
    return id in ids
    
