from app import app
from flask import request, render_template
from numbers import Number
import pandas as pd
from app import db
from app.models import It_companies
import json
from flask import jsonify

# my routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/table_view')
def table_view():
    job = None
    id_ = None
    result = ''
    message = ''
    mysql_data = []

    job = request.args.get('job')
    id_ = request.args.get('id')
    print('PAB> job = ', job, '  id_ = ', id_)

    if job is not None:
        if (job == 'get_companies' or
            job == 'get_company'   or
            job == 'add_company'   or
            job == 'edit_company'  or
            job == 'delete_company'):
            if id_ is not None:
                if not isinstance(id_, Number):
                    id_ = None
        else:
            job = None

    # Valid job found
    if job is not None:
        # Execute job
        if (job == 'get_companies'):
            # Get companies
            #print('PAB> I am in get_companies...')
            #code from https://www.sitepoint.com/creating-a-scrud-system-using-jquery-json-and-datatables/
            #PAB converted code from php to python and flask-sqlalchemy
            query = It_companies.query.order_by(It_companies.rank).all()
            if query is None:
                result  = 'error'
                message = 'query error'
            else:
                #print('PAB> query : ', query)
                result  = 'success'
                message = 'query success'
                for q in query:
                    #print('PAB> Company : ', q.company_name)
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

    # Prepare data
    data = {
      "result"  : result,
      "message" : message,
      "data"    : mysql_data
    }

    # Convert dict to JSON array
    json_data = json.dumps(data)
    #print('\nPAB> json_data : \n', json_data)
    return json_data


"""# Prepare array
mysql_data = array();"""

