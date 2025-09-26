def nlq_to_sql(nl_query):
    nl_query = nl_query.lower()
    
    sql = "SELECT * FROM students"
    
   
    numbers = [int(s) for s in nl_query.split() if s.isdigit()]
    number = numbers[0] if numbers else None
    
    if "above" in nl_query and number is not None:
        sql += f" WHERE marks > {number};"
    elif "below" in nl_query and number is not None:
        sql += f" WHERE marks < {number};"
    elif ("equal" in nl_query or "equals" in nl_query) and number is not None:
        sql += f" WHERE marks = {number};"
    else:
        sql += ";"
    
    return sql



if __name__ == "__main__":
    print("Natural Language to SQL Converter (Basic Rule-Based)")
    print("Example: 'Show all students with marks above 80'\n")
    
    user_query = input("Enter your query: ")
    sql_query = nlq_to_sql(user_query)
    
    print("\nGenerated SQL Query:")
    print(sql_query)