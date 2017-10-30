from app import app
from flask import request, render_template
from app import db
from app.models import It_companies
import json

# my routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/table_view')
def table_view():
    result = ''
    message = ''

    job = request.args.get('job')
    id_ = request.args.get('id_')
    mysql_data=[]

    if id_ is not None:
        try:
            check_id = int(id_) #id_ should be a str representation of a int
        except TypeError:
            message = 'company_id must be an integer'

    # Valid job found
    if job is not None:
        # Execute job
        if (job == 'get_companies'):
            # Get companies
            query = It_companies.query.order_by(It_companies.rank).all()
            if query is None:
                result  = 'error'
                message = 'query error'
            else:
                result  = 'success'
                message = 'query success'
                mysql_data = []
                for q in query:
                    functions  = '<div class="function_buttons"><ul>'
                    functions = functions + '<li class="function_edit"><a data-id="' + str(q.company_id) + '" data-name="' + q.company_name + '"><span>Edit</span></a></li>'
                    functions = functions + '<li class="function_delete"><a data-id="' + str(q.company_id) + '" data-name="' + q.company_name + '"><span>Delete</span></a></li>'
                    functions = functions + '</ul></div>'
                    mysql_data.append({
                        "rank" : q.rank,
                        "company_name" : q.company_name,
                        "industries" : q.industries,
                        "revenue" : q.revenue,
                        "fiscal_year" : q.fiscal_year,
                        "employees" : q.employees,
                        "market_cap" : q.market_cap,
                        "headquarters"  : q.headquarters,
                        "functions" : functions
                    })
        elif (job == 'get_company'):
            # Get company
            if (id_ == ''):
                result  = 'error'
                message = 'id missing'
            else:
                try:
                    q = It_companies.query.filter_by(company_id=id_).first()
                    mysql_data = []
                    mysql_data.append({
                        "rank" : q.rank,
                        "company_name" : q.company_name,
                        "industries" : q.industries,
                        "revenue" : q.revenue,
                        "fiscal_year" : q.fiscal_year,
                        "employees" : q.employees,
                        "market_cap" : q.market_cap,
                        "headquarters"  : q.headquarters
                    })
                    result  = 'success';
                    message = 'query success'
                except Exception as ex:
                    print('PAB> Exception in query : ', ex)
                    result  = 'error'
                    message = ex
        elif (job == 'add_company'):
            # Add company
            form_data = request.args
            try:
                new_company = It_companies(
                    rank=form_data['rank'],
                    company_name=form_data['company_name'],
                    industries=form_data['industries'],
                    revenue=form_data['revenue'],
                    fiscal_year=form_data['fiscal_year'],
                    employees=form_data['employees'],
                    market_cap=form_data['market_cap'],
                    headquarters=form_data['headquarters']
                    )
                db.session.add(new_company)
                db.session.commit()
                result = 'success'
                message = 'added new record'
            except Exception as ex:
                db.session.rollback()
                print('PAB> Exception in database operation : ', ex)
                result = 'error'
                message = ex
            finally:
                # print('PAB> Result = ', result)
                # print('PAB> Message = ', message)
                pass
        elif (job == 'edit_company'):
            # Edit company
            if (id_ == ''):
                result  = 'error'
                message = 'id missing'
            else:
                form_data = request.args
                try:
                    q = It_companies.query.filter_by(company_id=id_).first()
                    q.rank=form_data['rank']
                    q.company_name=form_data['company_name']
                    q.industries=form_data['industries']
                    q.revenue=form_data['revenue']
                    q.fiscal_year=form_data['fiscal_year']
                    q.employees=form_data['employees']
                    q.market_cap=form_data['market_cap']
                    q.headquarters=form_data['headquarters']
                    db.session.commit()
                    result  = 'success'
                    message = 'Company data changed'
                except Exception as ex:
                    db.session.rollback()
                    print('PAB> Exception in database operation : ', ex)
                    result  = 'error'
                    message = ex
                finally:
                    # print('PAB> edit_company result : ', result)
                    # print('PAB> edit_company message : ', message)
                    pass
        elif (job == 'delete_company'):
            # Delete company
            if (id == ''):
                result  = 'error'
                message = 'id missing'
            else:
                try:
                    q = It_companies.query.filter_by(company_id=id_).first()
                    db.session.delete(q)
                    result  = 'success'
                    message = 'delete successful'
                except Exception as ex:
                    db.session.rollback()
                    print('PAB> Exception in database operation : ', ex)
                    result  = 'error'
                    message = ex
                finally:
                    # print('PAB> delete_company result : ', result)
                    # print('PAB> delete_company message : ', message)
                    pass

    # Prepare data
    data = {
      "result"  : result,
      "message" : message,
      "data"    : mysql_data
    }
    # Convert dict to JSON array
    return json.dumps(data)