"""# Valid job found
if (job != '')
    # Connect to database
    #db_connection = mysqli_connect($db_server, $db_username, $db_password, $db_name);
    #if (mysqli_connect_errno())
    #    $result  = 'error';
    #    $message = 'Failed to connect to database: ' . mysqli_connect_error();
    #    job     = ''

    # Execute job
    if (job == 'get_companies'){

        # Get companies
        $query = "SELECT * FROM it_companies ORDER BY rank";
        $query = mysqli_query(db_connection, $query);
        if (!$query)
            $result  = 'error';
            $message = 'query error';
        else
            $result  = 'success';
            $message = 'query success';
            while ($company = mysqli_fetch_array($query))
                $functions  = '<div class="function_buttons"><ul>';
                $functions .= '<li class="function_edit"><a data-id="'   . $company['company_id'] . '" data-name="' . $company['company_name'] . '"><span>Edit</span></a></li>';
                $functions .= '<li class="function_delete"><a data-id="' . $company['company_id'] . '" data-name="' . $company['company_name'] . '"><span>Delete</span></a></li>';
                $functions .= '</ul></div>';
                mysql_data[] = array(
                  "rank"          => $company['rank'],
                  "company_name"  => $company['company_name'],
                  "industries"    => $company['industries'],
                  "revenue"       => '$ ' . $company['revenue'],
                  "fiscal_year"   => $company['fiscal_year'],
                  "employees"     => number_format($company['employees'], 0, '.', ','),
                  "market_cap"    => '$ ' . $company['market_cap'],
                  "headquarters"  => $company['headquarters'],
                  "functions"     => $functions
                )
    elif (job == 'get_company'){

        # Get company
        if (id == '')
            $result  = 'error';
            $message = 'id missing';
        else
            $query = "SELECT * FROM it_companies WHERE company_id = '" . mysqli_real_escape_string(db_connection, id) . "'";
            $query = mysqli_query(db_connection, $query);
            if (!$query)
                $result  = 'error';
                $message = 'query error';
            else
                $result  = 'success';
                $message = 'query success';
                while ($company = mysqli_fetch_array($query))
                    mysql_data[] = array(
                    "rank"          => $company['rank'],
                    "company_name"  => $company['company_name'],
                    "industries"    => $company['industries'],
                    "revenue"       => $company['revenue'],
                    "fiscal_year"   => $company['fiscal_year'],
                    "employees"     => $company['employees'],
                    "market_cap"    => $company['market_cap'],
                    "headquarters"  => $company['headquarters']
                    );

    elif (job == 'add_company')

        # Add company
        $query = "INSERT INTO it_companies SET ";
        if (isset($_GET['rank']))         { $query .= "rank         = '" . mysqli_real_escape_string(db_connection, $_GET['rank'])         . "', "; }
        if (isset($_GET['company_name'])) { $query .= "company_name = '" . mysqli_real_escape_string(db_connection, $_GET['company_name']) . "', "; }
        if (isset($_GET['industries']))   { $query .= "industries   = '" . mysqli_real_escape_string(db_connection, $_GET['industries'])   . "', "; }
        if (isset($_GET['revenue']))      { $query .= "revenue      = '" . mysqli_real_escape_string(db_connection, $_GET['revenue'])      . "', "; }
        if (isset($_GET['fiscal_year']))  { $query .= "fiscal_year  = '" . mysqli_real_escape_string(db_connection, $_GET['fiscal_year'])  . "', "; }
        if (isset($_GET['employees']))    { $query .= "employees    = '" . mysqli_real_escape_string(db_connection, $_GET['employees'])    . "', "; }
        if (isset($_GET['market_cap']))   { $query .= "market_cap   = '" . mysqli_real_escape_string(db_connection, $_GET['market_cap'])   . "', "; }
        if (isset($_GET['headquarters'])) { $query .= "headquarters = '" . mysqli_real_escape_string(db_connection, $_GET['headquarters']) . "'";   }
        $query = mysqli_query(db_connection, $query);
        if (!$query)
            $result  = 'error';
            $message = 'query error';
        else
            $result  = 'success';
            $message = 'query success';

    elif (job == 'edit_company')

        # Edit company
        if (id == ''){
            $result  = 'error';
            $message = 'id missing';
        else
            $query = "UPDATE it_companies SET ";
            if (isset($_GET['rank']))         { $query .= "rank         = '" . mysqli_real_escape_string(db_connection, $_GET['rank'])         . "', "; }
            if (isset($_GET['company_name'])) { $query .= "company_name = '" . mysqli_real_escape_string(db_connection, $_GET['company_name']) . "', "; }
            if (isset($_GET['industries']))   { $query .= "industries   = '" . mysqli_real_escape_string(db_connection, $_GET['industries'])   . "', "; }
            if (isset($_GET['revenue']))      { $query .= "revenue      = '" . mysqli_real_escape_string(db_connection, $_GET['revenue'])      . "', "; }
            if (isset($_GET['fiscal_year']))  { $query .= "fiscal_year  = '" . mysqli_real_escape_string(db_connection, $_GET['fiscal_year'])  . "', "; }
            if (isset($_GET['employees']))    { $query .= "employees    = '" . mysqli_real_escape_string(db_connection, $_GET['employees'])    . "', "; }
            if (isset($_GET['market_cap']))   { $query .= "market_cap   = '" . mysqli_real_escape_string(db_connection, $_GET['market_cap'])   . "', "; }
            if (isset($_GET['headquarters'])) { $query .= "headquarters = '" . mysqli_real_escape_string(db_connection, $_GET['headquarters']) . "'";   }
            $query .= "WHERE company_id = '" . mysqli_real_escape_string(db_connection, id) . "'";
            $query  = mysqli_query(db_connection, $query);
            if (!$query)
                $result  = 'error';
                $message = 'query error';
            else
                $result  = 'success';
                $message = 'query success';

    elif (job == 'delete_company')

        # Delete company
        if (id == '')
            $result  = 'error';
            $message = 'id missing';
        else
            $query = "DELETE FROM it_companies WHERE company_id = '" . mysqli_real_escape_string(db_connection, id) . "'";
            $query = mysqli_query(db_connection, $query);
            if (!$query)
                $result  = 'error';
                $message = 'query error';
            else
                $result  = 'success';
                $message = 'query success';

"""
